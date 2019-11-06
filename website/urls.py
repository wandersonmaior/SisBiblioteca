from website.views import IndexTemplateView, LivroListView, LivroUpdateView, LivroCreateView, \
    LivroDeleteView

from django.urls import path

app_name = 'website'

urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name="index"),

    # GET /livro/cadastrar
    path('livro/cadastrar', LivroCreateView.as_view(), name="cadastra_livro"),

    # GET /livros
    path('livros/', LivroListView.as_view(), name="lista_livros"),

    # GET/POST /livro/{pk}
    path('livro/<pk>', LivroUpdateView.as_view(), name="atualiza_livro"),

    # GET/POST /livros/excluir/{pk}
    path('livro/excluir/<pk>', LivroDeleteView.as_view(), name="deleta_livro"),
]