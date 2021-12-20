from django.urls import path
from .views import (
    ArticleListPage,
    ArticleDetailPage,
    ArticleCreatePage,
    ArticleUpdatePage,
    ArticleDeletePage
    )

urlpatterns = [
    path('', ArticleListPage.as_view(), name='news'),
    path('<int:pk>/', ArticleDetailPage.as_view(), name='news_detail'),
    path('create/', ArticleCreatePage.as_view(), name='news_new'),
    path('edit/<int:pk>', ArticleUpdatePage.as_view(), name="news_edit"),
    path('delete/<int:pk>', ArticleDeletePage.as_view(), name="news_delete")
]