from curses.panel import update_panels
from email.policy import default
from venv import create
from django.db import models

class Article(models.Model):
    title = models.CharField(default="", max_length=30)

    text = models.TextField(default="",)

    author = models.CharField(default="", max_length=30)

    created_at = models.DateField(auto_now_add=True) #作成時に日付を自動で入力

    updated_at = models.DateField(auto_now=True) #変更時に変わっていく日付