from django.urls import path
from django.urls import path, reverse_lazy
from .views import (
    UserProfile,
    SignupView,
    LoginView,
    ChangePasswordView,
)

from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetCompleteView,
)

app_name = "user"

urlpatterns = [
    #authentication 1
    path('profile/', UserProfile, name="profile"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('change-password/', ChangePasswordView.as_view(), name="change_password"),

    # authentication 2

    # PasswordResetView sends the mail
    path('reset-password/', PasswordResetView.as_view(
        template_name='registrations/password_reset.html',
        success_url=reverse_lazy('resume:password_reset_done')
    ), name="password_reset"),

    # PasswordResetDoneView shows a success message for the above
    path('password-reset-done/', PasswordResetDoneView.as_view(
        template_name='registrations/password_reset_done.html'),
        name="password_reset_done"),

    # PasswordResetConfirmView checks the link the user clicked and prompts for a new password
    path('password-reset-confirm/(<uidb64>)-(<token>)/', PasswordResetConfirmView.as_view(
        template_name='registrations/password_reset_confirm.html',
        success_url=reverse_lazy('resume:password_reset_complete')
    ), name="password_reset_confirm"),

    # PasswordResetCompleteView shows a success message for the above
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(template_name='registrations/password_reset_complete.html'),
         name="password_reset_complete"),

]