from django.shortcuts import render, get_object_or_404, redirect
from commublog.models import Post, Comment
from datetime import timezone
from django.shortcuts import render
from commublog.models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from commublog.forms import PostForm, CommentForm
from django.urls import reverse_lazy

# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
class PostDetailView(DetailView):
    model = Post    

class CreatePostView(LoginRequiredMixin, CreateView):
    login_required = True
    redirect_field_name = 'commublog/post_detail.html'
    form_class = PostForm
    model = Post
    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_required = True
    redirect_field_name = 'commublog/post_detail.html'
    form_class = PostForm
    model = Post
    
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_required = True
    redirect_field_name = 'commublog/post_list.html'
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')
    


    #########################################
    #########################################
@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            
            return redirect('post_detail', pk=post.pk)
        
    else:
        form = CommentForm()
        
    return render(request, 'commublog/comment_form.html', {'form':form})