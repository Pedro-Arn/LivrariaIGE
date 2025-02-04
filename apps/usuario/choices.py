from django.db import models

class Generos(models.TextChoices):
    MASCULINO = 'M', 'Masculino'
    FEMININO = 'F', 'Feminino'
    OUTRO = 'O', 'Outro'

class Ocupacoes(models.TextChoices):
    ESTUDANTE = 'E', 'Estudante'
    PROFESSOR = 'P', 'Professor'
    OUTRO = 'V', 'Visitante'

class Identificacoes(models.TextChoices):
    MATRICULA = 'M', 'Matrícula'
    CPF = 'C', 'CPF'
