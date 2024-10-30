from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=36)
    slug = models.SlugField()


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField()
    
    class Meta:
        verbose_name = "Article"  # Le nom de l'ensemble des instances
        ordering = ["-date", "-published"]
        
    def __str__(self):
        return self.title  # Le nom de chacune des instances
    
    def numberOfWords(self):
        return len(self.content.split())
    
    def get_absolute_url(self):
        return reverse("post-details", kwargs={"slug":self.slug})
    
    
    @property
    def publish_string(self):
        if self.published:
            return "L'article est publie"
        return "L'article est inaccessible"
    
    
    def save(self, *args, **kwargs):
        
        if not self.slug:
            self.slug = slugify(self.title)
            
        super().save(*args, **kwargs)