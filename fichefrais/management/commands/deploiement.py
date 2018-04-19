from django.core.management.base import BaseCommand
from fichefrais.models import Etat

etats = ((1, "blue", "Créer"),
         (2, "orange", "Cloturée"),
         (3, "green", "Validée"),
         (4, "red", "Refusée"),
         (5, "yellow", "Mise en paiement"),
         (6, "green", "Remboursée"),
         (7, "yellow", "En Traitement"))


class Command(BaseCommand):
    help = 'Crée tout les états possible pour les frais et fiches'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        qs_etat = Etat.objects.all()
        for e in qs_etat:
            e.delete()

        for e in etats:
            Etat.objects.create(valeur=e[0], color=e[1], libelle=e[2])
