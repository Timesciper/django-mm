from django.db import models


class AbstractGameSystem(models.Model):
    name = models.CharField(max_length=1000, verbose_name='Game System Name', unique=True)


class Formula(models.Model):
    game_system = models.ForeignKey(AbstractGameSystem, on_delete=models.CASCADE, verbose_name='System')
    # eval? nah eval is bad
    # we have to make a parser. good thing - we have only mmr_higher mmr_lower and +-*/^ and ()
    rule_string = models.CharField(max_length=1000, verbose_name='Rule for processing mmr after game')


