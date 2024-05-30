from rest_framework import generics, status
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_options(self, request, format=None):
        # Define allowed methods for this endpoint
        return Response(allowed_methods=['GET', 'POST', 'OPTIONS'])

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_options(self, request, pk, format=None):
        # Define allowed methods for this endpoint
        return Response(allowed_methods=['GET', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'])


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_options(self, request, format=None):
        # Define allowed methods for this endpoint
        return Response(allowed_methods=['GET', 'POST', 'OPTIONS'])
    
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_options(self, request, pk, format=None):
        # Define allowed methods for this endpoint
        return Response(allowed_methods=['GET', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'])