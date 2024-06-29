from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView

app_name = BlogConfig.name

urlpatterns = [
    path("blog", cache_page(60)(BlogListView.as_view()), name="blog"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blog-info"),
]
