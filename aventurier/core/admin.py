from django.contrib import admin

from core.models import Language, LanguageFramework, Level, VocabItem

# Register your models here.
admin.site.register(Language)
admin.site.register(LanguageFramework)
admin.site.register(Level)
admin.site.register(VocabItem)
