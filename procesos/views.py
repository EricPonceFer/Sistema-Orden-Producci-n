from django.shortcuts import render

def home(request):
    return render(request, 'procesos/home.html')
# Create your views here.
