from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('',views.index, name = 'index'),
    path('details/<int:blog_id>',views.details, name = 'details'),
]
