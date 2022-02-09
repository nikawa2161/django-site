from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

# Create your views here.

def index(request):
    objs = Article.objects.all()
    context = {
      'title': 'タイトル',
      'articles': objs,
    }
    return render(request, 'mysite/index.html', context)