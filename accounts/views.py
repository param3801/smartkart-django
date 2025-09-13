from django.shortcuts import render, redirect,HttpResponse
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


# Create your views here.
def register(request):
    if request.method == 'POST':
        # Handle form submission and user registration logic here
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            username = email.split('@')[0]
            password = form.cleaned_data.get('password')
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            user.phone_number = phone_number
            user.save()

            #user activation and email verification logic can be added here
            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'
            message = render_to_string('accounts/account_verification_email.html',{
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            # messages.success(request, 'Your account has been registered successfully!,  Please check your email to activate your account.')
            # return redirect('register')
            return redirect('/accounts/login/?command=verification&email='+email)
            

    else:
      form  = RegistrationForm()
    context = {
            'form': form,
        }
            

    return render(request, 'accounts/register.html', context)  


def login_view(request):
    if request.method == 'POST':
        # Handle login logic here
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Authenticate user (you can use Django's built-in authentication system)
        user = authenticate(email = email, password=password)
        # If authentication is successful, log the user in and redirect to a dashboard or home page
        if user is not None: 
            login(request, user)
            messages.success(request,"You are now logged in.")
            return redirect('home')  # Replace 'dashboard' with your desired redirect URL
        else:
        # If authentication fails, display an error message
            messages.error(request,"Invalid login credentials   Please try again.")
            return redirect('login')
        
    return render(request, 'accounts/login.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.success(request,"You are logged out.")
    return redirect('login')


def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')
    
    
def forget_password(request):
    if request.method=='POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)


            #reset password email
            current_site = get_current_site(request)
            mail_subject = 'Reset your password'
            message = render_to_string('accounts/reset_password_email.html',{
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })
            to_email = email
            send_email  = EmailMessage(mail_subject, message,to=[to_email])
            send_email.send()

            messages.success(request,'reset password link as been sent to you email, please check your mail')
            return redirect('login')
        else:
            messages.error(request,'Account does not exists!')
            return redirect('forget_password')


    return render(request,'accounts/forget_password.html')



def resepassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request,'reset your password')
        return redirect('resetpassword')
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('loign')
    

def resetpassword(request):
    if request.method=='POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password'] 
        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request,'Password reset successfully')
            return redirect('login')
        else:
            messages.error(request,'Password does not match!')
            return redirect('resetpassword')

    return render(request, 'accounts/resetpassword.html')
     



