# Generated by Django 4.2.9 on 2024-02-22 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_alter_recipe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='steps',
            field=models.TextField(default=1, help_text='Seperate each step with two commas', max_length=1000),
            preserve_default=False,
        ),
    ]
