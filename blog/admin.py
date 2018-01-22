from django.contrib import admin

# Register your models here.

from blog import models


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Post, PostAdmin)