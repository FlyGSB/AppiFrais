from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from fichefrais.models import FicheFrais, LigneFraisHorsForfait, LigneFraisForfait
from fichefrais.serializers import (AndroidLigneFraisForfaitSerializer, AndroidLigneFraisHorsForfaitSerializer,
                                    AndroidFicheFraisSerializer)

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'name': "%s %s" % (user.first_name, user.last_name)
        })

###########
# ANDROID #
###########


@api_view(["GET"])
@authentication_classes((TokenAuthentication, BasicAuthentication, SessionAuthentication))
@permission_classes((IsAuthenticated,))
def android_user_fiche_frais_view(request, pk):
    """
    Affichage de l'API pour android
    :param pk: id d'un utilisateur
    :return: une reponse au format JSON
    """
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
    """
    Affiche les details d'une fiche de frais
    :param pk: clef primaire d'une fiche de frais
    :return: une reponse au format JSON
    """
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
