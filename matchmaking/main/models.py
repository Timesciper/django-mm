from django.db import models
from game_systems.models import AbstractGameSystem
from matchmaking.settings import DEFAULT_MMR_STARTPOINT, DEFAULT_MAX_MMR_DIFF


class AbstractPlayer(models.Model):
    # no login or email here - we can extend it with custom player class later
    # abstract player can have multiple mmr's which depend on system


    def get_mmr(self, game_system=''):
        game = AbstractGameSystem.objects.get(name=game_system)
        return MMR.objects.filter(game_system=game).get(player=self)


class MMR(models.Model):
    # we can define system or leave it, but it always should point to a player
    player = models.ForeignKey(AbstractPlayer, on_delete=models.CASCADE, verbose_name='Owner-player')
    # maybe default system - like default?
    game_system = models.ForeignKey(AbstractGameSystem, on_delete=models.CASCADE, verbose_name='Game system related to mmr')
    value = models.IntegerField(default=DEFAULT_MMR_STARTPOINT, verbose_name='MMR value')


class Matchmaking(models.Model):
    # here we should define baseline for finding opponent
    max_diff = models.IntegerField(default=DEFAULT_MAX_MMR_DIFF, verbose_name='Default max MMR difference between players')
    # mm can vary based on system
    game_system = models.ForeignKey(AbstractGameSystem, on_delete=models.CASCADE, verbose_name='Game system ')

