from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .forms import LogForm
from .models import Log
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


def logfiles_list(request):
    logs = Log.objects.all()
    return render(request, 'WebMining/logfiles_list.html', {
        'logs': logs
    })


def upload_log(request):
    if request.method == 'POST':
      form = LogForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
      return redirect('logfiles_list')
    else:
     form = LogForm()
    return render(request, 'WebMining/upload_log.html', {
        'form': form
    })