from django.contrib import admin
from .models import Note, Subject, VideoLecture, Book, SamplePaper
from django.template.defaultfilters import truncatechars
# Register your models here.
admin.site.site_header = "The CS Guide"
admin.site.index_title = "Admin Dashboard"


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject', 'subject_code', 'semester']
    list_filter = ['semester']
    search_fields = ['subject', 'subject_code']


@admin.register(Note, Book, SamplePaper)
class CommonAdmin(admin.ModelAdmin):
    # ordering = ['subject__semester']
    list_display = ['get_title', 'get_subject', 'get_subject_code', 'get_semester',
                    'created']

    list_filter = ['subject', 'subject__semester', 'created',]
    search_fields = ['title', 'contributer', 'id']

    def get_title(self, obj):
        return truncatechars(obj.title, 40)

    @admin.display(ordering='subject__subject', description="Subject")
    def get_subject(self, obj):
        return truncatechars(obj.subject.subject, 10)

    @admin.display(ordering='subject__subject_code', description="Code")
    def get_subject_code(self, obj):
        return truncatechars(obj.subject.subject_code, 15)

    @admin.display(ordering='subject__semester', description='Semester')
    def get_semester(self, obj):
        return obj.subject.semester


@admin.register(VideoLecture)
class VideoLectureAdmin(admin.ModelAdmin):
    list_display = ['get_link', 'get_subject',
                    'get_subject_code', 'get_semester', 'created']
    list_filter = ['subject', 'subject__semester', 'created',]
    search_fields = ['link', 'contributer', 'id']

    def get_link(self, obj):
        return truncatechars(obj.link, 40)

    @admin.display(ordering='subject__subject', description="Subject")
    def get_subject(self, obj):
        return truncatechars(obj.subject.subject, 10)

    @admin.display(ordering='subject__subject_code', description="Code")
    def get_subject_code(self, obj):
        return truncatechars(obj.subject.subject_code, 15)

    @admin.display(ordering='subject__semester', description='Semester')
    def get_semester(self, obj):
        return obj.subject.semester
