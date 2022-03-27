from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def test(request):
    return HttpResponse('<h1>Hello World</h1>')

def Home(request):
    return render(request,'HomePage.html')

def Service(request):
    return render(request,'service.html')

def contract(request):
    return render(request,'contract.html')

def talk(request):
    if request.method == 'POST':
        data = request.POST.copy()
        title = data.get('title')
        email = data.get('email')
        comment = data.get('comment')
        
       # print(tile, email, comment)
        new1 = contract()
        new1.title = title
        new1.email = email
        new1.comment = comment
        new1.save()
        
    return render(request,'talk_me.html')
