from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    description = models.CharField(max_length=350)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name="categories")

    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    content = models.TextField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)