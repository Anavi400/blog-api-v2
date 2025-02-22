from rest_framework.permissions import permissions
from rest_framework import generics
from .models import Post

class PostList(generic.views.RetrieveUpdateDestroyAPIView)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permission.IsAdminUser)

class PostDetail(generic.views.RetrieveUpdateDestroyAPIView)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
