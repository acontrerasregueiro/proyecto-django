""" Define los patrones URL para learning logs"""
from django.urls import path
from . import views
app_name ='learning_logs'

urlpatterns = [
    #Home page
    path('',views.index,name = 'index'),
    #Page that shows all topics.
    path('topics/',views.topics, name = 'topics'),
    #Detalle para cada tema
    path('topics:<int:topic_id>/', views.topic,name ='topic'),
    #Página para añadir un nuevo tema
    path('new_topic/', views.new_topic, name ='new_topic'),
    #Página para añadir new entries
    path('new_entry/<int:topic_id>/',views.new_entry, name = 'new_entry'),
    #Página para editar entries
    path('edit_entry/<int:entry_id>/', views.edit_entry,name ='edit_entry'),
]
