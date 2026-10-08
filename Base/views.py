from django.shortcuts import render

def home (request):
    return render (request, "home.html")

def detail (request):
    return render (request, "detail.html ")

def info (request):
    return render (request, "info.html ")

def avto_bozor (request):
    return render (request, "avto-bozor.html ")

def index (request):
    return render (request, "index.html ")