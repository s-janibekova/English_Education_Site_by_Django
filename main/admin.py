from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Tutorial,TutorialSeries,TutorialCategory

# Register your models here.

class TutorialAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["tutorial_title", "tutorial_published"]}),
        ("URL", {'fields': ["tutorial_slug"]}),
        ("Series", {'fields': ["tutorial_series"]}),
        ("Content", {"fields": ["tutorial_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }


admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial,TutorialAdmin)
'''
Set fieldsets to control the layout of admin “add” and 
“change” pages.

fieldsets is a list of two-tuples, in which 
each two-tuple represents a <fieldset> on the admin form page.
 (A <fieldset> is a “section” of the form.)

The two-tuples are in the format (name, field_options), 
where name is a string representing the title of the fieldset 
and field_options is a dictionary of information about the 
fieldset, including a list of fields to be displayed in it.
'''