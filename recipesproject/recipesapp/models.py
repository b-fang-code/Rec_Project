from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название рецепта')
    description = models.TextField(verbose_name='Описание рецепта')
    instructions = models.TextField(verbose_name='Инструкция приготовления')
    prep_time = models.PositiveIntegerField(verbose_name='Время приготовления в минутах')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, through='RecipeCategory', verbose_name='Категория')
    ingredients = models.TextField(verbose_name='Ингредиенты')
    image = models.ImageField(upload_to='recipe_images/', null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.title


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
