from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    lineCount = request.GET['fulltext']
    #print(lineCount)
    return render(request, 'count.html',{'fulltext':lineCount})
