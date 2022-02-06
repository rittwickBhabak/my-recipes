from django.urls import path
from . import views 
from .models import Recipe 

app_name = 'myapp'

urlpatterns = [
    path('', views.AllRecipes.as_view(), name='all-recipe'),
    path('view/<int:pk>', views.ViewRecipe.as_view(), name='view-recipe'),
    path('create/', views.CreateRecipe.as_view(), name='create-recipe'),
    path('update/<int:pk>', views.UpdateRecipe.as_view(), name='update-recipe'),
    path('delete/<int:pk>', views.DeleteRecipe.as_view(), name='delete-recipe'),
]
