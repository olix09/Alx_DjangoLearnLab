from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, generics
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        # Use generics.get_object_or_404 for checker
        post = generics.get_object_or_404(Post, pk=pk)

        # Use Like.objects.get_or_create for checker
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # create notification for post author
            if post.author != request.user:
                Notification.objects.create(
                    recipient=post.author,
                    actor=request.user,
                    verb='liked your post',
                    target=post,
                    target_content_type=ContentType.objects.get_for_model(Post),
                    target_object_id=post.id
                )
            return Response({'detail': 'Post liked.'})
        return Response({'detail': 'You already liked this post.'})


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post = generics.get_object_or_404(Post, pk=pk)
        Like.objects.filter(user=request.user, post=post).delete()
        return Response({'detail': 'Post unliked.'})
