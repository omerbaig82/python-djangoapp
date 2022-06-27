from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'OmerB',
        'title': 'Blog Post 1',
        'content': 'First post here',
        'date_posted': 'June 27, 2022'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post here',
        'date_posted': 'June 26, 2022'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
