from django.shortcuts import render, redirect
from courseaa.models import courseaa

def homepage(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        new_signin = courseaa(name=name, email=email, password=password)
        new_signin.save()
        #return redirect('/admin/')  # Redirects to the Django admin panel

    return render(request, "project.html")
    
def login(request):
    return render(request,'login.html')