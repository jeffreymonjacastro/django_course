from django.contrib import admin
from . import models

class NotesAdmin(admin.ModelAdmin):
  list_display = ('title', 'created')

admin.site.register(models.Notes, NotesAdmin)