from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.create_room, name='create_room'),
    path('rooms/<int:room_id>/', views.join_room, name='join_room'),
    path('rooms/<int:room_id>/messages/', views.send_message, name='send_message'),
]
