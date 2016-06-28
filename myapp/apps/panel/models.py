from django.db import models

class Panel(models.Model):
    panel_nombre=models.CharField(max_length=120) 
    panel_descripcion=models.TextField()
    panel_data_inicio=models.DateField(auto_now_add=True)
    concluido=models.BooleanField(verbose_name='Concluido', default=False)
    #proyecto = models.ForeignKey(proyecto, related_name='tareas')
    
    def __str__(self):                              
        return self.panel_nombre


