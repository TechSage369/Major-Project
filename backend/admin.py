from django.contrib import admin
from .models import Note, Subject, Video_Lecture, Book, SamplePaper
# Register your models here.
admin.site.site_header = "The CS Guide"
admin.site.index_title = "Admin Dashboard"

admin.site.register(Subject)
admin.site.register(Note)
admin.site.register(Video_Lecture)
admin.site.register(Book)
admin.site.register(SamplePaper)
