from home.models import Post
from django.shortcuts import render
import random

# Create your views here.
def index(request):

    ids = [i.id for i in Post.objects.all()]
    random.shuffle(ids)
    shuffled = [Post.objects.get(id=i) for i in ids]

    context = {
        'shuffled': shuffled
    }

    return render(request, 'index.html', context)

def posts(request, cat):
    posts = Post.objects.filter(category=f'{cat}')

    if posts.count() == 0:
        return render(request, 'error.html')
    else:
        posts = Post.objects.filter(category=f'{cat}')

        context = {
            'posts': posts,
            'cat': cat
        }

        return render(request, 'posts.html', context)
