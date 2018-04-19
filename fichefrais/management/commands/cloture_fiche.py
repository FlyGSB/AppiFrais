import datetime

from django.core.management.base import BaseCommand, CommandError


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
