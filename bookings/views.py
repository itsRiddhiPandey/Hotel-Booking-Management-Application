# bookings/views.py
from django.core.exceptions import ValidationError
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404

from profiles.models import Profile
from .models import Booking
from rooms.models import Room
from .forms import BookingForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
@login_required
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

# View for creating a new booking
@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')  # Redirect to booking list after successful booking
    else:
        form = BookingForm()

    return render(request, 'bookings/create_booking.html', {'form': form})

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            login(request, user)  # Log in the user after registration
            return redirect('booking_list')  # Redirect to a page after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

# User login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()

            # Check if the user has a profile, create one if not
            try:
                profile = user.profile
            except Profile.DoesNotExist:
                # Create a new profile for the user if it doesn't exist
                Profile.objects.create(user=user)

            login(request, user)  # Log in the user
            return redirect('booking_list')  # Redirect after successful login
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})
# User logout view
def logout_view(request):
    logout(request)  # Log out the user
    return redirect('login')  # Redirect to login page after logout


def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        try:
            booking.delete()
            return redirect('booking_list')  # Redirect to a success page or view
        except ValidationError as e:
            return HttpResponseForbidden(str(e))

    return render(request, 'bookings/cancel_booking.html', {'booking': booking})