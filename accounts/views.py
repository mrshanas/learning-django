from django.shortcuts import redirect, render
# from django.http import HttpResponse
# from django.contrib.auth import authenticate,login
# from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,UserEditForm,ProfileEditForm
from .models import Profile
from django.contrib import messages

# Create your views here.
# superuser
# username: shanas
# password:postgram789

# --user 2--
# username:nassibu
# password:nassibu123

# --user 3--
# username:mteua
# password:mteua123

@login_required
def dashboard(request):
    """Typical home view"""
    return render(request,'accounts/dashboard.html',{'section':'dashboard'})

def register(request):
    """Register new users to the app"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(data=request.POST)

        if user_form.is_valid():
            # create a new user but dont save yet to db
            new_user = user_form.save(commit=False)

            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # creates an empty profile for each user registered
            Profile.objects.create(user=new_user)

            return render(request,'accounts/register_done.html',{'new_user':new_user})

    else:
        user_form = UserRegistrationForm()

    return render(request,'accounts/register.html',{'user_form':user_form})

@login_required
def edit(request):
    """Allow users to edit their profile details"""
    if request.method == 'POST':
        # inorder to prepopulate the input fields with
        # previous objects user instance parameter
        # in the forms instances
        user_form = UserEditForm(instance=request.user,data=request.POST)

        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)

        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(request,'Profile edited successfully')

        else:
            messages.error(request,'Error in updating your profile')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request,'accounts/edit.html',{'user_form':user_form,'profile_form':profile_form})



# def user_login(request):
#     """Authenticating users and starting a session"""
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
        
#         if form.is_valid():
#             clean_data = form.cleaned_data
#             user = authenticate(request,username=clean_data['username'],password=clean_data['password'])

#             if user is not None:
#                 if user.is_active:
#                     login(request,user)
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('disabled account')

#             else:
#                 return HttpResponse('Invalid login')

#     else:
#         form = LoginForm()

#     return render(request,'accounts/login.html',{'form':form})

