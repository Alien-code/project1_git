from django.shortcuts import render
from .models import Post

# Create your views here.
# for home page request\

user1 = {'name': 'Md Ashiouzzaman Real', 'age': 22, 'university': 'UIU', 'dept': 'CSE'}


def home(request):
    all_post = Post.objects.all()
    return render(request, 'index.html', {'all_post_list': all_post})


# task - all_post_list
def allPost(request):
    new_all_post = Post.objects.all()
    return render(request, 'all_post_list_task.html', {'new_post_list': new_all_post})

# for blog-tutorial
def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'post-list.html', {'post_list': post_list})

# Single post with Query-get()
def single_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    print(post)
    return render(request, 'single_post.html', {'post': post})

def contact(request):
    return render(request, 'contact.html')
