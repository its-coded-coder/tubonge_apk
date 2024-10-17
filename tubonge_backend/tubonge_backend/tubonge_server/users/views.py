from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = CustomUser.objects.create_user(username=username, password=password)
        return JsonResponse({'user_id': user.id, 'username': user.username})

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'user_id': user.id, 'username': user.username})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
