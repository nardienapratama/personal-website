from django.urls import include, path
from django.contrib import admin
from .import views
# from .views import hello_function


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('about/',  views.about, name='about'),
    path('books/',  views.books, name='books'),    
    path('signup/', views.signup, name='signup'),
    path('schedule/', views.schedule, name='schedule'),
    path('deleteEvents/', views.delete_events, name='deleteEvents'),
    path('displayRegisForm/', views.display_regis_form, name='displayRegisForm'),
    path('runForm/', views.run_form, name='runForm'),
    path('emailValidation/', views.email_validation, name='emailValidation'),
    path('auth/', include('social_django.urls', namespace='social')),  # <- Here
]

