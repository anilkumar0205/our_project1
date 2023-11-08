from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def king(request):
    return HttpResponse('hi this is king')