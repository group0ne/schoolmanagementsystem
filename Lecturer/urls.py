from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth import views
from django.views.generic import TemplateView
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from Lecturer.models import Note,Assignment
from Lecturer.views import *
urlpatterns = [
                url(r'^note_view/$', notes, name='notes'),
                url(r'^grade_view/$', grades, name='grades'),
                url(r'^assignment_view/$', assignment, name='assignments'),
            ]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)