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
    context = {}
    if request.method == 'POST':
        data = request.POST.copy()
        title = data.get('title')
        email = data.get('email')
        comment = data.get('comment')
        #print(title, email, comment)
        
        if title == '' or email == '' or comment == '':
            context['status'] = 'alert'
            return render(request,'talk_me.html',context)
        
        new = contract_1()
        new.title = title
        new.email = email
        new.comment = comment
        new.save()
        
        context['status']='status'
        
    return render(request,'talk_me.html',context)
