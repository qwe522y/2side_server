from django.contrib import admin
from . import models


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'status', 'added')
    list_filter = ('status', )


admin.site.register(models.Document, DocumentAdmin)
