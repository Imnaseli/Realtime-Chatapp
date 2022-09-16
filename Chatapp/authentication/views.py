from django.http import HttpResponse
from django.shortcuts import render  ,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url = 'signin')
def home(request):
    return render(request , "authentication/index.html")



def signup(request):
    
        #Get data from form 
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        
        #Validation
        if User.objects.filter(username = username):
            messages.error(request , "Username already exists!")
            return redirect ('signup')

        if User.objects.filter(email = email):
            messages.error(request , 'Email address already exists!')
            return redirect ('signup')
        
        if len(username) > 12:
            messages.error(request , 'Username must be under 12 characters')
            return redirect ('signup')
        
        if pass1 != pass2 :
            messages.error(request , 'Passwords dont match bro.')
            return redirect ('signup')
        
        if not username.isalnum():
            messages.error(request , 'Username is only Alpha-Numeric gee')
            return redirect ('signup')      
        
        if len(pass1) < 10:
            messages.error(request , 'Password should be more than 10 charaters!')
            return redirect ('signup')      
                   
        
        #Create user object (eith the user module imported)
        user = User.objects.create_user(username , email , pass1)
        user.first_name = firstname
        user.last_name = lastname

        #Save in the database
        user.save()
        
        #Send a messsage telling the user he has successfully created an account
        messages.success(request , 'Your account has been succesfully made , Welcome to the Iluuminati.')
        return redirect ('signin')
        
    return render (request , 'authentication/signup.html')



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(request , username = username  , password = pass1)
        
        if user is not None:
            login(request , user)
            return redirect( 'home'  )
        else:
            messages.error(request , 'Wrong credentials.')
            return redirect('signin')
        
    return render (request , 'authentication/signin.html')


@login_required(login_url = 'signin')
def signout(request):
    logout(request)
    # messages.success(request , 'Logged out successfully.')
    return redirect('home')