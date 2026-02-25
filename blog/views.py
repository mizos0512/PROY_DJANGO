
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from .forms import PostCreateForm
from .models import Post


# Create your views here.

class BlogListView(View):
  def get(self, request, *arg, **kwargs):
      posts = Post.objects.all()
      context ={
        'posts': posts,
      }    
 
      return render(request, 'blog_list.html', context)
    
class BlogCreateView(View):
  def get(self, request, *arg, **kwargs):
      formulario=PostCreateForm()
      context ={
        'Formu':formulario  
      }
      return render(request, 'blog_create.html', context)
    
  def post(self, request, *arg, **kwargs):
    if request.method == 'POST':
      formulario=PostCreateForm(request.POST)
      if formulario.is_valid():
        title = formulario.cleaned_data.get('title')
        content = formulario.cleaned_data.get('content')
        p, created = Post.objects.get_or_create(title=title, content=content)
        p.save()
      return redirect('blog:home')
    titulo='Juan'   
    context ={
         
      }    
    return render(request, 'blog_create.html', context)  
   
  
class BlogDetailView(View):
  def get(self, request, pk, *arg, **kwargs):
    post= get_object_or_404(Post, pk=pk)
    
    context ={
      'post': post,
    }
    return render(request, 'blog_detail.html', context)  