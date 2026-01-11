from django.urls import path
from . import views
from .views import PostListView
from .views import PostListView, PostDetailView, PostDeleteView, PostUpdateView
from .views import PostListAPIView
from .views import PostCreateView
from .views import PostUpdateView


urlpatterns = [
    path('', PostListView.as_view(), name='timeline'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('api/posts/', PostListAPIView.as_view()), 
    path('api/weather/', views.weather, name='weather'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit')
]
