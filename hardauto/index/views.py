from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.apps import AppConfig

# this 'class Post' is taking the model from the 'hardblog' which is located as 'name' hardblog/apps.py file.
# It is then used within the index view to show the blog post list.
class Post(AppConfig):
    name = 'hardblog'

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'hardblog/post_list.html', {'posts': posts})

