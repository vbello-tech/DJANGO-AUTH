from django.urls import path
from .views import (
    UserProfile,
    signupview,
    login,
    change_password,
)

app_name = "user"

urlpatterns = [
    path('profile/', UserProfile, name="profile"),
    path('signup/', signupview, name="signup"),
    path('login/', login, name="login"),
    path('change-password/', change_password, name="change_password"),
]