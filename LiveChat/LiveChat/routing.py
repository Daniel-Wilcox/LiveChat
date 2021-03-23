# Routing is the WS equivalent of URLS
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from ChatRooms.routing import ChatRoom_ws_urlpatterns

# This is how to route a WS request
applications = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            ChatRoom_ws_urlpatterns,
        )
    ),

})
