from django.shortcuts import render, redirect
from django.contrib import messages
from validate_email import validate_email
from .models import User

# Create your views here.
def register(request):
    if request.method == "POST":
        context = {'has_error': False, 'data': request.POST}
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')


        if len(password) < 6:
            messages.add_message(request,messages.ERROR,
                                 'Password should atleast exceed 6 characters')
            context['has_error'] = True
        
        if password != password2:
            messages.add_message(request,messages.ERROR,
                                 'Password mismatch')
            context['has_error'] = True

        if not validate_email(email):
            messages.add_message(request,messages.ERROR,
                                 'Enter a valid email address')
            context['has_error'] = True

        if not username:
            messages.add_message(request,messages.ERROR,
                                 'Username is required')
            context['has_error'] = True

        if User.objects.filter(username=username).exists():
            messages.add_message(request,messages.ERROR,
                                 'Username is already taken, Choose another')
            context['has_error'] = True

        if User.objects.filter(email=email).exists():
            messages.add_message(request,messages.ERROR,
                                 'Email is already taken, Choose another')
            context['has_error'] = True

        if context['has_error']:
            return render(request, 'authentication/register.html', context)
        

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()


        messages.add_message(request, messages.SUCCESS,'Account Sucessfully created!, you can login')
        return redirect('login')

    return render(request, 'authentication/register.html')

def login(request):
    return render(request, 'authentication/login.html')