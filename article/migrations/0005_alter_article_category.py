# Generated by Django 5.0.1 on 2024-01-26 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_category_options_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='article.category'),
        ),
    ]
