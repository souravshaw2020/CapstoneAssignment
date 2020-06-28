from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from django.utils import timezone
from django.views.generic.detail import DetailView

from hello.models import Article,ArticleDetail

class ArticleCounterRedirectView(RedirectView):

    permanent = False
    query_string = True
    pattern_name = 'article-detail'

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])
        return super().get_redirect_url(*args, **kwargs)

class ArticleDetail(DetailView):

    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

# Create your views here.
