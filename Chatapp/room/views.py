from django.shortcuts import render  ,redirect
from .models import Room , Message
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url = 'signin')
def rooms(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render (request , 'room/rooms.html' , context)

@login_required(login_url = 'signin')
def room(request , slug):
    room = Room.objects.get(slug = slug)
    chats = Message.objects.filter(room = room)
    context = {'room':room , 'chats':chats }
    return render (request , 'room/room.html' , context)