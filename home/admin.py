from django.contrib import admin
from .models import Tutorial
from tinymce.widgets import TinyMCE
from django.db import models

class TutorialAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

admin.site.register(Tutorial,TutorialAdmin)