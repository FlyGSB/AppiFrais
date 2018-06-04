import datetime
from django.core.management.base import BaseCommand
from fichefrais.models import FicheFrais, Etat, LigneFraisForfait, LigneFraisHorsForfait


class Command(BaseCommand):
    help = 'Cloture les fiches de frais de mois -1'

    def add_arguments(self, parser):
        """
        :param parser:
        :return:
        """
        pass

    def handle(self, *args, **options):
        """
        TODO: Faire la command de crontab qui cloture les fiches automatiquement
        :param args:
        :param options:
        :return:
        """
        today = datetime.date.today()
        if today.day == 20:
            pass

        all_fiche_frais = FicheFrais.objects.all()

        cloture = Etat.objects.get(valeur=2)
        refuse = Etat.objects.get(valeur=4)
        paiement = Etat.objects.get(valeur=5)
        rembourse = Etat.objects.get(valeur=6)

        print("Nombre de fiche de frais: %s" % all_fiche_frais.count())
        for fiche_frais in all_fiche_frais:
            fiche_frais.set_montant_valide()

            if today.day >= 10:
                if fiche_frais.date.month == today.month and fiche_frais.date.year == today.year:
                    if fiche_frais.etat.valeur < 3:
                        fiche_frais.etat = cloture
                        fiche_frais.save()

            if today.day >= 20:
                if fiche_frais.date.month == today.month and fiche_frais.date.year == today.year:
                    if fiche_frais.etat.valeur == 3:
                        fiche_frais.etat = paiement
                        fiche_frais.save()

                ligne_ff = LigneFraisForfait.objects.filter(fiche_frais=fiche_frais)
                ligne_hf = LigneFraisHorsForfait.objects.filter(fiche_frais=fiche_frais)

                for frais in ligne_ff:
                    if frais.etat.valeur != 3:
                        frais.etat = refuse
                        frais.save()

                for frais in ligne_hf:
                    if frais.etat.valeur != 3:
                        frais.etat = refuse
                        frais.save()

            if fiche_frais.date.month < today.month-1 or fiche_frais.date.year < today.year:
                fiche_frais.etat = rembourse
                fiche_frais.save()

                ligne_ff = LigneFraisForfait.objects.filter(fiche_frais=fiche_frais)
                ligne_hf = LigneFraisHorsForfait.objects.filter(fiche_frais=fiche_frais)

                for frais in ligne_ff:
                    if frais.etat.valeur != 3:
                        frais.etat = refuse
                        frais.save()

                for frais in ligne_hf:
                    if frais.etat.valeur != 3:
                        frais.etat = refuse
                        frais.save()

            if fiche_frais.date.month == today.month-1 and fiche_frais.date.year == today.year:
                fiche_frais.etat = paiement
                fiche_frais.save()
