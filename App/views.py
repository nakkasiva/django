from django.shortcuts import render
from django.http import HttpResponse
from .models import Details

# Create your views here.
def sample(request):
    context={
        "flights":Details.objects.all()
    }
    return render(request,"index.html",context)