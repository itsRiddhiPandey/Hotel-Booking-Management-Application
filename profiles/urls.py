from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('update/', views.update_profile_view, name='update_profile'),
]
