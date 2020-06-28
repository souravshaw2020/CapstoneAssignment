from django.shortcuts import render
from django.views.generic.dates import MonthArchiveView

from hello.models import Article

class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    allow_future = True
# Create your views here.
