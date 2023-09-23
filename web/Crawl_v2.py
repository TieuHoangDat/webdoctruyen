#
import os
import random
import requests
from .models import Author, Genre, Novel, Chapter, NovelAuthor, NovelGenre

BASE_URL = "https://api.truyenfull.vn"
DIR_PATH = "D:\\ChapterContent"

def fetch_novel_details(novel_id):
    """Fetch and save details of a novel."""
    response = requests.get(f"{BASE_URL}/v1/story/detail/{novel_id}")
    data = response.json()['data']

    author, _ = Author.objects.get_or_create(name=data['author'])

    novel, _ = Novel.objects.get_or_create(
        title=data['title'],
        cover=data['image'],
        total_likes=random.randint(0, 1000),
        total_views=random.randint(100, 100000),
        status=data['status'],
        description=data['description'],
        rating=round(random.uniform(1.0, 5.0), 2),
    )

    NovelAuthor.objects.get_or_create(novel_id=novel.id, author_id=author.id)

    for genre_id in data["category_ids"].strip().split(","):
        if genre_id:
            NovelGenre.objects.get_or_create(genre_id=int(genre_id), novel_id=novel.id)

    fetch_chapters(novel_id)

def fetch_chapters(novel_id):
    response = requests.get(f"{BASE_URL}/v1/story/detail/{novel_id}/chapters")
    chapters = response.json()['data']

    for chapter in chapters:
        fetch_chapter(chapter['id'], novel_id)

def fetch_chapter(chapter_id, novel_id):
    response = requests.get(f"{BASE_URL}/v1/chapter/detail/{chapter_id}")
    data = response.json()['data']

    chapter, _ = Chapter.objects.get_or_create(
        title=data['chapter_name'],
        chapter_number=data['position'],
        novel_id=novel_id,
    )

    directory = os.path.join(DIR_PATH, str(novel_id))
    os.makedirs(directory, exist_ok=True)

    file_path = os.path.join(directory, f"{chapter.id}.txt")
    chapter.path = file_path
    chapter.save()

    with open(file_path, "w", encoding='utf-8') as file:
        file.write(data['content'])

def fetch_novels(page):
    response = requests.get(f"{BASE_URL}/v1/story/all?type=story_update&page={page}")
    novels = response.json()["data"]

    for novel in novels:
        fetch_novel_details(novel['id'])

def main():
    for i in range(1, 5):
        fetch_novels(i)

