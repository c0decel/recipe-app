# Generated by Django 4.2.9 on 2024-02-08 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='no_img.png', upload_to='media/recipe_images'),
        ),
    ]
