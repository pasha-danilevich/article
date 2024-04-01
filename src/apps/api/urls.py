from django.urls import path, include
from apps.api import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'articles', views.ArticlesViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    # GET/POST
    # GET/PUT/PATCH/DELETE
    path('', include(router.urls)),

    # path('auth/', include('rest_framework.urls')),

    # JWT auth
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # auth
    path('auth/registration/', views.RegistrationAPIView.as_view()),
    path('auth/login/', views.LoginAPIView.as_view())

]
