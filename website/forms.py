from sisbiblioteca.models import Livro
from django import forms


# FORMULÁRIO DE INCLUSÃO DE LIVROS
# -------------------------------------------

class InsereLivroForm(forms.ModelForm):

    class Meta:
        # Modelo base
        model = Livro

        # Campos que estarão no form
        fields = [
            'titulo',
            'autor',
            'genero',
            'idioma',
            'ano_public',
            #'data_criacao',
            #'data_alteracao'
        ]
