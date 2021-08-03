from django.db import models

from django.conf import settings

class Issues(models.Model):
    title = models.CharField(max_length=128, blank=False)
    desc = models.CharField(max_length=128)
    tag = models.CharField(max_length=128)
    projet_id = models.IntegerField() # Foreign key ???
    status = models.CharField(max_length=128)
    author_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)


