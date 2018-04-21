from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware

from fichefrais.models import Etat, Forfait
from accounts.models import Job, Profile
from django.contrib.auth.models import User
from datetime import date, datetime


etats = ((1, "blue", "Crée"),
         (2, "orange", "Cloturée"),
         (3, "green", "Validée"),
         (4, "red", "Refusée"),
         (5, "yellow", "Mise en paiement"),
         (6, "green", "Remboursée"),
         (7, "yellow", "En Traitement"))

jobs = (("Administrateur", 3, "home_admin"),
        ("Comptable", 2, "home_comptable"),
        ("Visiteur", 1, "home_visiteur"))

users = (('Villechalane', 'Louis', 'lvillachane', 'jux7gjux7g', '8 rue des Charmes', '46000', 'Cahors', 2005, 12, 21, 1),
        ('Andre', 'David', 'dandre', 'oppg5oppg5', '1 rue Petit', '46200', 'Lalbenque', 1998, 11, 23, 1),
        ('Bedos', 'Christian', 'cbedos', 'gmhxdgmhxd', '1 rue Peranud', '46250', 'Montcuq', 1995, 1, 12, 1),
        ('Tusseau', 'Louis', 'ltusseau', 'ktp3sktp3s', '22 rue des Ternes', '46123', 'Gramat', 2000, 5, 1, 3),
        ('Bentot', 'Pascal', 'pbentot', 'doyw1doyw1', '11 allée des Cerises', '46512', 'Bessines', 1992, 7, 9, 1),
        ('Bioret', 'Luc', 'lbioret', 'hrjfshrjfs', '1 Avenue gambetta', '46000', 'Cahors', 1998, 5, 11, 1),
        ('Bunisset', 'Francis', 'fbunisset', '4vbnd4vbnd', '10 rue des Perles', '93100', 'Montreuil', 1987, 10, 21, 2),
        ('Bunisset', 'Denise', 'dbunisset', 's1y1rs1y1r', '23 rue Manin', '75019', 'paris', 2010, 12, 5, 1),
        ('Cacheux', 'Bernard', 'bcacheux', 'uf7r3uf7r3', '114 rue Blanche', '75017', 'Paris', 2009, 11, 12, 1),
        ('Cadic', 'Eric', 'ecadic', '6u8dc6u8dc', '123 avenue de la République', '75011', 'Paris', 2008, 9, 23, 1),
        ('Charoze', 'Catherine', 'ccharoze', 'u817ou817o', '100 rue Petit', '75019', 'Paris', 2005, 11, 12, 1),
        ('Clepkens', 'Christophe', 'cclepkens', 'bw1usbw1us', '12 allée des Anges', '93230', 'Romainville', 2003, 8, 11, 1),
        ('Cottin', 'Vincenne', 'vcottin', '2hoh92hoh9', '36 rue Des Roches', '93100', 'Monteuil', 2001, 11, 18, 2),
        ('Daburon', 'François', 'fdaburon', '7oqpv7oqpv', '13 rue de Chanzy', '94000', 'Créteil', 2002, 2, 11, 1),
        ('De', 'Philippe', 'pde', 'gk9kxgk9kx', '13 rue Barthes', '94000', 'Créteil', 2010, 12, 14, 1),
        ('Debelle', 'Michel', 'mdebelle', 'od5rtod5rt', '181 avenue Barbusse', '93210', 'Rosny', 2006, 11, 23, 1),
        ('Debelle', 'Jeanne', 'jdebelle', 'nvwqqnvwqq', '134 allée des Joncs', '44000', 'Nantes', 2000, 5, 11, 2),
        ('Debroise', 'Michel', 'mdebroise', 'sghkbsghkb', '2 Bld Jourdain', '44000', 'Nantes', 2001, 4, 17, 1),
        ('Desmarquest', 'Nathalie', 'ndesmarquest', 'f1fobf1fob', '14 Place d Arc', '45000', 'Orléans', 2005, 11, 12, 1),
        ('Desnost', 'Pierre', 'pdesnost', '4k2o54k2o5', '16 avenue des Cèdres', '23200', 'Guéret', 2001, 2, 5, 1),
        ('Dudouit', 'Frédéric', 'fdudouit', '44im844im8', '18 rue de l église', '23120', 'GrandBourg', 2000, 8, 1, 1),
        ('Duncombe', 'Claude', 'cduncombe', 'qf77jqf77j', '19 rue de la tour', '23100', 'La souteraine', 1987, 10, 10, 1),
        ('Enault-Pascreau', 'Céline', 'cenault', 'y2qduy2qdu', '25 place de la gare', '23200', 'Gueret', 1995, 9, 1, 1),
        ('Eynde', 'Valérie', 'veynde', 'i7sn3i7sn3', '3 Grand Place', '13015', 'Marseille', 1999, 11, 1, 1),
        ('Finck', 'Jacques', 'jfinck', 'mpb3tmpb3t', '10 avenue du Prado', '13002', 'Marseille', 2001, 11, 10, 1),
        ('Frémont', 'Fernande', 'ffremont', 'xs5tqxs5tq', '4 route de la mer', '13012', 'Allauh', 1998, 10, 1, 3),
        ('Gest', 'Alain', 'agest', 'dywvtdywvt', '30 avenue de la mer', '13025', 'Berre', 1985, 11, 1, 1))

forfaits_hist = (("Forfait Etape", 110, 2017, 1, 30, 2017, 12, 31),
                 ("Forfait Etape", 102.5, 2016, 6, 30, 2017, 1, 29),
                 ("Forfait Etape", 100, 2016, 1, 1, 2016, 5, 31),
                 ("Nuitée Hôtel", 75, 2016, 1, 1, 2017, 1, 30),
                 ("Repas Restaurant", 22.50, 2017, 1, 30, 2017, 12, 31),
                 ("Repas Restaurant", 20, 2016, 1, 1, 2017, 1, 29),
                 ("Frais Kilométrique", 0.58, 2016, 1, 1, 2017, 12, 31))

forfaits = (("Forfait Etape", 110, 2018, 1, 1),
            ("Nuitée Hôtel", 75, 2017, 1, 31),
            ("Repas Restaurant", 22.50, 2018, 1, 1),
            ("Frais Kilométrique", 0.58, 2018, 1, 1))


class Command(BaseCommand):
    help = 'Initialise la base de données et injecte le jeu de test principal'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        Etat.objects.all().delete()
        for e in etats:
            Etat.objects.create(valeur=e[0], color=e[1], libelle=e[2])
        print("etat ok")

        Job.objects.all().delete()
        for e in jobs:
            Job.objects.create(libelle_job=e[0], valeur_job=e[1], home_job=e[2])
        print("job ok")

        User.objects.all().delete()
        for e in users:
            use = User.objects.create(first_name=e[1], last_name=e[0], email=e[2]+"@gsb.com", username=e[2]
                                      , date_joined=make_aware(datetime(e[7], e[8], e[9]), timezone=None, is_dst=None))
            use.set_password(e[3])
            use.save()

            Profile.objects.create(user=use, adresse=e[4], ville=e[6], cp=e[5], job=Job.objects.get(valeur_job=e[10]))
        print("user ok")

        Forfait.objects.all().delete()
        for e in forfaits:
            Forfait.objects.create(libelle_forfait=e[0], montant=e[1], date_debut=date(e[2], e[3], e[4]))
        for e in forfaits_hist:
            Forfait.objects.create(libelle_forfait=e[0], montant=e[1], date_debut=date(e[2], e[3], e[4]),
                                   date_fin=date(e[5], e[6], e[7]))
        print("forfaits ok")
