from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, update_session_auth_hash
from django.core.exceptions import ObjectDoesNotExist
import logging
from django.utils import timezone
from .forms import (
    NewUSerForm,
    LoginForm,
)

logger = logging.getLogger(__name__)

#user profile
def UserProfile(request):
    context = {
        'user':request.user
    }
    return render(request, 'registrations/profile.html', context)

#sign up
class SignupView(View):
    def get(self, *args, **kwargs):
        form = NewUSerForm()
        context = {
            'form': form
        }
        return render(self.request, 'registrations/signup.html', context)
    def post(self, *args, **kwargs):
        if self.request.method == 'POST':
            form = NewUSerForm(self.request.POST)
            if form.is_valid():
                user = form.save()
                logger.info(f"{user.username} signed up @ {timezone.now()}")
                return redirect('/')
            else:
                form = NewUSerForm()

#login
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
            return redirect ('user:login')

#change password
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


