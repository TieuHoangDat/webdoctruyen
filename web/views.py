from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import nameForm
# Create your views here.

def index(request):
    str = "hello"
    context = {
        "a" : str
    }
    return render(request,"index.html",context=context)

def login(request):
    if request.method == "POST":
        form = nameForm(request.POST)
        if form.is_valid():
            return HttpResponse("Good JObs")
    else:
        form = nameForm()

    return render(request, "login.html", {"form":form})
