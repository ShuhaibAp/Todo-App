from django import forms
from .models import *


class TodoAddForm(forms.ModelForm):
    class Meta:
        model=TodoModel
        exclude=['Status']
        widgets={
        "Title":forms.TextInput(attrs=({"class":"form-control","placeholder":"Interview"})),
        "Description":forms.TextInput(attrs=({"class":"form-control","placeholder":"Interview at 10 o'clock"})),
        "Date":forms.DateInput(attrs=({"class":"form-control","placeholder":"2024-12-02"})),
        "Image":forms.ClearableFileInput(attrs={'class':'form-control '}),
        }

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model=TodoModel
        exclude=['Status']
        widgets={
        "Title":forms.TextInput(attrs=({"class":"form-control mb-2","placeholder":"Interview"})),
        "Description":forms.TextInput(attrs=({"class":"form-control mb-2","placeholder":"Interview at 10 o'clock"})),
        "Date":forms.DateInput(attrs=({"class":"form-control mb-2","placeholder":"2024-12-02"})),
        "Image":forms.ClearableFileInput(attrs={'class':'form-control mb-5'}),
        }