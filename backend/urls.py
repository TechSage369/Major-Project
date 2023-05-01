from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #     path('admin/login/', views.loginUser, name='login'),
    path('logout', views.logoutUser, name="logout"),
    path('about-us',views.aboutUs, name = 'about-us'),
    path('contact',views.contact, name = 'contact'),
    path('notes-table', views.notes_table, name='notes-table'),
    path('notes-table/notes/<str:subject>/<slug:id>',
         views.notes, name="notes"),
    path('video-lectures', views.video_lectures_table,
         name='video-lectures-table'),
    path('video-lectures/videos/<str:subject>/<slug:id>',
         views.video_lectures, name="video-lectures"),

    path('course-books', views.course_books_table, name='course-books-table'),
    path('course-books/books/<str:subject>/<slug:id>',
         views.course_books, name="course-books"),

    path('sample-papers', views.sample_papers_table, name='sample-papers-table'),
    path('sample-papers/papers/<str:subject>/<slug:id>', views.sample_papers,
         name='sample-papers'),

    path('admindashboard', views.dashboard, name="admin-dashboard"),
]
