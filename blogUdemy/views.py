from datetime import datetime
from typing import Any
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# from django.views import View
from django.views.generic import TemplateView

from blogUdemy.forms import SignupForm, BlogForm


def index(request):  
    return render(request, "index.html", context={"prenom": "Martial", "date": datetime.today()})


def home(request):
    return HttpResponse("<h1>L'accueil de mon site !</h1>")

def signup(request):
    
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("Merci de vous etre inscrit au site")
    else:
        form = SignupForm()
    
    return render(request, "accounts/signup.html", context={"form":form})


def blogForm(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            # blog = form.save(commit=False)
            # blog.published = True
            # blog.save()
            form.save()
            return HttpResponseRedirect(request.path)
    else:
        init_values = {}
        if request.user.is_authenticated:
            init_values["author"] = request.user
        init_values["date"] = datetime.today()
        form = BlogForm(initial=init_values)
    
    return render(request, "blog/post.html", context={"form":form})


# class HomeView(View):
#     title = "Default"
    
#     def get(self, request):
#         return HttpResponse(f"<h1>{ self.title } !</h1><a href='cbv/blog/'>Le Blog</a>")

class HomeView(TemplateView):
    template_name = "index.html"
    title = "Default"
    date = datetime(1999, 8, 31)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context["date"] = self.date
        return context

def cbvHome(request):
    return HttpResponse("<h1>Accueil du site !</h1><a href='cbv/blog/'>Le Blog</a>")