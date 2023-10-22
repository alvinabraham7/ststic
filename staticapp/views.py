from django.shortcuts import render
from .models import football

# Create your views here.


def index(request):
    obj=football.objects.all()
    return render(request, "index.html",{'result':obj})




# Create your views here.
