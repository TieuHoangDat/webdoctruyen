from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("login",views.login,name="login"),
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('chapter/<int:chapter_id>', views.chapter, name="chapter"),
    path('novel/<int:novel_id>',views.novel,name="book"),
    path('novel/<int:novel_id>/dc',views.novel,name="discuss"),
    path('novel/<int:novel_id>/catalog', views.catalog, name="catalog")
]
