from django.db import models
from django.utils.text import slugify

from apps.autor.models import Autor
from apps.curso.models import Materias


class Editora(models.Model):
    nome = models.CharField(
        max_length=100,
        null=False,
        unique=True,
    )

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'editora'


class Link(models.Model):
    site = models.CharField(
        'Site de compra', 
        max_length=100,
        blank=False,
        null=False,
    )
    link = models.TextField(
        'Link do site',
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.site

    class Meta:
        db_table = 'Link'


class Livros(models.Model):
    titulo = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        unique=False,
    )
    descricao = models.TextField(max_length=500, blank=True)
    ano_publicacao = models.DateField(
        verbose_name='Data de publicação',
        blank=True,
        null=True
    )
    editora = models.ForeignKey(
        Editora,
        on_delete=models.CASCADE,
        blank=False,
        null=True
    )
    links = models.ManyToManyField(
        Link,
        blank=True,
        verbose_name='Onde comprar',
    )
    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        blank=False,
        null=True,
        related_name='livros',
    )
    materia = models.ManyToManyField(
        Materias,
        related_name='materia_livro',
        verbose_name='Materias associadas',
    )
    slug = models.SlugField(unique=True, blank=True)
    capa = models.ImageField(
        upload_to='livros', 
        null=True, 
        blank=True,
        default='capa_base.png'
    )

    class Meta:
        db_table = 'livros'
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['titulo',]

    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)


class Comentario(models.Model):
    from apps.usuario.models import Usuario

    from apps.usuario.models import Usuario

    livro = models.ForeignKey(
        Livros,
        on_delete=models.CASCADE,
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
    )
    corpo = models.TextField()
    postado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['postado_em',]

    def __str__(self):
        return f'{self.livro.titulo} por {self.usuario.first_name}'
