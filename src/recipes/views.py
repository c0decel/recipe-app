from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe

# Create your views here.

def home(request):
    return render(request, 'recipes/home.html')

class ViewAllRecipes(ListView):
    model = Recipe
    template_name = 'recipes/all_recipes.html'

class ViewRecipeDetails(DetailView):
    model = Recipe
    template_name = 'recipes/details.html'
