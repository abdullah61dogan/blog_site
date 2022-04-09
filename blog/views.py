from logging import lastResort
from django.shortcuts import render
from tomlkit import date

# Create your views here.


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = posts.sort(key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
      "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
