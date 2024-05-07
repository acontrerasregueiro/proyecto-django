from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """Registramos un nuevo usuario"""
    
    if request.method != 'POST':
        #Mostramos un formulario en blanco
        form = UserCreationForm()
    else:
        form = UserCreationForm(data = request.POST)
        
        if form.is_valid():
            new_user = form.save()
            #Loggeamos al usuario y lo redirigimos a la pag principal
            login(request,new_user)
            return redirect('learning_logs:index')
    
    
    context = {'form':form}
    return render(request,'registration/register.html', context)