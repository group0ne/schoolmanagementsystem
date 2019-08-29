from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from Lecturer.models import Note, Assignment, Grade


@login_required()
def notes(request):
    qs = Note.objects.all()
    context = dict()
    context['notes'] = qs
    return render(request, 'notes.html', context)

def assignment(request):
    qs = Assignment.objects.all()
    context = dict()
    context['assignments'] = qs
    return render(request, 'assignment.html', context)

def grades(request):
    qs = Grade.objects.all()
    context = dict()
    context['grades'] = qs
    return render(request, 'grades.html', context)