from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from fichefrais.models import FicheFrais, LigneFraisHorsForfait, LigneFraisForfait
from fichefrais.serializers import (AndroidLigneFraisForfaitSerializer, AndroidLigneFraisHorsForfaitSerializer,
                                    AndroidFicheFraisSerializer)

###########
# ANDROID #
###########


@api_view(["GET"])
@authentication_classes((TokenAuthentication, BasicAuthentication, SessionAuthentication))
@permission_classes((IsAuthenticated,))
def android_user_fiche_frais_view(request, pk):
    try:
        fiches_frais = FicheFrais.objects.filter(user_id=pk)
    except FicheFrais.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        all_fiche = AndroidFicheFraisSerializer(fiches_frais, many=True)
        return Response(all_fiche.data)


@api_view(["GET"])
@authentication_classes((TokenAuthentication, BasicAuthentication, SessionAuthentication))
@permission_classes((IsAuthenticated,))
def android_detail_fiche_frais_view(request, pk):
    try:
        fiche_frais = FicheFrais.objects.get(pk=pk)
    except FicheFrais.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        ligne_frais_forfait = LigneFraisForfait.objects.filter(fiche_frais=fiche_frais)
        ligne_frais_hors_forfait = LigneFraisHorsForfait.objects.filter(fiche_frais=fiche_frais)
        ff_serialize = AndroidLigneFraisForfaitSerializer(ligne_frais_forfait, many=True)
        hf_serialize = AndroidLigneFraisHorsForfaitSerializer(ligne_frais_hors_forfait, many=True)
        return Response(ff_serialize.data + hf_serialize.data)
