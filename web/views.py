from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def add_comment(request, novel_id):
    if request.method == 'POST':
        novel = Novel.objects.get(pk=novel_id)
        comment_text = request.POST.get('comment_text')
        if comment_text!="":
            Comment.objects.create(novel=novel, user=request.user, comment_text=comment_text)
    return redirect('discuss', novel_id=novel_id)


def get_genre_list():
    return Genre.objects.all()

def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        keys = Novel.objects.filter(title__contains = searched)
        # Lọc theo trạng thái
        status = request.POST["status"]
        if status:
            keys = keys.filter(status=status)

        # Lọc theo đánh giá
        rate = request.POST["rate"] 
        if rate:       
            keys = keys.filter(rating__gte=rate)

        # Lọc theo thể loại
        genre = request.POST["genre"]
        if genre:
            keys = keys.filter(genres=genre)
    return render(request, 'search.html', {"searched": searched, "keys":keys})   



def index(request):
    top_like =  Novel.objects.all().order_by("-total_likes")[5:13]

    context = {
        "top_like" : top_like,
      
    }
    return render(request,"index.html",context=context)

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}  
    return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'user or password not correct!')

    context = {}
    return render(request, 'login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('index')

def chapter(request,chapter_id):
    chapter = Chapter.objects.get(id=chapter_id)
    path = chapter.path
    with open(path,mode="r", encoding="utf-8") as file:
       content =  file.read()
      # print(content)
    context = {
        "chapter" : chapter,
        "content" : content
     }
    return render(request, "web/chapter.html", context=context)

def novel(request, novel_id):
    novelObj =  Novel.objects.get(id=novel_id)
    context = {
        "NovelInfo" : novelObj,
        "AuthorInfo" : novelObj.authors.all(),
        "GenreInfo" : novelObj.genres.all()
    }
    return render(request,"web/novel.html",context=context)

def discuss(request, novel_id):
    novelObj =  Novel.objects.get(id=novel_id)
    context = {
        "NovelInfo" : novelObj,
        "AuthorInfo" : novelObj.authors.all(),
        "GenreInfo" : novelObj.genres.all()
    }
    return render(request,"web/discuss.html",context=context)

def catalog(request, novel_id):
    novelObj =  Novel.objects.get(id=novel_id)
    chapters = Chapter.objects.filter(novel=novelObj).order_by('chapter_number')
    context = {
        "NovelInfo" : novelObj,
        'chapters': chapters
    }
    return render(request,"web/catalog.html",context=context)