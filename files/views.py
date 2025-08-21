import csv, json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import FileRecord
from .serializers import FileRecordSerializer

class FileUploadView(APIView):
    def post(self, request):
        uploaded_file = request.FILES.get("file")
        if not uploaded_file:
            return Response({"error": "No file provided"}, status=400)

        # Create record
        record = FileRecord.objects.create(
            file=uploaded_file,
            filename=uploaded_file.name,
            status="uploading",
            progress=0,
        )

        # Simulate parsing (CSV only here)
        try:
            decoded = uploaded_file.read().decode("utf-8").splitlines()
            reader = csv.DictReader(decoded)
            data = [row for row in reader]

            record.parsed_json = data
            record.status = "ready"
            record.progress = 100
            record.save()

        except Exception as e:
            record.status = "failed"
            record.save()
            return Response({"error": str(e)}, status=500)

        return Response(FileRecordSerializer(record).data, status=201)


class FileProgressView(APIView):
    def get(self, request, pk):
        record = get_object_or_404(FileRecord, pk=pk)
        return Response({"file_id": str(record.id), "status": record.status, "progress": record.progress})


class FileContentView(APIView):
    def get(self, request, pk):
        record = get_object_or_404(FileRecord, pk=pk)
        if record.status != "ready":
            return Response({"message": "File upload or processing in progress. Try later."}, status=202)
        return Response({"file_id": str(record.id), "data": record.parsed_json})


class FileListView(APIView):
    def get(self, request):
        records = FileRecord.objects.all().order_by("-created_at")
        return Response(FileRecordSerializer(records, many=True).data)


class FileDeleteView(APIView):
    def delete(self, request, pk):
        record = get_object_or_404(FileRecord, pk=pk)
        record.delete()
        return Response({"message": "Deleted", "file_id": str(pk)})
