from django.urls import path
from tontine.views import *


urlpatterns = [
    path('login/', Login, name='login'),
    path('register/', register, name='register'),
    path('home/', home, name='home'),
#---------------------------------------------------------------------------------------------
    path('create/', TontineCreate, name='create_tontine' ),
    path('tontine/<int:pk>', TontineDetails, name='show_details'),
    path('tontine/delete/<int:pk>', TontineDelete, name='delete_tontine'),
    path('tontine/update_tontine/<int:pk>', TontineModify, name='update_tontine'),
    path('tontine/ajouter_membre/<int:pk>', AjouterMembre, name='ajouter_membre'),
    path('tontine/search_tontine', TontineSearch.as_view(), name='search_tontine'),
#----------------------------------------------------------------------------------------------
    path('tontine/update_membre', MemberModify, name='update_membre'),
#----------------------------------------------------------------------------------------------
    path('tontine/create_cotisation/<int:pk>', CotisationCreate, name='create_cotisation'),
    path('tontine/cotisation/<int:pk>', CotisationDetails, name='cotisation_details'),
    path('tontine/cotiser/<int:pk>', CotisationAffiche, name='afficher_cotisation'),
    path('tontine/cotiser_cotis/<int:pk>', CotisationContribuer, name='cotiser'),
    path('tontine/suspendre_cotis/<int:pk>', CotisationSuspendre, name='suspendre_cotisation'),
#------------------------------------------------------------------------------------------------
    path('tontine/fond/<int:pk>', FondAffiche, name='fond'),
    path('tontine/create_fond/<int:pk>', FondCreate, name='create_fond'),
    path('tontine/afficher_fond/<int:pk>', FondParticipant, name='afficher_fond'),
    path('tontine/contribuer_fond/<int:pk>', FondContribuer, name='contribuer_fond'),
    path('tontine/update_fond/<int:pk>', FondModify, name='update_fond'),
    path('tontine/delete_fond/<int:pk>', FondDelete, name='delete_fond'),
#-------------------------------------------------------------------------------------------------
    path('tontine/pret/<int:pk>', PretAffiche, name='pret'),
    path('tontine/create_pret/<int:pk>', PretCreate, name='create_pret'),
    path('tontine/pret_details/<int:pk>', PretDetails, name='afficher_pret'),
    path('tontine/rembourser_pret/<int:pk>', PretRembourser, name='rembourser_pret'),
    path('tontine/reporter_pret/<int:pk>', PretReporter, name='reporter_pret'),
#-------------------------------------------------------------------------------------------------
    path('tontine/rapport/<int:pk>', Statistique, name='statistique'),
#---------------------------------------------------------------------------------------------------
    path('tontine/reunion/<int:pk>', ReunionAffiche, name='reunion'),
    path('tontine/create_reunion/<int:pk>', ReunionCreate, name='create_reunion'),
    path('tontine/reunion_details/<int:pk>', ReunionDetails, name='afficher_reunion'),
    path('tontine/reunion_signer/<int:pk>', ReunionSigner, name='signer'),

    
]
