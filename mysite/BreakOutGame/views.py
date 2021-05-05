from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    return render(request,"breakout/index.html")
