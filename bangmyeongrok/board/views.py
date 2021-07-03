from django.shortcuts import render, redirect
from .models import Dongbang
# Create your views here.
def home(request):
    dongbangs = Dongbang.objects
    return render(request, 'home.html',{'dongbangs':dongbangs})

def submit(request):
    bang = Dongbang()
    bang.message = request.GET['message']
    bang.writer = request.GET['writer']
    bang.date = request.GET['date']
    bang.save()
    return redirect('/')