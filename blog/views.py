from rest_framework import permissions
from rest_framework.generics import (GenericAPIView, CreateAPIView, ListAPIView, RetrieveAPIView )
from rest_framework.mixins import (RetrieveModelMixin, DestroyModelMixin,
                                   UpdateModelMixin)

from blog.models import (Post, Comment)
from blog.permissions import (IsOwnerOrReadOnly,)
from blog.serializers import (PostCreateSerializer, CommentCreateSerializer, PostSerializer, CommentSerializer)


class PostCreate(CreateAPIView):
    serializer_class = PostCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostDetail(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_url_kwarg = 'post_id'
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentCreate(CreateAPIView):
    serializer_class = CommentCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentList(ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['post_id'])


class CommentDetail(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'comment_id'
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['post_id'])

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)