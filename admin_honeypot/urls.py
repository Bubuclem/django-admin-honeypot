'''
Urls for the admin_honeypot app.
'''
from django.urls import path, re_path

from admin_honeypot import views

app_name = 'admin_honeypot'
urlpatterns = [
    path('login/', views.AdminHoneypot.as_view(), name='login'),
    re_path(r'^.*$', views.AdminHoneypot.as_view(), name='index'),
]
