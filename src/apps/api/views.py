from django.http import Http404
from django.contrib.auth.models import User


from rest_framework import views
from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from apps.api.serializers import ArticleSerializer, UserSerializer, CreateUserSerializer
from apps.article.models import Article
from apps.api.permissions import UserPermission

class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes  = (UserPermission,)

    def get_queryset(self):
        return self.queryset
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    





class RegistrationAPIView(views.APIView):
    
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.create(validated_data=serializer.validated_data)
            refresh = RefreshToken.for_user(user)   

            refresh.payload.update({
                'user_id': user.id,
                'username': user.username
            })
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token), # Отправка на клиент
            }) 

class LoginAPIView(views.APIView):

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        
        if username is None or password is None:
            return Response({'error': 'Нужен и логин, и пароль'})
        
        user = User.objects.get(username = username)
        refresh = RefreshToken.for_user(user)

        refresh.payload.update({
            'user_id': user.id,
            'username': user.username
        })

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
        






