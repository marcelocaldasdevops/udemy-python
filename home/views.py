from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):

    context = {
        'text': 'Ola home',
        'title': 'home'
        }

    return render(request, 'home/index.html', context)