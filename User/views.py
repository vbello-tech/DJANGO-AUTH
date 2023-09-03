from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView, View, ListView
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
def signupview(request):
    if request.method == 'POST':
        form = NewUSerForm(request.POST)
        if form.is_valid():
            user = form.save()
            logger.info(f"{user.username} signed up @ {timezone.now()}")
            return redirect('/')
    else:
        form = NewUSerForm()

    context = {
        'form': form
    }
    return render(request, 'registrations/signup.html', context)

#login
class UserLoginView(View):
    def get(self, *args, **kwargs):
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(self.request, 'registrations/login.html', context)
    def post(self, backend='django.contrib.auth.backends.ModelBackend', *args, **kwargs):
        form = LoginForm(self.request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(self.request, user)
                return redirect('/')
            else:
                return redirect('user:login')
        else:
            return redirect ('user:sign')

#change password
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/')
    else:
        form = PasswordChangeForm(data=request.POST, user=request.user)

    context = {
        'form': form
    }
    return render(request, 'registrations/change_password.html', context)