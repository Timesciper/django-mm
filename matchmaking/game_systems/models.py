from django.db import models


class AbstractGameSystem(models.Model):
    name = models.CharField(max_length=1000, verbose_name='Game System Name', unique=True)


class Formula(models.Model):
    game_system = models.ForeignKey(AbstractGameSystem, on_delete=models.CASCADE, verbose_name='System')
