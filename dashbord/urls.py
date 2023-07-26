from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('conversion/', views.conversion, name='conversion'),
    path('dictionary/', views.dictionary, name='dictionary'),
    path('homework/', views.homework, name='homework'),
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="registration/logout.html"), name='logout'),
    path('notes/detail/', views.notes_detail, name='notes-detail'),
    path('notes/', views.notes, name='notes'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('todo/', views.todo, name='todo'),
    path('wiki/', views.wiki, name='wiki'),
    path('youtube/', views.youtube, name='youtube'),
    path('delete/<int:pk>', views.delete_note, name='delete-note'),
    path('note/detail/<int:pk>', views.note_detail.as_view(), name='note-detail'),
    path('update_homework/<int:pk>', views.update_homework, name='update-homework'),
    path('delete_homework/<int:pk>', views.delete_homework, name='delete-homework'),
    path('update_todo/<int:pk>', views.update_todo, name='update-todo'),
    path('delete_todo/<int:pk>', views.delete_todo, name='delete-todo'),

]
