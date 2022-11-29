from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Comment
from .forms import CommentForm

def index(request):
    error = ''
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comments')
        else:
            error = 'Incorrect form'

    form = CommentForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')

def comments(request):
    comments = Comment.objects.order_by('-id')
    return render(request, 'main/comments.html', {'title': 'All Comments', 'comments': comments})

def user(request):
    message = request.GET.get("message", "U can type ur name and message in the link above <br>(use: ?name=urname&message=urmessage)")
    name = request.GET.get("name", "Stranger")
    return HttpResponse(f"<h1>Hello, {name}! {message}!</h1><br><a href='/'><button>Go back</button</a>")
    
