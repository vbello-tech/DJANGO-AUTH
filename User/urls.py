from django.urls import path
from .views import (
    UserProfile,
    signupview,
    UserLoginView,
    changepassword,
)

app_name = "user"

urlpatterns = [
    path('profile/', UserProfile, name="profile"),
    path('signup/', signupview, name="signup"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('change-password/', changepassword, name="change_password"),
]