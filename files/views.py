import boto3
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Initialize S3 Client
def get_s3_client():
    return boto3.client(
        's3',
        endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )


@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        s3_client = get_s3_client()
        file = request.FILES['file']
        try:
            s3_client.upload_fileobj(file, settings.AWS_STORAGE_BUCKET_NAME, file.name)
            return redirect('file_list')
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
    return render(request, 'files/upload.html')



def file_list(request):
    s3_client = get_s3_client()
    try:
        response = s3_client.list_objects_v2(Bucket=settings.AWS_STORAGE_BUCKET_NAME)
        files = [obj['Key'] for obj in response.get('Contents', [])]
        return render(request, 'files/list.html', {'files': files})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
def delete_file(request):
    if request.method == 'POST':
        file_name = request.POST.get('file_name')
        if not file_name:
            return JsonResponse({'error': 'File name is required'}, status=400)
        s3_client = get_s3_client()
        
        try:
            s3_client.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=file_name)
            return redirect('file_list')
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


def generate_presigned_url(request):
    file_name = request.GET.get('file_name')
    if not file_name:
        return JsonResponse({'error': 'File name is required'}, status=400)
    s3_client = get_s3_client()
    try:
        url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME, 'Key': file_name},
            ExpiresIn=3600  # URL valid for 1 hour
        )
        return redirect(url)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

