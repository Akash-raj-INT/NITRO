import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import UploadedFile

class ProgressConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.file_id = self.scope['url_route']['kwargs']['file_id']
        await self.accept()

    async def receive(self, text_data):
        file = UploadedFile.objects.get(id=self.file_id)
        await self.send(text_data=json.dumps({
            "file_id": str(file.id),
            "status": file.status,
            "progress": file.progress
        }))
