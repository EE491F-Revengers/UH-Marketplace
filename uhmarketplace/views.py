from django.views import generic
from django.urls import reverse_lazy
from .models import Textbook, Uhmarketplace, Courses
from django.utils import timezone
from .filters import TextbookFilter, CoursesFilter
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls.base import set_urlconf

#####################################
#            Home Page              #
#####################################

class IndexView(generic.ListView):
    template_name = 'uhmarketplace/index.html'
    model = Uhmarketplace

#####################################
#        Underdeveloped pages       #
#####################################

class DormView(generic.ListView):
    template_name = 'uhmarketplace/dorm.html'
    model = Uhmarketplace

class FoodieView(generic.ListView):
    template_name = 'uhmarketplace/foodie.html'
    model = Uhmarketplace

class SuppliesView(generic.ListView):
    template_name = 'uhmarketplace/supplies.html'
    model = Uhmarketplace

#####################################
#         Textbooks tab views       #
#####################################

class CreateView(generic.edit.CreateView):
    template_name = 'uhmarketplace/createtextbook.html'
    model = Textbook
    fields = ['book_title','book_author','course','content', 'created_by']
    success_url = reverse_lazy('uhmarketplace:textbook') # more robust than hardcoding to /uhmarketplace/; directs user to index view after creating a Uhmarketplace

class UpdateView(generic.edit.UpdateView):
    template_name = 'uhmarketplace/updatetextbook.html'
    model = Textbook
    fields = ['book_title','book_author','course','content']
    success_url = reverse_lazy('uhmarketplace:textbook')

class DeleteView(generic.edit.DeleteView):
    template_name = 'uhmarketplace/deletetextbook.html' # override default of uhmarketplace/uhmarketplace_confirm_delete.html
    model = Textbook
    success_url = reverse_lazy('uhmarketplace:textbook')

class TextbookView(generic.ListView):
    template_name = 'uhmarketplace/textbook.html'
    context_object_name = 'textbook_list'

    def get_queryset(self):
        """Return the all uhmarketplace."""
        return Textbook.objects.all()

class DecOrderDateView(generic.ListView): #decending order (newest to oldest)
    template_name = 'uhmarketplace/decorderdate.html'
    context_object_name = 'textbook_list'

    def get_queryset(self):
        """Return all the textbooks."""
        return Textbook.objects.order_by('-published_date')

class AscOrderDateView(generic.ListView): #ascending order (oldest to newest)
    template_name = 'uhmarketplace/ascorderdate.html'
    context_object_name = 'textbook_list'

    def get_queryset(self):
        """Return all the textbooks."""
        return Textbook.objects.order_by(('published_date'))

class SearchTextbookView(generic.ListView):
    template_name = 'uhmarketplace/searchtextbook.html'
    context_object_name = 'textbook_list'

    def get_queryset(self):
        """Return all the textbooks."""
        return Textbook.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TextbookFilter(self.request.GET, queryset=self.get_queryset())
        return context

class FilterCreatedByView(generic.ListView):
    template_name = 'uhmarketplace/createdBy.html'
    context_object_name = 'textbook_list'

    def get_queryset(self):
        """Return all the textbooks."""
        me = User.objects.get(username=self.request.user)
        return Textbook.objects.filter(created_by=me) 

#####################################
#         Classes tab views         #
#####################################

class CreateCourseView(generic.edit.CreateView):
    template_name = 'uhmarketplace/createclasses.html'
    model = Courses
    fields = ['course_title', 'content', 'created_by']
    success_url = reverse_lazy('uhmarketplace:classes') # more robust than hardcoding to /uhmarketplace/; directs user to index view after creating a Uhmarketplace

class UpdateCourseView(generic.edit.UpdateView):
    template_name = 'uhmarketplace/updateclasses.html'
    model = Courses
    fields = ['course_title','content']
    success_url = reverse_lazy('uhmarketplace:classes')

class DeleteCourseView(generic.edit.DeleteView):
    template_name = 'uhmarketplace/deleteclasses.html' # override default of uhmarketplace/uhmarketplace_confirm_delete.html
    model = Courses
    success_url = reverse_lazy('uhmarketplace:classes')

class CoursesView(generic.ListView):
    template_name = 'uhmarketplace/classes.html'
    context_object_name = 'courses_list'

    def get_queryset(self):
        """Return the all courses."""
        return Courses.objects.all()

class DecOrderCourseDateView(generic.ListView): #decending order (newest to oldest)
    template_name = 'uhmarketplace/decorderclassesdate.html'
    context_object_name = 'courses_list'

    def get_queryset(self):
        """Return all the Courses."""
        return Courses.objects.order_by('-published_date')

class AscOrderCourseDateView(generic.ListView): #ascending order (oldest to newest)
    template_name = 'uhmarketplace/ascorderclassesdate.html'
    context_object_name = 'courses_list'

    def get_queryset(self):
        """Return all the Courses."""
        return Courses.objects.order_by(('published_date'))

class SearchCourseView(generic.ListView):
    template_name = 'uhmarketplace/searchclasses.html'
    context_object_name = 'courses_list'

    def get_queryset(self):
        """Return all the Courses."""
        return Courses.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CoursesFilter(self.request.GET, queryset=self.get_queryset())
        return context

class FilterCreatedByCoursesView(generic.ListView):
    template_name = 'uhmarketplace/createdByClasses.html'
    context_object_name = 'courses_list'

    def get_queryset(self):
        """Return all the courses."""
        me = User.objects.get(username=self.request.user)
        return Courses.objects.filter(created_by=me)

