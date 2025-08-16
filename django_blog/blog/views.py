from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import RegistrationForm, PostForm

# Registration view
def register_view(request):
    if request.method == 'POST':  # <--- POST and method
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()      # <--- save() called
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'blog/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':  # POST handling
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('index')

# Profile view
@login_required
def profile_view(request):
    if request.method == 'POST':       # POST handling
        request.user.email = request.POST.get('email', request.user.email)
        request.user.save()             # save() called
    return render(request, 'blog/profile.html', {'user': request.user})

# Index view
def index(request):
    return render(request, 'blog/index.html')

# CRUD class-based views (keep as before)
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
