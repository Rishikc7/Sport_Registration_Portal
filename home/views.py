from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse('<h1>hello guys</h1>')
    return render(request, 'home/homepage.html')


