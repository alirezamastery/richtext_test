from ckeditor.fields import RichTextField
from django.db import models


class Doc(models.Model):
    content = RichTextField(config_name='awesome_ckeditor')
