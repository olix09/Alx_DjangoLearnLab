from django.urls import path
from . import views
# Tag and Search URLs
from django.views.generic import ListView
from .models import Post, Tag

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/posts_by_tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug')
        tag = Tag.objects.get(name=tag_slug)
        return tag.posts.all()
urlpatterns = [
    path('', views.index, name='index'),
path('tags/<str:tag_name>/', views.posts_by_tag, name='posts-by-tag'),
path('search/', views.search_posts, name='search-posts'),
path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts-by-tag'),
    # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),

    # Blog CRUD
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
# Comments
path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    # Comments
    path('posts/<int:post_id>/comments/new/', views.add_comment, name='comment-create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
]




