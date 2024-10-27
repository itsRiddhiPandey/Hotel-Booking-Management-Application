# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UpdateProfileForm, UpdateUserForm
from .models import Profile
@login_required
def profile_view(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    return render(request, 'profiles/profile.html', {'user': user, 'profile': profile})
@login_required
def update_profile_view(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was updated successfully!')
            return redirect('profile')  # Redirect back to profile view after updating
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=profile)

    return render(request, 'profiles/update_profile.html', {'user_form': user_form, 'profile_form': profile_form})
