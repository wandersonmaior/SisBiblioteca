from django.db import models

# Create your models here.

class Livro(models.Model):

    titulo = models.CharField( 
    	max_length=255, 
    	null=False, 
    	blank=False 
    )


    autor = models.CharField(
       max_length=255,
       null=False,
       blank=False
    )
    
    genero = models.CharField(
       max_length=255,
       null=False,
       blank=False
    )

    idioma = models.CharField(
        default="",
        max_length=20,
        null=False,
        blank=False
    )

    ano_public = models.CharField(
    	max_length=4, 
    	null=False, 
    	blank=False 
    )

    """data_criacao = models.DateTimeField(
    	auto_now_add=True,
    	editable=False
    )

    data_alteracao = models.DateTimeField(
    	auto_now=True,
    	editable=False
    )"""
    

    objetos = models.Manager()