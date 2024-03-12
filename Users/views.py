from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth.models import User
from article.models import *


# Create your views here.

def register(request):
    if request.method=='POST':
        form=NewRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('article:login')
    else:
        form=NewRegisterForm()
    # form=NewRegisterForm()
    context={
        'forms':form
    }
    return render(request,'Users/register.html',context)

def  profile(request):
    articles=Article.objects.filter(author=request.user).all().order_by('-pub_date')
    context={
        'articles':articles
    }
    return render(request,'Users/profile.html',context)


def edit_profile(request):
    try:
        profile=request.user.profile
    except profile.DoesNotExist:
        profile=None
    
    if request.method=='POST':
        if profile:
            profile.user=request.user
            profile.first_name=request.POST.get("first_name")
            profile.last_name=request.POST.get("last_name")
            profile.contact_number=request.POST.get("contact_number")
            # profile.image=request.FILES.get("image")
            profile.bio=request.POST.get("bio")
            if request.FILES.get('image'):
                profile.image=request=request.FILES['image']
            profile.save()
        else:
            user=request.user
            first_name=request.POST.get("first_name")
            last_name=request.POST.get("last_name")
            contact_number=request.POST.get("contact_number")
            image=request.FILES.get("image")
            bio=request.POST.get("bio")

            profile=Profile(user=user,first_name=first_name,image=image,bio=bio,contact_number=contact_number,last_name=last_name)
            profile.save()

        return redirect("Users:profile")
    context={
        'profile':profile
    }

    return render(request,'Users/edit_profile.html',context)

def author_profile(request,pk):
    author=User.objects.get(pk=pk)
    article_count=Article.objects.filter(author=author).count()
    context={
        'author':author,
        'article_count':article_count
    }
    return render(request,'Users/author_profile.html',context)


