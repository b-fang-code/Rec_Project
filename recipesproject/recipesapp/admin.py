from django.contrib import admin
from .models import Recipe, Category, RecipeCategory


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author')
    list_filter = ('category', 'author')
    search_fields = ('title', 'category', 'author')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class RecipeCategoryAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'category')
    list_filter = ('recipe', 'category')
    search_fields = ('recipe', 'category')




admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(RecipeCategory)
