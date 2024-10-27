# bookings/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_list, name='booking_list'),  # List all bookings
    path('new/', views.create_booking, name='create_booking'),  # Create a new booking
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),

]
