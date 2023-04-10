from . models import GameRound, LotteryRound, DiceRoll, Account
from django.contrib.auth.models import User
from paystack.models import Paystack
from flutterwave.models import FlutterWave
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from paystack.models import Userhistory
from django.utils import timezone



@receiver(post_save, sender = Paystack)
def HistoryPaystack(sender, created, instance, **kwargs):
    if created:
        history = Userhistory.objects.create(paystack =instance , email= instance.email ,amount = instance.amount, date_created = instance.generated, transaction = 'Deposit')

@receiver(post_save, sender = Paystack)    
def UpdateHistoryPaystack(sender,  instance, created, **kwargs):
    if created == False:
        history  = Userhistory.objects.filter(paystack=instance).update(confirm = instance.verified)
        instance.userhistory.save()
        print('History updated succesfully')


@receiver(post_save, sender = FlutterWave)
def HistoryFlutterwave(sender, created, instance, **kwargs):
    if created:
        history = Userhistory.objects.create(flutterwave =instance , email= instance.email ,amount = instance.amount, date_created = instance.generated, transaction = 'Deposit')

@receiver(post_save, sender = FlutterWave)    
def UpdateHistoryFlutterwave(sender,  instance, created, **kwargs):
    if created == False:
        history  = Userhistory.objects.filter(flutterwave=instance).update(confirm = instance.verified)
        instance.userhistory.save()
        print('History updated succesfully')

#created new round

@receiver(post_save, sender = GameRound)    
def CreateNewRoound(sender,  instance, created, **kwargs):
    if created == False:
        total = GameRound.objects.count()
        last_game = GameRound.objects.get(week=int(total))
        count = 1
        timing = 3
        while count < 5:
            round = GameRound.objects.create(week = int(last_game.week + count), time_generated=last_game.time_generated + timezone.timedelta(minutes=timing))
            print('New Round Created Succesfully')
            count += 1
            timing +=3
            
        

#created new lottery round

@receiver(post_save, sender = LotteryRound)    
def CreateNewRoound(sender,  instance, created, **kwargs):
    if created == False:
        total = LotteryRound.objects.all().count()
        last_game =  LotteryRound.objects.get(week=total)
        count = 1
        timing = 7
        while count < 2:
            round = LotteryRound.objects.create(week = int(last_game.week + count), time_generated=last_game.time_generated + timezone.timedelta(days=timing))
            print('New Round Created Succesfully')
            count += 1
            timing +=7

@receiver(post_save, sender = DiceRoll)
def UpdateUserBalance(sender, instance , created, **kwargs):
    if created == False:
        if instance.status == 'Won':
            user = Account.objects.get(email=instance.user)
            user.balance +=  instance.winnings
            user.save()
        
    
    
    
               


        
        


        
        