from django.shortcuts import render, redirect
from .forms import LogForm
from .models import Log
from .General import *


# Create your views here.


def home(request):
    traffic = {}
    traffic['requests'] = get_total_requests()
    traffic['traffic'] = get_total_traffic()
    traffic['frenq_status'] = freq_status()
    traffic['unique_ip'] = get_total_unique_ip()
    traffic['total_5xx'] = get_total_5xx_status()

    return render(request, 'WebMining/home.html', traffic)


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