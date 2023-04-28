from django.contrib import admin
from .models import Note, Subject
# Register your models here.
admin.site.site_header = "The CS Guide"
admin.site.index_title = "Admin Dashboard"

admin.site.register(Subject)
admin.site.register(Note)
