from rest_framework import generics, status
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema

class APISchema(ManualSchema):
    """
    Manual schema to define the available API endpoints and their HTTP methods.
    """
    def get_schema_operation(self, operation_id):
        api_endpoints = {
            'list': {
                'http_method': 'GET',
                'description': 'List all posts.'
            },
            'create': {
                'http_method': 'POST',
                'description': 'Create a new post.'
            },
            'detail': {
                'http_method': 'GET',
                'description': 'Retrieve details of a specific post.'
            },
            'update': {
                'http_method': 'PUT',
                'description': 'Update a specific post.'
            },
            'partial_update': {
                'http_method': 'PATCH',
                'description': 'Update a subset of fields in a specific post.'
            },
            'delete': {
                'http_method': 'DELETE',
                'description': 'Delete a specific post.'
            }
        }
        # Match operation_id with corresponding endpoint information
        for endpoint, info in api_endpoints.items():
            if operation_id.endswith(endpoint):
                return info
        return None

class HomeView(generics.GenericAPIView):
    schema = APISchema()

    def get(self, request):
        return Response({
            'message': 'Welcome to my API!',
            'endpoints': {
                'posts': {
                    'GET': '/api/',
                    'POST': '/api/',
                    'detail': {
                        'GET': '/api/<int:pk>/',
                        'PUT': '/api/<int:pk>/',
                        'PATCH': '/api/<int:pk>/',
                        'DELETE': '/api/<int:pk>/',
                    }
                }
            }
        })


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