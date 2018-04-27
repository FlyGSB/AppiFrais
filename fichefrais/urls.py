from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from fichefrais.views.Api import (AndroidUserFicheFraisViewSet, android_detail_fiche_frais_view)
from .views import (creation_frais, home_visiteur, supprimer_frais, list_fiche_frais, ajout_piece_jointe,
                    home_comptable, validation_frais, selection_visiteur, liste_a_valider, liste_fiche_frais_comptable,
                    creation_forfait, gestion_forfait, cloture_forfait, liste_ancien_forfait,
                    home_admin, edit_elem_fiche_frais, supression_user, gestion_utilisateur, modification_user,
                    home, fiche_frais, user_fiche_frais, customAuthToken)

router = routers.DefaultRouter()
router.register(r'user_fiche_frais', AndroidUserFicheFraisViewSet)

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^fichefrais/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', fiche_frais, name="fichefrais"),
    url(r'^fichefrais/(?P<id_user>[0-9]+)/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', user_fiche_frais, name="user_fichefrais"),
    # VISITEUR
    url(r'^visiteur/$', home_visiteur, name="home_visiteur"),
    url(r'^visiteur/ajout_fichefrais/$', creation_frais, name="creation_ff"),
    url(r'^visiteur/listfichefrais/$', list_fiche_frais, name="list_fiche_frais"),
    url(r'^visiteur/justificatif/$', ajout_piece_jointe, name="ajout_justificatif"),
    url(r'^visiteur/edit/(?P<type_elem>\w+)/(?P<obj_id>[0-9]+)/$', edit_elem_fiche_frais, name="edit_elem_fiche_frais"),
    url(r'^visiteur/suppr_frais/(?P<type_elem>\w+)/(?P<obj_id>[0-9]+)/$', supprimer_frais, name="suppr_elem_frais"),
    # COMPTABLE
    url(r'^comptable/$', home_comptable, name="home_comptable"),
    url(r'^comptable/validation/(?P<valide>[0-9]+)/(?P<type_frais>\w+)/(?P<frais_id>[0-9]+)/$', validation_frais, name="validation_frais"),
    url(r'^comptable/liste_validation/$', liste_a_valider, name="liste_validation"),
    url(r'^comptable/liste_fiche/$', liste_fiche_frais_comptable, name="liste_fiche"),
    url(r'^comptable/liste_forfait/$', liste_ancien_forfait, name="liste_ancien_forfait"),
    url(r'^comptable/selection_visiteur/$', selection_visiteur, name="selection_visiteur"),
    url(r'^comptable/ajout_forfait/$', creation_forfait, name="ajout_forfait"),
    url(r'^comptable/cloture_forfait/(?P<pk>[0-9]+)/$', cloture_forfait, name="cloture_forfait"),
    url(r'^comptable/gestion_forfait/$', gestion_forfait, name="gestion_forfait"),
    # ADMIN
    url(r'^administration/$', home_admin, name="home_admin"),
    url(r'^administration/gestion_user/$', gestion_utilisateur, name="gestion_utilisateur"),
    url(r'^administration/del_utilisateur/(?P<user_id>[0-9]+)/$', supression_user, name="suppression_user"),
    url(r'^administration/modif_user/(?P<user_id>[0-9]+)/$', modification_user, name="modification_user"),
    # API
    url(r'^api-rest/', include(router.urls)),
    url(r'^api-rest/detail_fiche_frais/(?P<pk>[0-9]+)/$', android_detail_fiche_frais_view),
    url(r'^api-token-auth/',  customAuthToken, name="customAuthToken"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
