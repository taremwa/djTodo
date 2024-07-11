from django.shortcuts import render
from django.contrib import messages
from validate_email import validate_email

# Create your views here.
def register(request):
    if request.method == "POST":
        context = {'has_error': False}
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')


        if len(password) < 6:
            messages.add_message(request,messages.ERROR,'Password should atleast exceed 6 characters')
            context['has_error'] = True
        
        if password != password2:
            messages.add_message(request,messages.ERROR,'Password mismatch')
            context['has_error'] = True



    return render(request, 'authentication/register.html')

def login(request):
    return render(request, 'authentication/login.html')