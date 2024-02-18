from django.urls import path
from .views import home, ViewAllRecipes, ViewRecipeDetails

app_name = 'recipes'

urlpatterns = [
    path('', home),
    path('all_recipes/', ViewAllRecipes.as_view(), name='all_recipes'),
    path('all_recipes/<int:pk>', ViewRecipeDetails.as_view(), name='details')
]