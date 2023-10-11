from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("login",views.login,name="login"),
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('search/', views.search, name="search"),
    path('logout/', views.logoutPage, name="logout"),
    path('chapter/<int:chapter_id>', views.chapter, name="chapter"),
    path('novel/<int:novel_id>',views.novel,name="book"),
    path('novel/<int:novel_id>/dc',views.discuss,name="discuss"),
    path('novel/<int:novel_id>/add_comment/', views.add_comment, name='add_comment'),
    path('novel/<int:novel_id>/catalog', views.catalog, name="catalog")
]
