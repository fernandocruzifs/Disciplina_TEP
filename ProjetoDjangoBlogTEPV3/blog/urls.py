
from django.urls import path
from blog.views import (BlogCreateView, BlogListView,BlogDetailView, BlogUpdateView, BlogDeleteView, 
                DetalharPostView, EditarPostView, ExcluirPostView,HomeIndexView, InserirPostView, ListagemPostView)

urlpatterns = [
    path('', HomeIndexView,name='home'),
    path('listagemPosts',ListagemPostView,name='listagemPosts'),
    path('detalhapost/<int:pk>/', DetalharPostView,name='detalhapost'),
    path('post/novo/', InserirPostView,name='novo_post'),
    path('post/<int:pk>/edicao/', EditarPostView,name='edicao_post'),
    path('post/<int:pk>', ExcluirPostView,name='exclusao_post'),
]


"""
    path('', BlogListView.as_view(),name='home'),
    path('detalhapost/<int:pk>/', BlogDetailView.as_view(),name='detalhapost'),
    path('post/novo/', BlogCreateView.as_view(),name='novo_post'),
    path('post/<int:pk>/edicao/', BlogUpdateView.as_view(),name='edicao_post'),
    path('post/<int:pk>', BlogDeleteView.as_view(),name='exclusao_post'),
    """