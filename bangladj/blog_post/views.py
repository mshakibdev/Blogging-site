from django.shortcuts import render
from .models import post

def home(request):
    all_post = post.objects.all()
    return render(request, "index.html", { 'all_post_list' : all_post })

def post_list(request):
    post_list = post.objects.all()
    return render(request, 'post_list.html', {'post_list': post_list})

def single_post(request,post_id):
    posts =post.objects.get(pk= post_id)
    print(posts)
    print(posts.title)
    return render(request, 'single_post.html', {'posts' : posts})

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')