# Generated by Django 5.1.3 on 2025-02-06 15:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FaSequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Full Genome', 'Full Genome'), ('Coding DNA Sequence', 'Coding DNA Sequence'), ('Peptide Sequence', 'Peptide Sequence')], default='Coding DNA Sequence', max_length=50)),
                ('sequence', models.TextField()),
                ('identifiant', models.CharField(default='Non defini', max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fa_sequences', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
