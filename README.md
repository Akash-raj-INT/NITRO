# 📂 File Parser CRUD API (FastAPI)

A simple backend API to upload, parse, and manage files using **FastAPI**.  
Supports CRUD operations with progress tracking and file parsing.

---

## 🚀 Features
- Upload and parse files (CSV, JSON, Excel, etc.)
- Track upload & parsing progress
- List all uploaded files
- Retrieve file content
- Delete uploaded files
- Extensible parser system

---

## 🔑 Endpoints

### ➕ Upload File
`POST /files`

Upload a file using **form-data**:
- **Key**: `file`
- **Value**: (Choose File)

---

### 📃 List Files
`GET /files`

Returns CSV uploaded files.

---

### ⏳ Get Progress
`GET /files/{file_id}/progress`

Check parsing progress of a file.

---

### 📄 Get Content
`GET /files/{file_id}`

Retrieve parsed file content.

---

### ❌ Delete File
`DELETE /files/{file_id}`

Delete an uploaded file by ID.

---

## 🧠 Notes on Progress Tracking
- Upload progress uses **Content-Length** and chunked write (up to ~90%).
- Parsing progress advances from ~90% → 100% while rows are inserted in batches.

---

## 🔒 Authentication (Optional)
JWT authentication can be added:
```python
from fastapi.security import HTTPBearer

##🧪 Tests
Run tests with:

pytest -q

##🧩 Extending Parsers
Add a new module under app/parsers/ (e.g., excel_parser.py).

Update routes/files.py to route by file extension.

Call the appropriate background task.

##📬 Postman / Thunder Client
You can test the API using Postman or Thunder Client.

Example Collection
Save the following as postman_collection.json and import it:
{
  "info": {
    "name": "File Parser CRUD API",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Upload File",
      "request": {
        "method": "POST",
        "header": [],
        "body": {
          "mode": "formdata",
          "formdata": [
            { "key": "file", "type": "file", "src": "sample.csv" }
          ]
        },
        "url": { "raw": "http://localhost:8000/files", "host": ["http://localhost:8000"], "path": ["files"] }
      }
    },
    {
      "name": "List Files",
      "request": { "method": "GET", "url": { "raw": "http://localhost:8000/files", "host": ["http://localhost:8000"], "path": ["files"] } }
    },
    {
      "name": "Get Progress",
      "request": { "method": "GET", "url": { "raw": "http://localhost:8000/files/{{file_id}}/progress", "host": ["http://localhost:8000"], "path": ["files", "{{file_id}}", "progress"] } }
    },
    {
      "name": "Get Content",
      "request": { "method": "GET", "url": { "raw": "http://localhost:8000/files/{{file_id}}", "host": ["http://localhost:8000"], "path": ["files", "{{file_id}}"] } }
    },
    {
      "name": "Delete File",
      "request": { "method": "DELETE", "url": { "raw": "http://localhost:8000/files/{{file_id}}", "host": ["http://localhost:8000"], "path": ["files", "{{file_id}}"] } }
    }
  ]
}

API available at:
👉 http://127.0.0.1:8000

Docs available at:
👉 http://127.0.0.1:8000/docs

📌 Tech Stack
FastAPI

SQLite (default, can use PostgreSQL/MySQL)

Uvicorn

Pydantic

Pytest
