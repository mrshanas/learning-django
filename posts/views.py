from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostCreateForm
from .models import Post
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required

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

@login_required
@require_POST
@ajax_required
def post_like(request):
    """Allow users to like post through AJAX"""
    post_id = request.POST.get('id')
    action = request.POST.get('action')

    if post_id and action:
        try:
            post = Post.objects.get(id=post_id)
            if action == 'like':
                post.users_like.add(request.user)
            else:
                post.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'error'})

@login_required
def post_list(request):
    """Display users post"""
    posts = Post.objects.filter(user=request.user)

    return render(request,'posts/list.html',{'section':'images','posts':posts})