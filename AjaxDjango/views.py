from django.shortcuts import render
from DjangoProject.settings import BASE_DIR
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
import os
import shutil
# Create your views here.
def home(request):
    return render(request,'main.html')

def loadFile(request):
    if request.method == "POST":
        shutil.rmtree(os.path.join(BASE_DIR, 'media'))
        url = request.POST.get('w_name', '')
        files = request.FILES.get('fileToUpload', '')
        fs=FileSystemStorage()
        fs.save(files.name, files)
        with open(os.path.join(BASE_DIR, 'media', files.name)) as f:
            preview = f.readlines()
        f.close()
        print("preview \n", preview)
        previewFile = "".join(preview)
        return JsonResponse({'status': 'File Saved','file':previewFile},safe=False)
    else:
        return JsonResponse({'status': 'GET CALL'})

