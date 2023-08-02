from django.forms import ModelForm
from .models import producto

class productForm(ModelForm):
    class Meta:
        model = producto
        fields = ['title', 'description']
