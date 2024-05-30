from rest_framework import generics, status
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework import viewsets

class HomeView(generics.GenericAPIView):
    
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
    
class CommentByPost(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['pk'])

    def get_options(self, request, format=None):
        return Response(allowed_methods=['GET'])
    
class RecentPosts(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-pub_date')[:4]
    serializer_class = PostSerializer

    def get_options(self, request, format=None):
        return Response(allowed_methods=['GET'])
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

"""    
from django.contrib.auth import login, authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer

class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({'message': 'Login successful'})
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'})
"""