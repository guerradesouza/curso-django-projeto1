from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {
        'name':'Wilmar Guerra',
    }
    return render(request,'me-apague/temp.html', context)