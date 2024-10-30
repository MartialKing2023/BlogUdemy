from django.urls import path
from blog.views import BlogIndexView, BlogDetailsView, BlogCreateView, BlogUpdateView, BlogDeleteView


urlpatterns = [
    path('', BlogIndexView.as_view(), name="blog-index"),
    path('create/', BlogCreateView.as_view(), name="blog-create"),
    path('post/<str:slug>/', BlogDetailsView.as_view(), name="blog-details"),
    path('post/<str:slug>/edit/', BlogUpdateView.as_view(), name="blog-edit"),
    path('post/<str:slug>/delete/', BlogDeleteView.as_view(), name="blog-delete"),
]
