from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, TemplateView, UpdateView
from .models import Recipe

class AllRecipes(ListView):
    model = Recipe 

class CreateRecipe(CreateView):
    fields = "__all__"
    model = Recipe 

class UpdateRecipe(UpdateView):
    fields = "__all__"
    model = Recipe 

class DeleteRecipe(DeleteView):
    model = Recipe 
    success_url = reverse_lazy('myapp:all-recipe')

class ViewRecipe(DetailView):
    model = Recipe 