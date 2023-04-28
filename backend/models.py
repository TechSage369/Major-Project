from django.db import models
import uuid
# Create your models here.


class Subject(models.Model):
    SEMISTER_CHOICE = [
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
        (6, 'VI'),
    ]
    semister = models.IntegerField(
        choices=SEMISTER_CHOICE)
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
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.title


class Video_Lecture(models.Model):
    subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, null=True, blank=True)
    link = models.CharField(max_length=1000)
    created = models.DateField(auto_now_add=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.link