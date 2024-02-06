from django.test import TestCase
from .models import Recipe

class RecipeModelTest(TestCase):

    def setUpTestData():
        Recipe.objects.create(name='Tea', cook_time=5, ingredients='tea leaves, water, sugar', description='Steep tea leaves in boiling water and add sugar.')

    def test_name(self):
        recipe = Recipe.objects.get(id=1)
        recipe_name = recipe._meta.get_field('name').verbose_name
        self.assertEqual(recipe_name, 'name')

    def test_cook_time(self):
        recipe = Recipe.objects.get(id=1)
        recipe_cook_time = recipe._meta.get_field('cook_time').help_text
        self.assertEqual(recipe_cook_time, 'in minutes')
        
    def test_calc_difficulty(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.calc_difficulty(), 'Easy')