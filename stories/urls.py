from django.urls import path
from . import views

urlpatterns = [
  path('blog/', views.blog_list, name='blog_list'),
  path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
  path('success-stories/', views.success_story_list, name='success_list'),
  path('success-stories/<int:pk>/',views.success_story_detail,name='success_detail'),
]