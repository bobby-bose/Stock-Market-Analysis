# myapp/views.py
from django.shortcuts import render

def home(request):

    return render(request, 'homepage.html')

def info(request):
    return render(request, 'info.html')

def seasoned(request):
    return render(request, 'seasoned.html')

def novice(request):
    return render(request, 'novice.html')

def analysis(request):
    return render(request, 'analysis.html')

def chat(request):
    return render(request, 'chat.html')
