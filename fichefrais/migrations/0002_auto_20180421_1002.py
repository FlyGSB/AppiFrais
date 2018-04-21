# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-21 08:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fichefrais', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lignefraisforfait',
            old_name='frais_forfait',
            new_name='forfait',
        ),
        migrations.AlterField(
            model_name='fichefrais',
            name='etat',
            field=models.ForeignKey(on_delete=models.SET('...'), to='fichefrais.Etat'),
        ),
        migrations.AlterField(
            model_name='fichefrais',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fiche_frais', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lignefraisforfait',
            name='fiche_frais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frais_forfait', to='fichefrais.FicheFrais'),
        ),
        migrations.AlterField(
            model_name='lignefraishorsforfait',
            name='fiche_frais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frais_hors_forfait', to='fichefrais.FicheFrais'),
        ),
        migrations.AlterField(
            model_name='piecesjointe',
            name='fiche_frais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='justificatif', to='fichefrais.FicheFrais'),
        ),
    ]