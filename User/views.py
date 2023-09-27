import logging

from django.conf import settings
from django.contrib import auth
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import View
from .forms import (
    NewUSerForm,
    LoginForm,
)

logger = logging.getLogger(__name__)


# user profile
def userprofile(request):
    context = {
        'user': request.user
    }
    return render(request, 'registrations/profile.html', context)


# sign up
class SignupView(View):
    def get(self, *args, **kwargs):
        form = NewUSerForm()
        context = {
            'form': form
        }
        return render(self.request, 'registrations/signup.html', context)

    def post(self, *args, **kwargs):
        form = NewUSerForm(self.request.POST)
        if form.is_valid():
            user = form.save()
            logger.info(f"{user.username} signed up @ {timezone.now()}")
            user_mail = user.email
            print(user_mail)
            subject = 'Thank you for registering to our site'
            message = ' it  means a world to us '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user_mail]
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)
            return redirect('/')
        else:
            form = NewUSerForm()


def signup_view(request):
    if request.method == 'POST':
        form = NewUSerForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            logger.info(f"{user.username} signed up @ {timezone.now()}")
            user_mail = user.email
            print(user_mail)
            subject = 'Thank you for registering to our site'
            message = ' it  means a world to us '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user_mail]
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)
            return redirect('/')
    else:
        form = NewUSerForm()

    context = {
        'form': form
    }
    return render(request, 'registrations/signup.html', context)


# login
class LoginView(View):
    def get(self, *args, **kwargs):
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(self.request, 'registrations/login.html', context)

    def post(self, *args, **kwargs):
        form = LoginForm(self.request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(self.request, username=username, password=password)
            auth.login(self.request, user)
            logger.info(f"{username} signed up @ {timezone.now()}")
            return redirect('/')
        else:
            return redirect('user:login')


# change password
class ChangePasswordView(View, LoginRequiredMixin):
    def get(self, *args, **kwargs):
        form = PasswordChangeForm(user=self.request.user)
        context = {
            'form': form
        }
        return render(self.request, 'registrations/change_password.html', context)

    def post(self, *args, **kwargs):
        if self.request.method == 'POST':
            form = PasswordChangeForm(data=self.request.POST, user=self.request.user)
            if form.is_valid():
                form.save()
                update_session_auth_hash(self.request, form.user)
                logger.info(f"{self.request.user.username} changed password @ {timezone.now()}")
                return redirect('/')
        else:
            form = PasswordChangeForm(user=self.request.user)


class LogoutView(View, LoginRequiredMixin):
    def post(self, *args, **kwargs):
        auth.logout(self.request)
        return HttpResponseRedirect('/')
