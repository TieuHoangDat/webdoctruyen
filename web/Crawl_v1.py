import sqlite3
import requests 
import json
import os
import random
from .models import Author,Genre,Novel,Chapter,NovelAuthor,NovelGenre

base_url = "https://api.truyenfull.vn"
dir_path = "D:\\ChapterContent"
list_book_all = "/v1/story/all?type=story_update&page="
list_books_by_genre = "/v1/story/cate?cate=linh_di&type=story_new&page="
book_info = "/v1/story/detail/"
def url_chapterlist_by_id(novel_id):
    return base_url + "/v1/story/detail/" + str(novel_id) + "/chapters"
chapter_list = "/v1/story/detail/34845/chapters"
chapter_info = "/v1/chapter/detail/"

# res = requests.get(base_url + list_books_by_genre + "1")
# f = open('new1.json',"w")
# f.write(res.text)
# f.close()
def get_book_detail(book_id):
    res = requests.get(base_url+book_info+str(book_id))
    print(base_url+book_info+str(book_id))
    novel_info = res.json()['data']
    categories = str(novel_info["categories"]).split(",")
    category_ids = str(novel_info["category_ids"]).strip().split(",")
    #print("Categori" + str(category_ids))
    genres = zip(categories,category_ids)
    # for genre,id in genres:
    #     print(id,genre)
    #     try:
    #         genre = Genre.objects.get(id=id)
    #         print("exist :" + str(genre))
    #     except Genre.DoesNotExist:
    #        res = Genre.objects.update_or_create(id=id,name=genre)
    #        print("Not exist: " + str(res))
    author = novel_info['author']

    cover = novel_info['image']
    total_likes = random.randint(0,1000)
    total_views = random.randint(100,100000)
    status = str(novel_info['status'])
    description = str(novel_info['description'])
    rating = round(random.uniform(1.0,5.0),2)
    title = str(novel_info['title'])
    try:
        novel = Novel.objects.get(title=title)
        chapter = Novel.objects.get(novel_id=novel.id)
        if chapter.DoesNotExist:
            get_chapterlist_by_id(novel_id=novel.id)
        # if category_ids[0] != "": 
        #     for genre_id in category_ids:
        #         NovelGenre.objects.get_or_create(genre_id=int(genre_id),novel_id=novel.id)
        # print(novel.title)
    except Novel.DoesNotExist:
        novel, _ = Novel.objects.get_or_create(cover=cover,total_likes=total_likes,total_views=total_views,status=status,description=description,rating=rating,title=title)
        author,_ = Author.objects.get_or_create(name=author)
        #print("author_id: "+str(author.id) +" novel_id: " + str(novel.id))
        NovelAuthor.objects.get_or_create(novel_id=novel.id, author_id=author.id)
        get_chapterlist_by_id(novel_id=novel.id)
        if category_ids[0] != "":    
            for genre_id in category_ids:
                #print("45: "+genre_id)
                NovelGenre.objects.get_or_create(genre_id=int(genre_id),novel_id=novel.id)
     
    print("INSERT")


def get_chapterlist_by_id(novel_id):
    res = requests.get(url_chapterlist_by_id(novel_id=novel_id))
    chapter_list = res.json()['data']
    for chapter in chapter_list:
        get_chapter_by_id(chapter_id=chapter['id'],novel_id=novel_id)


def get_chapter_by_id(chapter_id,novel_id):
    res = requests.get(base_url+chapter_info+str(chapter_id))
    data = res.json()['data']
    title = data['chapter_name']
    chapter_number = data['position']
    novel_id = int(novel_id)
    content = data['content']
    
    chapter,_ = Chapter.objects.get_or_create(title=title,chapter_number=chapter_number,novel_id=novel_id)
    file_path = dir_path +"\\" +str(novel_id)+"\\"+str(chapter.id)+".txt"
    chapter.path = file_path
    chapter.save()
    if not os.path.exists(dir_path+"\\"+str(novel_id)):
        os.makedirs(dir_path+"\\"+str(novel_id))
    
    print(file_path)
    with open(file_path,"w",encoding='utf-8') as file:
        file.write(content)
    print(title)
    





def fetch_list_books_by_genre(url,page):
    res = requests.get(url+page)
    list_book_id = res.json()["data"]
    #print(list_book_id)
    for id in list_book_id:
        get_book_detail(id['id'])
for i in range(6,10):
    print(i)
    fetch_list_books_by_genre(base_url+list_book_all,str(i))



