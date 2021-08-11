# Generated by Django 3.2.5 on 2021-08-06 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Comments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Issues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='author_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='issue_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Issues.issues'),
        ),
    ]
