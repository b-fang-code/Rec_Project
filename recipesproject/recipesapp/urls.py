from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='recipesapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('recipe/add/', views.recipe_add, name='recipe_add'),
    path('recipe/<int:recipe_id>/edit/', views.recipe_edit, name='recipe_edit'),
    path('recipes/', views.get_all_recipes, name='all_recipes'),
]
