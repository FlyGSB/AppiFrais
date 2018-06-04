# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-30 17:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import fichefrais.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Etat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=20)),
                ('color', models.CharField(blank=True, max_length=20)),
                ('valeur', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FicheFrais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('date_modif', models.DateTimeField(auto_now=True)),
                ('nb_justificatif', models.IntegerField()),
                ('montant_valide', models.FloatField(max_length=6)),
                ('etat', models.ForeignKey(on_delete=models.SET(0), to='fichefrais.Etat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fiche_frais', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Forfait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle_forfait', models.CharField(max_length=50)),
                ('montant', models.FloatField(max_length=6)),
                ('date_debut', models.DateField(auto_now_add=True)),
                ('date_fin', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LigneFraisForfait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField()),
                ('date_frais', models.DateField()),
                ('date_ajout', models.DateField(auto_now_add=True)),
                ('date_modification', models.DateField(auto_now=True)),
                ('etat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fichefrais.Etat')),
                ('fiche_frais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frais_forfait', to='fichefrais.FicheFrais')),
                ('forfait', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forfait', to='fichefrais.Forfait')),
            ],
        ),
        migrations.CreateModel(
            name='LigneFraisHorsForfait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.FloatField(max_length=6)),
                ('libelle_hors_forfait', models.CharField(max_length=40)),
                ('date_frais', models.DateField()),
                ('date_ajout', models.DateField(auto_now_add=True)),
                ('date_modification', models.DateField(auto_now=True)),
                ('etat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fichefrais.Etat')),
                ('fiche_frais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frais_hors_forfait', to='fichefrais.FicheFrais')),
            ],
        ),
        migrations.CreateModel(
            name='PieceJointe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
                ('date_ajout', models.DateField(auto_now_add=True)),
                ('date_modification', models.DateField(auto_now=True)),
                ('piece', models.FileField(blank=True, null=True, upload_to=fichefrais.utils.user_directory_path)),
                ('fiche_frais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='justificatif', to='fichefrais.FicheFrais')),
            ],
        ),
    ]
