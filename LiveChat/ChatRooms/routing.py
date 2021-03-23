# Routing is the WS equivalent of URLS
from django.urls import re_path  # adv pathing
from ChatRooms.consumers import ChatRoomConsumer


ChatRoom_ws_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatRoomConsumer.as_asgi()),
]
