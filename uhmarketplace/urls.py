from django.urls import path
from . import views

app_name = 'uhmarketplace' # allows using 'uhmarketplace:index' for url and reverse_lazy methods
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('addtextbook/', views.CreateView.as_view(), name='createtextbook'),
    path('updatetextbook/<int:pk>', views.UpdateView.as_view(), name='updatetextbook'),
    path('deletetextbook/<int:pk>', views.DeleteView.as_view(), name='deletetextbook'),
    path('textbook/', views.TextbookView.as_view(), name='textbook'),
    path('dorm/', views.DormView.as_view(), name='dorm'),
    path('classes/', views.ClassesView.as_view(), name='classes'),
    path('foodie/', views.FoodieView.as_view(), name='foodie'),
    path('supplies/', views.SuppliesView.as_view(), name='supplies'),
    path('decorderDate/', views.DecOrderDateView.as_view(), name='decorderDate'),
    path('ascorderDate/', views.AscOrderDateView.as_view(), name='ascorderDate'),
    path('searchtextbook/', views.SearchTextbookView.as_view(), name='searchtextbook'),
    path('myTextbook/', views.FilterCreatedByView.as_view(), name='myTextbook'),
    path('addcomment/', views.CreateCommentView.as_view(), name='createcomment'),
    path('updatecomment/<int:pk>', views.UpdateCommentView.as_view(), name='updatecomment'),
    path('deletecomment/<int:pk>', views.DeleteCommentView.as_view(), name='deletecomment'),
]
