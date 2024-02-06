from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    cook_time = models.FloatField(help_text='in minutes')
    ingredients = models.CharField(max_length=120)
    description = models.TextField(max_length=200)

    def calc_difficulty(self):
        ingredients = self.ingredients.split(', ')
        if self.cook_time < 10 and len(ingredients) < 4:
            self.difficulty = 'Easy'
        elif self.cook_time < 10 and len(ingredients) >= 4:
            self.difficulty = 'Medium'
        elif self.cook_time >= 10 and len(ingredients) < 4:
            self.difficulty = 'Intermediate'
        else:
            self.difficulty = 'Hard'
        return self.difficulty

    def __str__(self):
        return str(self.name)
