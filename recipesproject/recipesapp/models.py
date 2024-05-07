from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructions = models.TextField()
    prep_time = models.PositiveIntegerField(help_text='Время приготовления в минутах')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, through='RecipeCategory')
    ingredients = models.TextField()
    image = models.ImageField(upload_to='recipe_images/', null=True, blank=True)

    def __str__(self):
        return self.title


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
