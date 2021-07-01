from django.views import generic
from django.urls import reverse_lazy
from .models import CommentSection, Textbook, Uhmarketplace
from django.utils import timezone
from .filters import TextbookFilter
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls.base import set_urlconf


class IndexView(generic.ListView):
    template_name = 'uhmarketplace/index.html'
    model = Uhmarketplace

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

class DormView(generic.ListView):
    template_name = 'uhmarketplace/dorm.html'
    model = Uhmarketplace

class ClassesView(generic.ListView):
    template_name = 'uhmarketplace/classes.html'
    model = Uhmarketplace

class FoodieView(generic.ListView):
    template_name = 'uhmarketplace/foodie.html'
    model = Uhmarketplace

class SuppliesView(generic.ListView):
    template_name = 'uhmarketplace/supplies.html'
    model = Uhmarketplace

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
        """Return all the blogs."""
        me = User.objects.get(username=self.request.user)
        return Textbook.objects.filter(created_by=me)
  
class CreateCommentView(generic.edit.CreateView):
    template_name = 'uhmarketplace/createtextbook.html'
    model = CommentSection
    fields = ['content', 'created_by']
    success_url = reverse_lazy('uhmarketplace:textbook') # more robust than hardcoding to /uhmarketplace/; directs user to index view after creating a Uhmarketplace

class UpdateCommentView(generic.edit.UpdateView):
    template_name = 'uhmarketplace/updatetextbook.html'
    model = CommentSection
    fields = ['content']
    success_url = reverse_lazy('uhmarketplace:textbook')

class DeleteCommentView(generic.edit.DeleteView):
    template_name = 'uhmarketplace/deletetextbook.html' # override default of uhmarketplace/uhmarketplace_confirm_delete.html
    model = CommentSection
    success_url = reverse_lazy('uhmarketplace:textbook')