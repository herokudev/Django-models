from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePage(request):
  return HttpResponse('This is the hello world app Home page')
  