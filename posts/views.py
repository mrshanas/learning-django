from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostCreateForm
from .models import Post
from accounts.models import Contact
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from django.contrib.auth.models import User

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

@login_required
def user_list(request):
    """Display all the users"""
    users = User.objects.filter(is_active=True)
    return render(request,'posts/user/list.html',{'section':'people','users':users})

@login_required
def user_detail(request,username):
    """Display user details"""
    user = get_object_or_404(User,username=username,is_active=True)

    # posts = Post.objects.filter(user=request.user)

    return render(request,'posts/user/detail.html',{'section':'people','user':user})

@ajax_required
@require_POST
@login_required
def user_follow(request):
    """Allow users to follow each other"""
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(user_from=request.user,user_to=user)
            else:
                Contact.objects.filter(user_from=request.user,user_to=user).delete()
            return JsonResponse({'status':'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status':'error'})
    return JsonResponse({'status':'error'})