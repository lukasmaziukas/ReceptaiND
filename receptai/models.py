from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Receptas(models.Model):
    title = models.CharField('Pavadinimas', max_length=100, help_text='Koks receptuko vardelis?')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Receptas'
        verbose_name_plural = 'Receptai'

    def __str__(self):
        return self.title


class Produktas(models.Model):
    text = models.CharField("Produktas", max_length=300, help_text='Įrašyk produktą')
    isCompleted = models.BooleanField()
    list = models.ForeignKey(Receptas, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Produktas'
        verbose_name_plural = 'Produktai'

    def __str__(self):
        return self.text