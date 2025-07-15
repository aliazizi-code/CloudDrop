# S3 File Manager

A simple Django application for managing files in an S3-compatible storage.

## Features

- Upload files to S3 bucket
- List all files in the bucket
- Delete files from the bucket
- Generate pre-signed URLs for file access (valid for 1 hour)

## Requirements

- Python 3.x
- Django
- boto3 (AWS SDK for Python)

## Installation

1. Install dependencies:
   ```bash
   pip install --no-cache-dir -r requirements.txt
   ```

2. Configure your S3 settings in Django's `settings.py`:
   ```python
   AWS_S3_ENDPOINT_URL = 'your-s3-endpoint'
   AWS_ACCESS_KEY_ID = 'your-access-key'
   AWS_SECRET_ACCESS_KEY = 'your-secret-key'
   AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
   ```

## Views

- `upload_file`: Handles file uploads to S3 (POST method)
- `file_list`: Lists all files in the S3 bucket
- `delete_file`: Deletes a file from the S3 bucket (POST method)
- `generate_presigned_url`: Generates a temporary URL for file access

## Usage

1. Access the upload page to upload files
2. View the file list to see all uploaded files
3. Generate temporary URLs to share files
4. Delete files when no longer needed

## Error Handling

All views return JSON responses with error messages when something goes wrong (status code 500 for server errors, 400 for bad requests).
```
