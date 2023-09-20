from django.urls import path
from .views import (
    UserProfile,
    SignupView,
    LoginView,
    ChangePasswordView,
)

app_name = "user"

urlpatterns = [
    path('profile/', UserProfile, name="profile"),
    path('signup/', SignupView, name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('change-password/', ChangePasswordView.as_view(), name="change_password"),
]