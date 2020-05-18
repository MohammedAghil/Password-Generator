from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def Home(request):
    return render(request,'password/home.html')

def Password(request):

    length = int(request.GET.get("length",12))

    characters = list('abcdefghijklmnopqrstuvwxyz')
    pwd = ''
    if(request.GET.get("uppercase")):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if (request.GET.get("special")):
        characters.extend(list('#$%^&*!@_+'))
    if (request.GET.get("numbers")):
        characters.extend(list('0123456789'))

    for i in range(0,length):
        pwd = pwd+ random.choice(characters)

    return render(request,'password/passwordgenerated.html',{'password':pwd})

def About(request):
    return render(request,'password/about.html')