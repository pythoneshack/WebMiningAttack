from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'WebMining/home.html')


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs=FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

    return render(request, 'WebMining/upload.html', context)