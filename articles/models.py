from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField(max_length=256)
    organization = models.CharField(max_length=128)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


