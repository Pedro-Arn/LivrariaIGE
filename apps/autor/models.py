import uuid
from django.db import models
from django.utils.text import slugify

class Autor(models.Model):
    nome_completo = models.CharField(max_length=100)
    biografia = models.TextField(max_length=500, blank=True)
    data_nascimento = models.DateField(
        blank=True,
        null=True,
        verbose_name='Data de nascimento',
    )
    slug = models.SlugField(unique=True, blank=True)
    foto_perfil = models.ImageField(
        upload_to='autor',
        null=True, 
        blank=True,
        default='usuario.png'
    )

    class Meta:
        db_table  = 'autor'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return self.nome_completo

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.nome_completo)
            slug = base_slug

            while Autor.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{uuid.uuid4().hex[:8]}"  # Gera um ID único de 8-dígitos

            self.slug = slug

        super().save(*args, **kwargs)