from django.shortcuts import render
from .models import *

# Create your views here.

# context processor
def categories(request):
    categories=category.objects.all()

    return {
        'categories':categories,
    }
    

def index(request):

    all_articles=Article.objects.all()

    context={'articles':all_articles}
    return render(request,'article/index.html',context)



def single_article(request,pk):
    article=Article.objects.get(pk=pk)
    context={
        'article':article
    }
    return render(request,'article/article.html',context)

def categorised_article(request,pk):
    if pk==0:
        article=Article.objects.all()
        context={
        'articles':article,
        'category':'all'}
    else:
        categories=category.objects.get(pk=pk)
        article=Article.objects.filter(category=categories).all()
        context={
            'articles':article,
            'category':categories}
    return render(request,'article/categorised_article.html', context)
