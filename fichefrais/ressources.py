from tastypie.resources import ModelResource
from fichefrais.models.FicheFrais import FicheFrais


class FicheFraisResource(ModelResource):

    class Meta:
        queryset = FicheFrais.objects.all()
        resourece_name = "fichefrais"
