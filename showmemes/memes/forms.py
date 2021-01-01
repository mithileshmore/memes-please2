from django import forms  
from memes.models import UserLogin


class UserLoginForm(forms.ModelForm):  
    class Meta:  
        model = UserLogin  
        fields = "__all__"  
