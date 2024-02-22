from django.test import TestCase
from .models import Recipe

class RecipeModelTest(TestCase):

    def setUpTestData():
        Recipe.objects.create(name='Tea', cook_time=5, ingredients='tea leaves, water, sugar', description='Steep tea leaves in boiling water and add sugar.', steps='Boil water,, Add tea leaves,, Add sugar')

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

    def test_steps(self):
        recipe = Recipe.objects.get(id=1)
        recipe_steps = recipe._meta.get_field('steps').help_text
        self.assertEqual(recipe_steps, 'Seperate each step with two commas')

    def test_steps_to_list(self):
        recipe = Recipe.objects.get(id=1)
        expected_steps = ['1. Boil water', '2. Add tea leaves', '3. Add sugar']
        self.assertEqual(recipe.steps_to_list(), expected_steps)