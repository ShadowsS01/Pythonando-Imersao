import uuid
from django.db import models
from django.contrib.auth.models import User


class Paciente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    choices_sexo = (("F", "Feminino"), ("M", "Masculino"))
    nome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=choices_sexo)
    idade = models.IntegerField()
    email = models.EmailField()
    telefone = models.CharField(max_length=19)
    nutri = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class DadosPaciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data = models.DateTimeField()
    peso = models.FloatField()
    altura = models.IntegerField()
    percentual_gordura = models.FloatField()
    percentual_musculo = models.FloatField()
    colesterol_hdl = models.FloatField()
    colesterol_ldl = models.FloatField()
    colesterol_total = models.FloatField()
    trigliceridios = models.FloatField()

    def __str__(self):
        return f"Paciente({self.paciente.nome}, {self.peso})"


class Refeicao(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    horario = models.TimeField()
    carboidratos = models.FloatField()
    proteinas = models.FloatField()
    gorduras = models.FloatField()

    class Meta:
        verbose_name_plural = "Refeições"

    def __str__(self):
        return self.titulo


class Opcao(models.Model):
    refeicao = models.ForeignKey(Refeicao, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to="opcao")
    descricao = models.TextField()

    class Meta:
        verbose_name_plural = "Opções"

    def __str__(self):
        return self.descricao
