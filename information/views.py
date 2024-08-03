from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib import messages
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from django.views.generic import CreateView

from .tokens import account_activation_token
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
from .tokens import account_activation_token
# Create your views here.

def activation_sent_view(request):
    return render(request, 'information/activation_sent.html')

def activate(request, uidb64, token):
    print("hello")
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true
        user.is_active = True
        # set signup_confirmation true
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('/information/')
    else:
        return render(request, 'information/activation_invalid.html')

def register(request):
    # return HttpResponse('<h1>Register</h1>')
    # return render(request, 'information/register.html')
    print("entered")
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            # user.is_active = False
            # user.is_staff = True
            # user.is_admin = True
            # user.is_superuser = True
            user.save()

            group = form.cleaned_data.get("group")
            profile = user.profile
            profile.group = group
            profile.save()

            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            message = render_to_string('information/activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # method will generate a hash value with user related data
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('information/activation_sent')
    else:
        form = UserRegisterForm()
    return render(request, 'information/register.html', {'form': form})

def contact(request):
    return render(request, 'information/contact.html')

# def Login(request):
#     print("FFF")
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password1')
#         print(username)
#         user = authenticate(request, username=username, password=password)
#         print(user)
#         if user is not None:
#             print("user authenticated")
#             profile = Profile.objects.get(user=user)
#             if profile.group == 'institute':
#                 print("i am institute")
#                 return redirect('institute')
#             elif profile.group == 'student':
#                 print("i am student")
#                 return redirect('student')
#             form = login(request, user)
#             # messages.success(request, "Welcome")
#             # print("Hello")
#             # return redirect('/signup/')
#         else:
#             messages.info(request, "Account exists, please login!!")
#     form = AuthenticationForm()
#     return render(request, 'home/homepage.html', {'form': form})


@login_required
def studprofile(request):
    return render(request, 'information/studprofile.html')


@login_required
def instprofile(request):
    return render(request, 'information/instprofile.html')

@login_required
def update_profile(request):
    u = User.objects.get(username = request.user.username)
    u.profile.first_name = request.POST.get('first_name')
    u.profile.last_name = request.POST.get('last_name')
    u.profile.save()
    return render(request, 'information/instprofile.html')

def update_pass(request):
    print('haiiiiiiii')
    u = User.objects.get(username = request.user.username)
    pas1 = request.POST.get('password1')
    pas2 = request.POST.get('password2')
    if pas1 == pas2:
        u.set_password(pas1)
        u.save()
    else:
        error = 'passwords do not match'
    return render(request, 'information/instprofile.html')