
from django.urls import path
from blog.views import BlogCreateView, BlogDeleteView, BlogDetailView, BlogListView, BlogUpdateView


urlpatterns = [
    path('', BlogListView.as_view(),name='home'),
    path('detalhapost/<int:pk>/', BlogDetailView.as_view(),name='detalhapost'),
    path('post/novo/', BlogCreateView.as_view(),name='novo_post'),
    path('post/<int:pk>/edicao/', BlogUpdateView.as_view(),name='edicao_post'),
    path('post/<int:pk>', BlogDeleteView.as_view(),name='exclusao_post'),
]