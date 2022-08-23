from django.db import models


# Create your models here.
class Orientador(models.Model):

    primeiro_nome = models.CharField(max_length=40)
    ultimo_nome = models.CharField(max_length=40)
    curriculo_link = models.URLField()

    def __str__(self):
        return self.primeiro_nome


class Autor(models.Model):
    primeiro_nome = models.CharField(max_length=40)
    ultimo_nome = models.CharField(max_length=40)
    foto = models.ImageField(upload_to='fotos', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.primeiro_nome


class Curso(models.Model):
    cursos = (
        ('Bacharelado', 'Bacharelado'),
        ('Licenciatura', 'Licenciatura'),
        ('Tecnólogo', 'Tecnólogo'),
    )

    nome = models.CharField(max_length=50)
    modalidade = models.CharField(max_length=30, choices=cursos, blank=False, null=False)

    def __str__(self):
        return self.nome


class TCC(models.Model):
    titulo = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    ano_documento = models.IntegerField()
    resumo = models.TextField()
    arquivo = models.FileField(upload_to='tccs')
    palavras_chave = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    orientador = models.ForeignKey(Orientador, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
