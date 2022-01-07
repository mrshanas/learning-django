from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm

# Create your views here.
@login_required
def create_image(request):
    """Create Images"""
    if request.method =='POST':
        form = ImageCreateForm(data=request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request,"Successfully Added an Image")

            # redirect to
            return redirect(new_item.get_absolute_url())

    else:
        # this means the user bookmarked via GET method
        form = ImageCreateForm(data=request.GET)

    return render(request,'posts/image/create.html',{'form':form,'section':'images'})
