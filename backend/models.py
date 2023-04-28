from django.db import models
import uuid
# Create your models here.


class Subject(models.Model):
    SEMESTER_CHOICE = [
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
        (6, 'VI'),
    ]
    semester = models.IntegerField(
        choices=SEMESTER_CHOICE)
    subject = models.CharField(max_length=200)
    subject_code = models.CharField(max_length=50, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return f'{self.subject_code}-{self.subject}'


class Note(models.Model):
    subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=500)
    notes_file = models.FileField(
        upload_to="Notes/")
    created = models.DateField(auto_now_add=True, editable=False)
    contributer = models.CharField(max_length=300, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.title


class VideoLecture(models.Model):
    subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, null=True, blank=True)
    link = models.CharField(max_length=1000)
    created = models.DateField(auto_now_add=True, editable=False)
    contributer = models.CharField(max_length=300, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.link


class Book(models.Model):
    subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=500)
    book_file = models.FileField(
        upload_to="Books/")
    created = models.DateField(auto_now_add=True, editable=False)
    contributer = models.CharField(max_length=300, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.title


class SamplePaper(models.Model):
    subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=500)
    paper_file = models.FileField(
        upload_to="Sample_Papers/")
    created = models.DateField(auto_now_add=True, editable=False)
    contributer = models.CharField(max_length=300, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.title
