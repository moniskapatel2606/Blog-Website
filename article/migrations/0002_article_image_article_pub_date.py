# Generated by Django 5.0.1 on 2024-01-25 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='default_img.jpg', upload_to='article_img/'),
        ),
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateField(auto_now=True),
        ),
    ]
