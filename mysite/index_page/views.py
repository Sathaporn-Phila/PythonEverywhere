from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    return render(request,"index_page/index.html")
def breakout(request):
    return render(request,"index_page/breakout.html")