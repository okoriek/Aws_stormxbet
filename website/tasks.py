from __future__ import absolute_import, unicode_literals
from .models import GameRound, LotteryRound
from django.utils import timezone
from celery import shared_task



# Celery for game
@shared_task
def Create():
    one = GameRound.objects.last()
    rounds = int(one.week) + 1
    GameRound.objects.create(week = rounds, time_generated = one.time_ending)

# Celery for lottery 
@shared_task
def CreateLottery():
    one = LotteryRound.objects.last()
    rounds = int(one.week) + 1
    LotteryRound.objects.create(week = rounds, time_generated = one.time_ending)