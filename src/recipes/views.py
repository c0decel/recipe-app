from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Recipe

def home(request):
    return render(request, 'recipes/home.html')

@login_required
def records(request):
    return render(request, 'recipes/records.html')

class ViewAllRecipes(ListView):
    model = Recipe
    template_name = 'recipes/all_recipes.html'

class ViewRecipeDetails(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/details.html'
