from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm
# Create your views here.
def index(request):
    """The home page for learning log"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request,'learning_logs/topics.html', context)

@login_required
def topic(request,topic_id):
    """Muestra un tema y todas sus entradas"""
    topic =Topic.objects.get(id = topic_id)
    #Nos aseguramos que un Topic pertenezca al usuario correcto
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries':entries }
    return render(request,'learning_logs/topic.html',context)

@login_required
def new_topic(request):
    """Añadimos un Tema nuevo"""
    
    if request.method != 'POST':
        #Si no hay datos que hacer submit, creamos un formulario en blanco
        form = TopicForm()
    else:
        #Ha habido un post, procesamos los datos
        form =(TopicForm(data = request.POST))
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            form.save()
            return redirect('learning_logs:topics')
    
    #Si llega un formulario vacio o invalido, redirigimos a la pagina de nuevo 
    #topic
    context = {'form': form}
    return render(request,'learning_logs/new_topic.html', context)

@login_required
def new_entry(request,topic_id):
    """Añadir un entry para un topic concreto"""
    topic = Topic.objects.get(id = topic_id)
    
    if request.method != 'POST':
        #No hay datos de submit, creamos un formulario en blanco
        form = EntryForm()
    else:
        #Recibimos un post, procesamos los datos
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit = False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id = topic_id)
    
    #Mostramos un formulario si llega en blanco o incorrecto
    context = {'topic': topic, 'form':form}
    return render(request,'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request,entry_id):
    """Editamos un comentario que ya exista"""
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    
    if request.method != 'POST':
        #No hay datos de submit, precargamos los datos en el formulario
        form = EntryForm(instance=entry)
    else:
        #Recibimos un post, procesamos los datos
        form = EntryForm(instance = entry, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id = topic.id)
    
    #Mostramos un formulario si llega en blanco o incorrecto
    context = {'entry': entry, 'topic': topic, 'form':form}
    return render(request,'learning_logs/edit_entry.html', context)
    