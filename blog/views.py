from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse, reverse_lazy
# from django.template.loader import render_to_string

# Create your views here.
# def index(request):
#     return render(request, "blog/index.html")

# def article(request, numeroArticle):
#     if numeroArticle in ["01", "02", "03"]:
#         return render(request, f"blog/article{numeroArticle}.html")
#     return render(request, "blog/articleNotFound.html")

from blog.models import Blog
from blogUdemy.forms import BlogCreateForm

from django.contrib.auth.models import User

#####################
def blog0(request):
    return redirect("home")

#####################

def blog(request):
    r = HttpResponse()
    s = JsonResponse({'2':'Le cul oooooh'})
    r.content = "{'1' : 'Bonjour tout le monde'}"
    #r.status_code = 404
    r['Content-type'] = 'application/json'
    return s


# @login_required   # Restreindre l'acces d'une a un utilisateur connecte

# @user_passes_test(lambda u: u.username == "test")   # lambda: ????  u: l'utilisateur qui va acceder a notre vue
@user_passes_test(lambda u: "Moderateurs" in [group.name for group in u.groups.all()])   # Si la chaine de caractere "Moderateurs" est dans les noms des groupes auxquels appartient l'utilisateur
# Restreindre l'acces a un utilisateur sous certaines conditions
def blog1(request):
    
    '''try:
        blog = Blog.objects.get(pk=2)
    except Blog.DoesNotExist:
        raise Http404("L'article #2 n'existe pas")
    '''
    
    # Tout ceci pourrait etre remplace part:
    blog = get_object_or_404(Blog, pk=1)      # get_object_or_404(la classe, les differents attributs)
     
    return HttpResponse(blog.content)

def blogPosts(request):
    return HttpResponse("Tous les articles du blog")

# def blogPost(request, slug):
#     blog = Blog.objects.get(slug=slug)
#     return render(request, "blog/post.html", {"blogPost":blog})

def blogPost(request):
    blog = get_object_or_404(Blog, pk=1)
    
    return render(request, "blog/post.html", context={"blogPost":blog})

# Structures conditionnelles
def structCondi(request):
    # blogs = Blog.objects.filter(pk__in=[1, 2, 3, 4, 5])
    blogs = Blog.objects.filter(pk__in=[10, 11, 12])
    
    return render(request, "blog/postStrucCondi.html", context={"posts":blogs})

# Les boucles
def boucles(request):
    blogs = Blog.objects.all()
    
    return render(request, "blog/boucles.html", context={"posts":blogs})

# Les URL
def indexUrl(request):
    blog = Blog.objects.all()
    
    return render(request, "blog/index.html", context={"posts":blog})

def postDetails(request, slug):
    post = Blog.objects.get(slug=slug)
    
    return render(request, "blog/posts.html", context={"post":post})


############################ CBV ###############################
from django.views.generic import DetailView, TemplateView, ListView, CreateView, UpdateView, DeleteView


class BlogIndexView(ListView):
    model = Blog  # Recuperer tous les posts
    # queryset = Blog.objects.filter(published=True)  # Recuperer les posts filtres
    template_name = "blog/index.html"
    context_object_name = "posts"
    
class BlogDetailsView(DetailView):
    model = Blog
    template_name = "blog/posts.html"
    context_object_name = "post"
    
class BlogCreateView(CreateView):
    model = Blog
    template_name = "blog/create_post.html"
    # fields = ['title', 'content', 'published', 'author']
    form_class = BlogCreateForm
    # success_url = reverse_lazy("blog-index")  # 1ere maniere de faire
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submitText"] = "Creer"
        context["titleText"] = "Creer un article"
        return context
    
    def get_success_url(self):  # 2e maniere de faire
        return reverse("blog-index")
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        form.instance.published = True
        return super().form_valid(form)
    
class BlogUpdateView(UpdateView):
    model = Blog
    template_name = "blog/create_post.html"
    form_class = BlogCreateForm
    
    def get_success_url(self):
        return reverse("blog-index")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submitText"] = "Modifier"
        context["titleText"] = "Modifier l'article"
        return context
    
class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blog/delete_post.html"
    context_object_name = "post"
    
    def get_success_url(self):
        return reverse("blog-index")