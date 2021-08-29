from django import forms
from ckeditor.fields import RichTextFormField

from .models import Doc


class DocForm(forms.ModelForm):
    content = RichTextFormField(config_name='awesome_ckeditor')

    class Meta:
        model = Doc
        fields = ['content']
