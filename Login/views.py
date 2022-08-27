from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        nombre = request.POST['first_name']
        apellido = request.POST['last_name']
        password = request.POST['password']

        user = User.objects.create_user(username, email, password)
        user.first_name = nombre
        user.last_name = apellido
        user.save()

    return render(request, 'registration/register.html')
