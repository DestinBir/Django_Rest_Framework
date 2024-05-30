from rest_framework import generics, status
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

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
