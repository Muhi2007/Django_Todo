from django.shortcuts import render

def home(request):
    return render(request, template_name='todos/home.html')

def about(request):
    return render(request, template_name='todos/about.html')