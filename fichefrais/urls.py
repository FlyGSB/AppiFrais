from django.conf.urls import url, include
from rest_framework.authtoken import views as auth_views
from .views import *


urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^fichefrais/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', fiche_frais, name="fichefrais"),
    url(r'^fichefrais/(?P<id_user>[0-9]+)/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', user_fiche_frais, name="user_fichefrais"),
    url(r'^fichefrais/pdf/(?P<id_fiche>[0-9]+)/$', GeneratePDF.as_view()),
    url(r'^password_change/$', changer_mdp, name="changer_mdp"),
    # VISITEUR
    url(r'^visiteur/$', home_visiteur, name="home_visiteur"),
    url(r'^visiteur/ajout_fichefrais/$', creation_frais, name="creation_ff"),
    url(r'^visiteur/liste_fiche/$', list_fiche_frais, name="list_fiche_frais"),
    url(r'^visiteur/justificatif/$', ajout_piece_jointe, name="ajout_justificatif"),
    url(r'^visiteur/edit_frais_forfait/(?P<pk>[0-9]+)/$', edit_ligne_frais_forfait, name="edit_ligne_frais_forfait"),
    url(r'^visiteur/edit_frais_hors_forfait/(?P<pk>[0-9]+)/$', edit_ligne_frais_hors_forfait, name="edit_ligne_frais_hors_forfait"),
    url(r'^visiteur/suppr_frais_forfait/(?P<pk>[0-9]+)/$', suppr_ligne_frais_forfait, name="suppr_ligne_frais_forfait"),
    url(r'^visiteur/suppr_frais_hors_forfait/(?P<pk>[0-9]+)/$', suppr_ligne_frais_hors_forfait, name="suppr_ligne_frais_hors_forfait"),
    url(r'^visiteur/suppr_justificatif/(?P<pk>[0-9]+)/$', suppr_justificatif, name="suppr_justificatif"),
    # COMPTABLE
    url(r'^comptable/$', home_comptable, name="home_comptable"),
    url(r'^comptable/validation/(?P<valide>[0-9]+)/(?P<type_frais>\w+)/(?P<frais_id>[0-9]+)/$', validation_frais, name="validation_frais"),
    url(r'^comptable/liste_validation/$', liste_a_valider, name="liste_validation"),
    url(r'^comptable/liste_fiche/$', liste_fiche_frais_comptable, name="liste_fiche"),
    url(r'^comptable/liste_forfait/$', liste_ancien_forfait, name="liste_ancien_forfait"),
    url(r'^comptable/selection_visiteur/$', selection_visiteur, name="selection_visiteur"),
    url(r'^comptable/ajout_forfait/$', creation_forfait, name="ajout_forfait"),
    url(r'^comptable/edit_forfait/(?P<pk>[0-9]+)/$', edit_forfait, name="edit_forfait"),
    url(r'^comptable/cloture_forfait/(?P<pk>[0-9]+)/$', cloture_forfait, name="cloture_forfait"),
    url(r'^comptable/gestion_forfait/$', gestion_forfait, name="gestion_forfait"),
    # ADMIN
    url(r'^administration/$', home_admin, name="home_admin"),
    url(r'^administration/gestion_user/$', gestion_utilisateur, name="gestion_utilisateur"),
    url(r'^administration/del_utilisateur/(?P<user_id>[0-9]+)/$', supression_user, name="suppression_user"),
    url(r'^administration/modif_user/(?P<user_id>[0-9]+)/$', modification_user, name="modification_user"),
    # API
    url(r'^api-rest/detail_fiche_frais/(?P<pk>[0-9]+)/$', android_detail_fiche_frais_view),
    url(r'^api-rest/user_fiche_frais/(?P<pk>[0-9]+)/$', android_user_fiche_frais_view),
    url(r'^api-token-auth/', auth_views.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
