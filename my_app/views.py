from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Authors
from .models import Articles
from .forms import PostForm 
# Create your views here.

def testView(request):
    #out = Authors.objects.get(pk=1)
    # out = Authors.viewAllArticless()
    html = "<html><body><h1>Данные: Ok</h1></body></html" #% out
    return HttpResponse(html)

def post_list(request):
    articles = Articles.objects.order_by('date')
    return render(request, 'my_app/post_list.html',{'articles':articles})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})