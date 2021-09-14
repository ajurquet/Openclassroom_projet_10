# Generated by Django 3.2.7 on 2021-09-09 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('BE', 'Back-end'), ('FE', 'Front-end'), ('IOS', 'IOS'), ('ANDROID', 'Android')], max_length=7)),
            ],
        ),
    ]
