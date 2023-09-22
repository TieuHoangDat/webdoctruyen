from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import nameForm
from .models import Novel
# Create your views here.

def index(request):
    str = "hello"
    context = {
        "top_like" : Novel.objects.all().order_by("-total_likes")[:10]
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
