from django import forms
from core.models import Users, Sides


class UserForms(forms.ModelForm):

    class Meta:
        model = Users
        fields = '__all__'



class SidesForms(forms.ModelForm):
    title = forms.CharField(label='Title',help_text='Title can contain any letters or numbers, without spaces', widget=forms.TextInput(attrs={'class': 'input-xlarge'}))
    desc = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'input-xlarge'}))


    class Meta:
        model = Sides
        exclude = ('status', )

