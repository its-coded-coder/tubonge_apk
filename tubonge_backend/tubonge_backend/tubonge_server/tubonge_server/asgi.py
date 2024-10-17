
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from core import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tubonge_server.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/some_path/", consumers.MyConsumer.as_asgi()),
        ])
    ),
})
