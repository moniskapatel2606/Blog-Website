from django.shortcuts import render, redirect
from .models import *
from .forms import *

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
        
        article=Article.objects.filter(category=categories).all()# (that up variable name categories)
        context={
            'articles':article,
            'category':categories}
    return render(request,'article/categorised_article.html', context)

def post_articleform(request):

    form=ArticleForm()
    if request.method=='POST':
      form=ArticleForm(request.POST,request.FILES)
      if form.is_valid():
          
          form.save()
          return redirect('article:single_article',pk=form.instance.id)
   
    context={
        'form':form
    }
    return render(request,'article/article_form.html',context)
