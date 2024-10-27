from django.db import models
from rooms.models import Room
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date


# bookings/models.py

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # Link to Room
    guest_name = models.CharField(max_length=100)
    check_in = models.DateField(null=True, blank=True)
    check_out = models.DateField(null=True, blank=True)
    is_confirmed = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)

    def cancel(self):
        print("cancel method called")
        self.is_canceled = True
        self.save()

    def __str__(self):
        return f"Booking for {self.guest_name} in room {self.room.room_type}"

    def __str__(self):
        return f"{self.guest_name} - {self.room.room_type}"

    def total_days(self):
        return (self.check_out - self.check_in).days

    def total_price(self):
        return self.total_days() * self.room.price

    def clean(self):
        # Ensure that both check_in and check_out are provided
        if self.check_in is None or self.check_out is None:
            raise ValidationError(_('Both check-in and check-out dates must be provided.'))

        # Ensure that the check-out date is after the check-in date
        if self.check_out <= self.check_in:
            raise ValidationError(_('Check-out date must be after check-in date.'))

        # Only check for overlapping bookings if this is a new or updated booking
        if not self.pk:  # Only validate if this is a new booking
            overlapping_bookings = Booking.objects.filter(
                room=self.room,
                check_in__lt=self.check_out,  # Check-in must be before the current check-out
                check_out__gt=self.check_in  # Check-out must be after the current check-in
            )
            if overlapping_bookings.exists():
                raise ValidationError(_('This room is already booked for the selected dates.'))

    def save(self, *args, **kwargs):
            # Ensure that the custom validation is run before saving
        self.clean()
        super().save(*args, **kwargs)

    def __str__ (self):
        return self.guest_name
    print("Booking model loaded")
# class Booking(models.Model):
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     guest_name = models.CharField(max_length=100)
#     check_in = models.DateField(null=True, blank=True)
#     check_out = models.DateField(null=True, blank=True)
#     is_confirmed = models.BooleanField(default=False)
#
#     def clean(self):
#         # Ensure that both check_in and check_out are provided
#         if self.check_in is None or self.check_out is None:
#             raise ValidationError(_('Both check-in and check-out dates must be provided.'))
#
#         # Ensure that the check-out date is after the check-in date
#         if self.check_out <= self.check_in:
#             raise ValidationError(_('Check-out date must be after check-in date.'))
#
#         # Check for overlapping bookings for the same room
#         overlapping_bookings = Booking.objects.filter(
#             room=self.room,
#             check_in__lt=self.check_out,  # Check-in must be before the current check-out
#             check_out__gt=self.check_in   # Check-out must be after the current check-in
#         )
#
#         if overlapping_bookings.exists():
#             raise ValidationError(_('This room is already booked for the selected dates.'))
#
#     def save(self, *args, **kwargs):
#         # Ensure that the custom validation is run before saving
#         self.clean()
#         super().save(*args, **kwargs)
# print("Booking model loaded")