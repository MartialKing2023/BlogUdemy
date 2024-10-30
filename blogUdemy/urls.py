"""
URL configuration for blogUdemy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from datetime import datetime
from django.contrib import admin
from django.urls import include, path
from django.views.defaults import server_error
from .views import home, index, signup, blogForm, HomeView
from blog.views import blog0, blog, blog1, blogPosts, blogPost, structCondi, boucles, postDetails, indexUrl


urlpatterns = [
    # path('', index),
    # path('blog/', include("blog.urls")),
    # path('blog/', blog, name="blog"),
    # path('', index, name="home"),
    path('blog0/', blog0, name="blog-index"),
    path('blog1/', blog1, name="blog1"),
    # path('blog/', blogPosts, name="blog-index"),
    # path('blog/<str:slug>/', blogPost, name="blog-post"),
    path('blog/', blogPost, name="blog-post"),
    path('admin/', admin.site.urls),
    path('cul/', server_error),
    path('struct-condi/', structCondi, name="struct-condi"),
    path('boucles/', boucles, name="boucles"),
    # path('', indexUrl, name="home"),
    path('blog/<str:slug>/', postDetails, name="post-details"),
    
    
    path('', home, name="home"),
    path('signup/', signup, name="signup"),
    
    path('article/', blogForm, name="blog-article"),
    
    path('cbv/', HomeView.as_view(title="Accueil du site", date=datetime.today()), name="cbv-index"),
    path('cbv/about/', HomeView.as_view(title="A propos", date=datetime.today()), name="cbv-about"),
    
    path('blog-cbv/', include('blog.urls')),
]
