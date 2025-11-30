from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from blog.forms import PostForm
from blog.models import Post
from django.contrib import messages
from django import template
"""
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
"""
register = template.Library()
@register.filter('in_group')
def in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
    
def HomeIndexView(request):
    context = {
        'post_list': Post.objects.all(),
    }
    return render(request,template_name='home.html',context=context,status=200)

def ListagemPostView(request):
 
    context = {
        'post_list': Post.objects.all(),
    }
    return render(request,template_name='listagemPosts.html',context=context,status=200)

def DetalharPostView(request,pk=None):
    context = {
        'post': Post.objects.filter(id=pk).first(),
    }
    return render(request,template_name='detalhapost.html',context=context,status=200)

def InserirPostView(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            try:
                object = form.save()
                messages.success(request, f'Post "{object.titulo}" criado com sucesso!')
            except Exception as e:
                print("Erro %s" % e)
                messages.error(request, f'Erro na inserção do post!')
        else:
            messages.error(request, f'Formulário não válido.')
    else:
        form = PostForm()
    context = {
        'form' : form,
    }
    return render(request,template_name="postInserirEditar.html",context=context,status=200)

def EditarPostView(request,pk):
    message = None
    objForm = get_object_or_404(Post,id=pk)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=objForm)  
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Post editado com sucesso!!!')
            except Exception as e:
                print("Erro %s" % e)
                messages.error(request,"Erro ao inserir Post.")
        else:
            messages.error(request,"Verifique os dados")
    else:
        form = PostForm(instance = objForm)
    context = {
        'form' : form,
    }
    return render(request,template_name="postInserirEditar.html", context = context) 

def ExcluirPostView(request,pk):
    message = None
    objForm = get_object_or_404(Post,id=pk)
    if request.method == 'POST':
        try:
            objForm.delete()
            context = {
                'form' : objForm,
                'post_list' : Post.objects.all(),
            }
            messages.success(request, 'Post excluído com sucesso!!!')
            return redirect('listagemPosts')
        except Exception as e:
            messages.error(request,"Erro ao excluir Post.")
    context = {
        'form' : objForm,
        'post_list' : Post.objects.all(),
    }
    return render(request,template_name="exclusao_post.html", context=context,status=200) 