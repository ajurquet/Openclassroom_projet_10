from Users.models import Users
from django.db import models

from django.conf import settings
from Projects.models import Projects


class Issues(models.Model):
    PRIORITY = [
               ('FAIBLE', 'Faible'),
               ('MOYENNE', 'Moyenne'),
               ('ELEVEE', 'Elevée'),
               ]

    TAG = [
          ('BUG', 'Bug'),
          ('AMELIORATION', 'Amélioration'),
          ('TACHE', 'Tâche')
          ]

    STATUT = [
             ('A_FAIRE', 'A faire'),
             ('EN_COURS', 'En cours'),
             ('TERMINE', 'Terminé')
             ]

    title = models.CharField(max_length=128, blank=False)
    desc = models.CharField(max_length=128)
    tag = models.CharField(max_length=12, choices=TAG)
    priority = models.CharField(max_length=7, choices=PRIORITY)
    project_id = models.ForeignKey(Projects,
                                   on_delete=models.CASCADE,
                                   related_name='Issues'
                                   )
    status = models.CharField(max_length=8, choices=STATUT)
    author_user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                                       on_delete=models.RESTRICT,
                                       related_name='Issues_created'
                                       )
    assignee_user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                                         on_delete=models.RESTRICT,
                                         related_name='Issues_assigned',
                                         default=Users.user_id
                                         )
    created_time = models.DateTimeField(auto_now_add=True)
