from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostCreateForm
from .models import Post

# Create your views here.
@login_required
def post_create(request):
    """Enable users create posts"""
    if request.method != 'POST':
        form = PostCreateForm()

    else:
        form = PostCreateForm(data=request.POST,files=request.FILES)
        print(form.is_valid())

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            print(new_form.user)
            new_form.save()
            return redirect('accounts:dashboard')

    return render(request,'posts/create.html',{'form':form})

@login_required
def post_detail(request,id,slug):
    """Show the post detail to users"""
    post = get_object_or_404(Post,id=id,slug=slug)
    return render(request,'posts/detail.html',{'section':'images','post':post})