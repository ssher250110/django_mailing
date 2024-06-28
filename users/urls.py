from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateView, UserResetPasswordView, ProfileView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', UserCreateView.email_verification, name='email-confirm'),
    path('reset-password/', UserResetPasswordView.as_view(template_name='users/user_reset_password.html'),
         name='reset-password'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
