from django.urls import path
from .views import UserProfile

app_name = "user"

urlpatterns = [
    path('profile/', UserProfile, name="prodile"),
]