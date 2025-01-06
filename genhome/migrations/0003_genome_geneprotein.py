# Generated by Django 5.0.9 on 2025-01-06 13:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genhome', '0002_annotation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sequence', models.TextField()),
                ('species', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GeneProtein',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('sequence', models.TextField()),
                ('genome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genes_proteins', to='genhome.genome')),
            ],
        ),
    ]
