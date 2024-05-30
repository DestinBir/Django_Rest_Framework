from rest_framework import generics, status
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from django.contrib.auth.models import User
from rest_framework import viewsets

class PostAutoSchema(AutoSchema):
    pass

class CommentAutoSchema(AutoSchema):
    pass

class HomeView(generics.GenericAPIView):
    
    schemas = [PostAutoSchema(), CommentAutoSchema()]  

    def get(self, request):
        return Response({
            'message': 'Welcome to my API!',
            'endpoints': {
                'posts': {
                    'GET': '/api/posts',
                    'POST': '/api/posts',
                    'detail': {
                        'GET': '/api/post/<int:pk>/',
                        'PUT': '/api/post/<int:pk>/',
                        'PATCH': '/api/post/<int:pk>/',
                        'DELETE': '/api/post/<int:pk>/',
                    }
                },
                'comments': {
                    'GET': '/api/comments',
                    'POST': '/api/comments',
                    'detail': {
                        'GET': '/api/comment/<int:pk>/',
                        'PUT': '/api/comment/<int:pk>/',
                        'PATCH': '/api/comment/<int:pk>/',
                        'DELETE': '/api/comment/<int:pk>/',
                    }
                }
            }
        })

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_options(self, request, format=None):
        return Response(allowed_methods=['GET', 'POST', 'OPTIONS'])

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_options(self, request, pk, format=None):
        return Response(allowed_methods=['GET', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'])


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_options(self, request, format=None):
        return Response(allowed_methods=['GET', 'POST', 'OPTIONS'])
    
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_options(self, request, pk, format=None):
        return Response(allowed_methods=['GET', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'])
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer