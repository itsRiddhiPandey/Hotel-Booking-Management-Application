from django.shortcuts import render, get_object_or_404
from .models import Room

def homepage(request):
    return render(request, 'homepage.html')
def room_list(request):
    rooms = Room.objects.all()
    return render(request, '../templates/rooms/room_list.html', {'rooms': rooms})

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, '../templates/rooms/room_detail.html', {'room': room})
