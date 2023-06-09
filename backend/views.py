from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, user_passes_test

# from django.contrib.auth.forms import AuthenticationForm
# from django.views.generic import View
# from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.contrib import messages
from .models import Subject, Note, VideoLecture, Book, SamplePaper
from django.db.models import Q
from .contextProcessor import *

# Create your views here.


def index(request):
    return render(request, 'pages/landing-page/landingpage.html')

def aboutUs(request):
    return render(request, 'pages/about_us.html')

def contact(request):
    return render(request, 'pages/contact_us.html')

def isLoggedIn(user):
    return not user.is_authenticated


@user_passes_test(isLoggedIn, login_url="index")
@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in',
                             extra_tags="success")
            return redirect('/admin/')
        else:
            messages.error(
                request, 'invalid username or password!', extra_tags='warning')
    return render(request, 'pages/admin_login.html')


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.error(
        request, 'Successfully Logged Out!', extra_tags='primary')
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'pages/admin_dashboard.html')


def notes_table(request):
    title = "Notes"
    context = getSubjectTableData()
    context['title'] = title
    return render(request, "pages/notes_table.html", context)


def notes(request, id, *args, **kwargs):
    data = Note.objects.filter(subject=id)
    subject = Subject.objects.get(id=id)
    context = {
        "data": data,
        "subject": subject,
    }
    return render(request, 'pages/notes.html', context)


def video_lectures_table(request):
    title = "Video Lectures"
    context = getSubjectTableData()
    context['title'] = title
    return render(request, "pages/video_lectures_table.html", context)


def video_lectures(request, id, *args, **kwargs):
    data = VideoLecture.objects.filter(subject=id)
    subject = Subject.objects.get(id=id)
    return render(request, "pages/video_lectures.html", context={'data': data, 'subject': subject})


def course_books_table(request):
    title = "Course Book"
    context = getSubjectTableData()
    context['title'] = (title)
    return render(request, "pages/course_books_table.html", context)


def course_books(request, id, *args, **kwargs):
    data = Book.objects.filter(subject=id)
    subject = Subject.objects.get(id=id)
    return render(request, "pages/course_books.html", context={'data': data, 'subject': subject})


def sample_papers_table(request):
    title = "Sample Paper"
    context = getSubjectTableData()
    context['title'] = (title)
    return render(request, "pages/sample_papers_table.html", context)


def sample_papers(request, id, *args, **kwargs):
    data = SamplePaper.objects.filter(subject=id)
    subject = Subject.objects.get(id=id)
    return render(request, "pages/sample_papers.html", context={'data': data, 'subject': subject})
