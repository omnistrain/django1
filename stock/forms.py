
from django import forms
from stock.models import Groupe, Formation

class ContactForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)

class GroupeForm(forms.ModelForm):
    class Meta:
        model= Groupe
        #fields = '__all__'
        exclude = ('active', 'page')

class FormationForm(forms.ModelForm):
    class Meta:
        model= Formation
        fields = '__all__'
        #exclude = ('active', 'page')