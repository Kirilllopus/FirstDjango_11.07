from django.forms import ModelForm, Textarea, TextInput
from MainApp.models import Snippet


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ['name', 'lang', 'code']
        labels = {'name': '', 'lang': '', 'code': ''}
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Название снипета'}),
            'code': Textarea(attrs={'placeholder': 'Код снипета'}),
        }