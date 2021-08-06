# Generated by Django 3.2.5 on 2021-08-05 07:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=128)),
                ('author_user_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]