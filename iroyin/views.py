from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.is_true = True
    feature1.detail = 'Our Service is very fast'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.is_true = True
    feature2.detail = 'Our Service is very reliable'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Affordable'
    feature3.is_true = True
    feature3.detail = 'Our Service is very affordable'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Easy to use'
    feature4.is_true = False
    feature4.detail = 'Our Service is easy to use'

    features = [feature1, feature2, feature3, feature4]
    return render(request, 'index.html', {'features': features})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exist')
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist')
                return redirect('register')
            
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request, 'Password does not match')
            return redirect('register')

    else:        
        return render(request, 'register.html')

    def login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user  = user.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Credentials does not match')
                return redirect('login')
        else:        
            return render(request, 'login.html')