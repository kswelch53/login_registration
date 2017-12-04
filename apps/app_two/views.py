from django.shortcuts import render, HttpResponse, redirect
from .models import User

def index(request):
    print("This is index function in app_two views.py")
# this prevents users from getting to success page by typing url /success
# to get to success page they must be logged in (in session)

    if 'user_id' not in request.session:
        return redirect('users:index')
    else:
        print("User id is:", request.session['user_id'])
        print("User name is:", request.session['user_first_name'])

# users who are logged in are directed to the success page:
    return render(request, 'app_two/success.html')
