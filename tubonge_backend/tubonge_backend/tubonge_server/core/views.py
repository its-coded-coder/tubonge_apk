from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Room, Message
from tubonge_backend.tubonge_server.users.models import CustomUser

@csrf_exempt
def create_room(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        room = Room.objects.create(name=name)
        return JsonResponse({'room_id': room.id, 'name': room.name})

@csrf_exempt
def join_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return JsonResponse({'room_id': room.id, 'name': room.name, 'created_at': room.created_at})

@csrf_exempt
def send_message(request, room_id):
    if request.method == 'POST':
        room = get_object_or_404(Room, id=room_id)
        user = get_object_or_404(CustomUser, id=request.POST.get('user_id'))
        content = request.POST.get('content')
        message = Message.objects.create(room=room, user=user, content=content)
        return JsonResponse({'message_id': message.id, 'content': message.content, 'timestamp': message.timestamp})

@csrf_exempt
def meeting_history(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    rooms = Room.objects.filter(messages__user=user).distinct()
    history = [{'room_id': room.id, 'name': room.name, 'created_at': room.created_at, 'ended_at': room.ended_at} for room in rooms]
    return JsonResponse({'history': history})
