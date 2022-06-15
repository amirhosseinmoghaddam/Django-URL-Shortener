from django.db import models

class Urls(models.Model):
    main_url = models.CharField(max_length=10000)
    shorten_url = models.CharField(max_length=256)
    visits = models.IntegerField(default=0)