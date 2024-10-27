from django.contrib import admin
from .models import Room, RoomImage

class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1  # Number of empty forms to display

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type', 'price', 'is_available')
    search_fields = ('room_number', 'room_type')
    list_filter = ('room_type', 'is_available')
    inlines = [RoomImageInline]  # Add inline model for images

admin.site.register(Room, RoomAdmin)
