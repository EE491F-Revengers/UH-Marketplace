from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class Uhmarketplace(models.Model):
    message = models.CharField(max_length=80)

class Textbook(models.Model):
    book_title = models.CharField(max_length=80)
    book_author = models.CharField(max_length=80)
    course = models.CharField(max_length=80)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.book_title

class Courses(models.Model):
    course_title = models.CharField(max_length=80)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.course_title