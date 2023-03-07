from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# for home page
def index(request):
    return render(request,'index.html')