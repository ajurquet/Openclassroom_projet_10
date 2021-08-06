from django.db import models

from Issues.models import Issues
from django.conf import settings


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=128, blank=False)
    author_user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                                       on_delete=models.RESTRICT
                                       )
    issue_id = models.ForeignKey(Issues, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

