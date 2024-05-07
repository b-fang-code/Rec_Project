from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import RecipeForm, SingUpForm
from .models import Recipe, Category
import random


def home(request):
    recipes = Recipe.objects.all()
    random_recipes = random.sample(list(recipes), min(len(recipes), 5))
    return render(request, 'recipesapp/home.html', {'random_recipes': random_recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipesapp/recipe_detail.html', {'recipe': recipe})


def get_all_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipesapp/all_recipes.html', {'recipes': recipes})


def signup(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SingUpForm()
    return render(request, 'recipesapp/signup.html', {'form': form})


@login_required
def recipe_add(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()
            return redirect('recipes:recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm()
    return render(request, 'recipesapp/recipe_form.html', {'form': form})


@login_required
def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user != recipe.author:
        return redirect('recipe_detail', recipe_id=recipe.id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipesapp/recipe_form.html', {'form': form})
