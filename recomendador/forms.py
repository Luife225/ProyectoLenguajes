from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    genero_preferido = forms.ChoiceField(choices=Profile._meta.get_field('genero_preferido').choices)
    plataforma_preferida = forms.ChoiceField(choices=Profile._meta.get_field('plataforma_preferida').choices)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('genero_preferido', 'plataforma_preferida',)
