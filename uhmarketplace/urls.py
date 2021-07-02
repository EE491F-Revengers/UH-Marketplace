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
    path('classes/', views.CoursesView.as_view(), name='classes'),
    path('foodie/', views.FoodieView.as_view(), name='foodie'),
    path('supplies/', views.SuppliesView.as_view(), name='supplies'),
    path('decorderDate/', views.DecOrderDateView.as_view(), name='decorderDate'),
    path('ascorderDate/', views.AscOrderDateView.as_view(), name='ascorderDate'),
    path('searchtextbook/', views.SearchTextbookView.as_view(), name='searchtextbook'),
    path('myTextbook/', views.FilterCreatedByView.as_view(), name='myTextbook'),
    path('addclasses/', views.CreateCourseView.as_view(), name='createclasses'),
    path('updateclasses/<int:pk>', views.UpdateCourseView.as_view(), name='updateclasses'),
    path('deleteclasses/<int:pk>', views.DeleteCourseView.as_view(), name='deleteclasses'),
    path('decorderclassesDate/', views.DecOrderCourseDateView.as_view(), name='decorderclassesDate'),
    path('ascorderclassesDate/', views.AscOrderCourseDateView.as_view(), name='ascorderclassesDate'),
    path('searchclasses/', views.SearchCourseView.as_view(), name='searchclasses'),
    path('myClasses/', views.FilterCreatedByCoursesView.as_view(), name='myClasses'),
]
