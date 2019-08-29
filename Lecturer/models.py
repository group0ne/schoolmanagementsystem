from django.conf import settings
from django.contrib.auth.models import Group
from django.db import models


class Subject(models.Model):
    LecturerName = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    SubjectTitle = models.CharField(max_length=100)
    SubjectDescription = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.SubjectTitle)


class Assignment(models.Model):
    LecturerName = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    AssignmentTitle = models.CharField(max_length=100)
    Comments = models.CharField(max_length=100)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    SubmissionDate = models.DateTimeField()
    AssignmentUpload = models.FileField(upload_to='documents/%Y/%m/%d/')

    def __str__(self):
        return str(self.AssignmentTitle)


class ViewAssignment(models.Model):
    LecturerName = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    AssignmentTitle = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    Comments = models.CharField(max_length=100)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    AssignmentUpload = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.AssignmentTitle)


class Note(models.Model):
    LecturerName = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    NoteTitle = models.CharField(max_length=100)
    Comments = models.CharField(max_length=100)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    NoteUpload = models.FileField(upload_to='documents/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.NoteTitle)

class Grade(models.Model):
    StudentName = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='student', on_delete=models.CASCADE)
    Assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Comments = models.CharField(max_length=100)
    mark = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.StudentName) + ": " + str(self.Assignment) + "==> Subject:" + str(self.Subject)
