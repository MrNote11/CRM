from django.shortcuts import redirect, render
import pathlib
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

this_dir = pathlib.Path(__file__).resolve().parent
def home(request):
    home_html = "home.html"
    
    # Check to see if the user is logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Welcome Back")
            return redirect('home')
        else:
            messages.error(request, "There was an error logging in. Please try again.")
            return redirect('home')
    
    return render(request, home_html)


def logout_users(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')
