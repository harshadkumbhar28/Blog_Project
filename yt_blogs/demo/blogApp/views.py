from django.shortcuts import render
from .models import Post, Category


# Create your views here.

def index(request):
    popular_post = Post.objects.filter(Section='Popular', Status="Publish").order_by('-id')[0:4]
    recent_post = Post.objects.filter(Section="Recent", Status="Publish").order_by('-id')[0:4]
    main_post = Post.objects.filter(Main_post=True, Status="Publish")[0:1]
    editor_pick = Post.objects.filter(Section="Editors_Pick", Status="Publish").order_by("-id")[0:1]
    editor_pick1 = Post.objects.filter(Section="Editors_Pick", Status="Publish").order_by("-id")[0:4]
    Trending = Post.objects.filter(Section="Trending", Status="Publish").order_by("-id")
    inspiration = Post.objects.filter(Section="Inspiration", Status="Publish").order_by("-id")[0:2]
    latest_post = Post.objects.filter(Section="Latest_Post", Status="Publish").order_by("-id")[0:4]
    images = Post.objects.filter().order_by("-id")[0:6]

    category = Category.objects.all()[0:4]

    context = {
        "popular_post": popular_post,
        "recent_post": recent_post,
        "main_post": main_post,
        "editor_pick": editor_pick,
        "editor_pick1": editor_pick1,
        "Trending": Trending,
        "inspiration": inspiration,
        "latest_post": latest_post,
        "category": category,
        "images": images
    }

    return render(request, 'index.html', context)


def base(request):
    return render(request, 'base.html')
