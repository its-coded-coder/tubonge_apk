
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/signaling/', consumers.MyConsumer.as_asgi()),
]
