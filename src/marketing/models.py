from django.db import models
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from .utils import Mailchimp

User = settings.AUTH_USER_MODEL

# Create your models here.

class MarketingPreference(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE )
    subcribed = models.BooleanField(default = True)
    mailchimp_msg = models.TextField(null = True, blank = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user.email


def marketing_pref_update_reciever(sender, instance, created, *args, **kwargs):
    if created:
        pass
        print('Add user to mailchimp')
        status_code, response_data = Mailchimp().subscribe(instance.user.email)
        print(status_code, response_data)

post_save.connect(marketing_pref_update_reciever, sender = MarketingPreference)


def make_marketing_pref_reciever(sender, instance, created, *args, **kwargs):

    if created:
        MarketingPreference.objects.get_or_create(user = instance)

post_save.connect(make_marketing_pref_reciever, sender = User)
