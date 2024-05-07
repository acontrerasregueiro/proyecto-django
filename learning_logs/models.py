from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """A topic the user is learning about"""
    
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    #Añadimos un campo owner, que establecerá una relación con la clave foránea
    #del model User
    owner = models.ForeignKey(User, on_delete= models.CASCADE)
    
    def __str__(self):
        """Return a string representation of the model"""
        return self.text

class Entry(models.Model):
    """Cosas especificas que hemos aprendido sobre ese Topic"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Devuelve un string representando la entrada"""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}"
        
