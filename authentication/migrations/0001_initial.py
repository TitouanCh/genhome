# Generated by Django 5.1.3 on 2025-02-06 15:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BioinfoUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('date_joined', models.DateField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True)),
                ('role', models.CharField(choices=[('AT', 'Attente'), ('LE', 'Lecteur'), ('AN', 'Annotateur'), ('VA', 'Validateur'), ('AD', 'Admin')], default='AD', max_length=24)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoleRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_role', models.CharField(choices=[('AT', 'Attente'), ('LE', 'Lecteur'), ('AN', 'Annotateur'), ('VA', 'Validateur'), ('AD', 'Admin')], default='LE', max_length=24)),
                ('status', models.CharField(choices=[('A', 'Accepté'), ('P', 'Attente'), ('D', 'Refusé')], default='P', max_length=1)),
                ('date_submitted', models.DateField(auto_now_add=True, verbose_name='Date de soumission')),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
