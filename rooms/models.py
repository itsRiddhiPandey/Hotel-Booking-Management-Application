# rooms/models.py
from django.db import models

class Room(models.Model):
    ROOM_TYPES = (
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Suite', 'Suite'),
    )

    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='room_photos/',null=True, blank=True)
    amenities = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_number} - {self.room_type}"

class RoomImage(models.Model):
    room = models.ForeignKey(Room, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='room_photos/additional/',null=True, blank=True)

    def __str__(self):
        return f"Image for Room {self.room.room_number}"