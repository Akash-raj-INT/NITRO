from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/progress/(?P<file_id>[0-9a-f-]+)/$', consumers.ProgressConsumer.as_asgi()),
]
