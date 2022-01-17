from django import forms
from .models import inventorymodel
class myform(forms.ModelForm):
    class Meta:
        model = inventorymodel
        fields = "__all__"