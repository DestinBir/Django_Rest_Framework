from django.urls import path
from .views import PostList, PostDetail, CommentDetail, CommentList, HomeView

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('post/<int:pk>/', PostDetail.as_view()),
    path('comments/', CommentList.as_view()),
    path('comment/<int:pk>/', CommentDetail.as_view()),
    path('', HomeView.as_view())
]
