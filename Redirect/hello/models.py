from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.CharField(max_length=10)
    def __str__(self):
        return self.title

class ArticleDetail(models.Model):
    headline = models.CharField(max_length=100)
    content =models.CharField(max_length=20)
    def __str__(self):
        return self.headline

    

# Create your models here.
