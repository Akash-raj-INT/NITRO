import uuid
from django.db import models

class FileRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to="uploads/")        # store uploaded file
    filename = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default="uploading")  # uploading/processing/ready/failed
    progress = models.IntegerField(default=0)
    parsed_json = models.JSONField(null=True, blank=True)  # Django 3.1+
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.filename
