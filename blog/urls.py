from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('category/<slug:category_slug>/', views.category_list, name='category_list'),
    path('register/', views.register, name='register'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
