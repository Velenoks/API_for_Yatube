from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly, IsAuthenticated)

from .models import Post, Comment, Group, Follow
from .serializers import (
    PostSerializer, CommentSerializer,
    GroupSerializer, FollowSerializer)
from .permission import IsAuthorOrReadOnly, IsAuthorAndFollow


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related(
        'author',
        'group',
    )
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('group',)

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly,)

    def get_queryset(self):
        id_post = self.kwargs['id_post']
        comments = Comment.objects.select_related(
            'author',
        ).filter(post=id_post)
        return comments

    def perform_create(self, serializer, *args, **kwargs):
        id_post = self.kwargs['id_post']
        post = get_object_or_404(Post, id=id_post)
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated, IsAuthorAndFollow,)
    filter_backends = (SearchFilter,)
    search_fields = ('user__username',)

    def get_queryset(self):
        queryset = Follow.objects.filter(following=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
