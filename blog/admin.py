from django.contrib import admin

# Register your models here.
from blog.models import Blog


# admin.site.register(Blog)   # 1ere facon de faire pour enregistrer un modele dans l'interface d'administration

# 2e facon de faire
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (    # pour inscrire les champs a afficher dans l'espace d'admin
        "title",
        "slug",
        "author",
        "published",
        "date",
        "numberOfWords",
    )
    
    list_editable = ("title", "published", )
    
    list_display_links = ("slug",)
    
    search_fields = ("title", "slug", )
    
    list_filter = ("published", "author", )
    
    autocomplete_fields = ("author", )
    
    # filter_horizontal = ("", )  # Pour les champs ManyToMany
    
    list_per_page = 3
    
    empty_value_display = "Inconnu"  # La valeur a inscrire pour les champs vides
