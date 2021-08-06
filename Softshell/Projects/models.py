from django.db import models

from django.conf import settings

class Projects(models.Model):
    PROJECT_TYPES = [
                    ('BE', 'Back-end'),
                    ('FE', 'Front-end'),
                    ('IOS', 'IOS'),
                    ('ANDROID', 'Android'),
                    ]

    project_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=7, choices=PROJECT_TYPES)
    author_user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                                       on_delete=models.RESTRICT
                                       )
