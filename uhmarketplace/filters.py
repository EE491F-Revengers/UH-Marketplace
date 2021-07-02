import django_filters
from .models import Textbook, Courses


class TextbookFilter(django_filters.FilterSet):
    class Meta:
        model = Textbook
        fields = {
            'book_title': ['icontains'],
            'book_author': ['icontains'],
            'content': ['icontains'],
            'course': ['icontains'],
        }

class CoursesFilter(django_filters.FilterSet):
    class Meta:
        model = Courses
        fields = {
            'course_title': ['icontains'],
            'content': ['icontains'],
        }