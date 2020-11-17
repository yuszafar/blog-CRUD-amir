from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from blog.models import Post, Comment

from django.contrib.auth import get_user_model

User = get_user_model()


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Post
        fields = ['title', 'text', 'author']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'author']
        read_only_fields = ['author']


class CurrentPostDefault:
    requires_context = True

    def __call__(self, serializer_field):
        return Post.objects.get(id=serializer_field.context['request'].parser_context['kwargs']['post_id'])

    def __repr__(self):
        return '%s()' % self.__class__.__name__


class CommentCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=CurrentUserDefault())
    post = serializers.HiddenField(default=CurrentPostDefault())

    class Meta:
        model = Comment
        fields = ['text', 'author', 'post']




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'post']
        read_only_fields = ['author', 'post']
