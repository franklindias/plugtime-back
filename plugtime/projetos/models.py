from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField("Título", max_length=255)
    description = models.CharField("Título", max_length=255)
    estimated_time = models.PositiveSmallIntegerField(verbose_name="Tempo estimado")
    time_value = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title

class Event(models.Model):
    start = models.DateTimeField(verbose_name="Início")
    end = models.DateTimeField(verbose_name="Fim")
    duration = models.DurationField(verbose_name="Duração")
    description = models.CharField(blank=False, max_length=100, verbose_name="Descrição")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Projeto")
    participant = models.ForeignKey("Participant", on_delete=models.CASCADE, verbose_name="Participante ")

    def __str__(self):
        return self.description


class Participant(models.Model):
    role = models.CharField(verbose_name="Função", max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Projeto")

    def __str__(self):
        return self.role
