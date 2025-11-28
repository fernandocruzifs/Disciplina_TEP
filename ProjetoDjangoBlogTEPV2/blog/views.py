from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from blog.models import Post
from django.contrib import messages
from django import template

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'detalhapost.html'
    
class BlogCreateView(CreateView):
    model = Post
    template_name = 'novo_post.html'
    fields = ["titulo","texto","autor"]
    
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'edicao_post.html'
    fields = ["titulo","texto"]
    
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'exclusao_post.html'
    success_url = reverse_lazy("home")