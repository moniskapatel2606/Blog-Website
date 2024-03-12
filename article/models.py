from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Categorie'

class  Article(models.Model):

    author=models.ForeignKey(User, on_delete=models.CASCADE,default=1)

    category=models.ForeignKey(category,on_delete=models.CASCADE,default=1)
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=8000)
    image=models.ImageField(upload_to='article_img/',default='default_img.jpg')#folder name  (pip install pillow)
    pub_date=models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("Users:profile")
    