from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PostCreateForm
from .models import Post

# Create your views here.
@login_required
def post_create(request):
    """Enable users create posts"""
    if request.method != 'POST':
        form = PostCreateForm(data=request.GET)

    else:
        form = PostCreateForm(data=request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('accounts:dashboard')

    return render(request,'posts/create.html',{'form':form})