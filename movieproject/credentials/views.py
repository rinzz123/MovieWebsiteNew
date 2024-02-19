from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            user_id = request.user.id
            # return render(request,'home.html')
            # return redirect('movieapp:allMovieCat', user_id=user_id)
            request.session['user_id'] = user_id
            return redirect('movieapp:allMovieCat')
            #return render(request,'home.html')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('credentials:login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('credentials:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                return redirect('credentials:register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()
                messages.info(request, "User created")

        else:
            messages.info(request, "Password not matched")
            return redirect('credentials:register')
        return redirect('credentials:login')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
