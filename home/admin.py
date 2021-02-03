from django.contrib import admin
from django.db import models
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    class Meta:
        model=Post

    class Media:
        js = ("home/js/rich.js",)
