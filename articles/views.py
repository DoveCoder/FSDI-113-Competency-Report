from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
    )

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.urls import reverse_lazy
from .models import Article

class ArticleListPage(LoginRequiredMixin,ListView):
    model = Article
    template_name = "news.html"

class ArticleDetailPage(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "news_detail.html"

class ArticleCreatePage(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "news_new.html"
    fields = ["title", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdatePage(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = "news_edit.html"
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeletePage(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "news_delete.html"
    success_url = reverse_lazy("news")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user