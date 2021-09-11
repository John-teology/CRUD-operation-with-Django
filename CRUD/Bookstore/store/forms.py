from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *

#creating forms
class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = "__all__"   #"__all__" shortcut para lahat na agad
        
        
  