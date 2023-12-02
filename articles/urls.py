from django.urls import path

from .views import (ArticleListView, ArticleDetailView, ArticleUpdateView)

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('/<int:pk>/edit', ArticleUpdateView.as_view(), name='article_edit'),
]