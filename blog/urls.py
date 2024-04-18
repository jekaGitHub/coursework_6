from django.urls import path

from blog.apps import BlogConfig
from blog.views import ArticleListView, ArticleDetailView

app_name = BlogConfig.name


urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='list_articles'),
    path('article/view/<int:pk>/', ArticleDetailView.as_view(), name='view_article'),
]