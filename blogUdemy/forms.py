from django import forms
from blog.models import Blog


JOBS = (
    ("python", "Developpeur python"),
    ("javascript", "Developpeur javascript"),
    ("csharp", "Developpeur C#"),
)

class SignupForm(forms.Form):
    pseudo = forms.CharField(max_length=8, required = False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput)
    job = forms.ChoiceField(choices=JOBS)
    cgu_accept = forms.BooleanField(initial=True)
    
    def clean_pseudo(self):
        pseudo = self.cleaned_data.get("pseudo")
        if "$" in pseudo:
            raise forms.ValidationError("Le pseudo ne peut pas contenir de $.")
        return pseudo
    
    
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            "title",
            "date",
            "author",
            "published",
            "category",
            "description",
        ]
        labels = {
            "title": "Titre",
            "category": "Categorie"
        }
        widgets = {"date": forms.SelectDateWidget(years=range(1990, 2040))}
        
        
class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            "title",
            "description",
            "content",
        ]
        labels = {
            "title": "Titre",
            "content": "Contenu",
            "published": "Publie",
        }