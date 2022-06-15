from http.client import OK
from pdb import post_mortem
from django.shortcuts import render
from pos.models import Super


# Create your views here.

def index(request):
    posts = Super.objects.all()
    context = {'posts': posts,}

    return render(request,'index.html', context)


def details(request):
    #post = Super.objects.get(OK)
    return render(request,'details.html')
