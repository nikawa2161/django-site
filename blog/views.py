from django.shortcuts import render
from blog.models import Article
from django.core.paginator import Paginator

# Create your views here.

def index(request):
  objs = Article.objects.all()
  paginator = Paginator(objs, 2) #paginatorでpage=1とかをつけてくれる
  page_number = request.GET.get('page')

  context = {
    'page_obj': paginator.get_page(page_number),
    'page_number': page_number,
  }
  return render(request, 'blog/blogs.html', context)

def article(request, pk): #urlで使用しているpkが変数として使用可能になる。
  obj = Article.objects.get(id=pk) #idと同じArticel.modesがオブジェクトを取得
  context = {
    'article': obj
  }
  return render(request, 'blog/article.html', context)