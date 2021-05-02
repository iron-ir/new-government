from django import forms
from django_json_widget.widgets import JSONEditorWidget
from .models import Candidate


class YourForm(forms.ModelForm):
    class Meta:
        model = Candidate

        fields = ('json_t',)

        widgets = {
            'json_t': JSONEditorWidget
        }