from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from sisbiblioteca.models import Livro
from website.forms import InsereLivroForm

# Create your views here.

# PÁGINA PRINCIPAL
# ----------------------------------------------

class IndexTemplateView(TemplateView):
    template_name = "website/index.html"


# LISTA DE LIVROS
# ----------------------------------------------

class LivroListView(ListView):
    template_name = "website/lista.html"
    model = Livro
    context_object_name = "livros"


# CADASTRAMENTO DE LIVROS
# ----------------------------------------------

class LivroCreateView(CreateView):
    template_name = "website/cria.html"
    model = Livro
    form_class = InsereLivroForm
    success_url = reverse_lazy("website:lista_livros")


# ATUALIZAÇÃO DE LIVROS
# ----------------------------------------------

class LivroUpdateView(UpdateView):
    template_name = "website/atualiza.html"
    model = Livro
    fields = '__all__'
    context_object_name = 'livro'
    success_url = reverse_lazy("website:lista_livros")


# EXCLUSÃO DE LIVROS
# ----------------------------------------------

class LivroDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Livro
    context_object_name = 'livro'
    success_url = reverse_lazy("website:lista_livros")
