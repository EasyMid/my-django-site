from django import forms
from .models import Articles

class PostForm(forms.ModelForm): 
    class Meta:
        model = Articles 
        fields = ('id_author','title','text',)