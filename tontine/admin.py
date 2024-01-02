from django.contrib import admin
from .models import *


# Register your models here.

class AdminMembre(admin.ModelAdmin):
    list_display=('id_membre','username','prenom','e_mail','adresse','telephone','date_naissance','profession')

class AdminAppartenir(admin.ModelAdmin):
    list_display=('id_membre', 'id_tontine','statut','nbr_parts' )

class AdminCandidat(admin.ModelAdmin):
    list_display=('id_candidat','id_membre','id_election','id_poste')    

class AdminContribuer(admin.ModelAdmin):
    list_display=('id_fond','id_membre','date')    

class AdminCotisation(admin.ModelAdmin):
    list_display=('id_cotisation','id_tontine','nom_cotisation','montant','date_debut','cycle','nb_participant','taux_interet')    

class AdminCotiser(admin.ModelAdmin):
    list_display=('id_membre', 'id_cotisation','date')    

class AdminElection(admin.ModelAdmin):
    list_display=('id_election','id_tontine','date','heure_election','temps_renouvelable')    

class AdminFond(admin.ModelAdmin):
    list_display=('id_fond', 'id_tontine','id_membre' ,'type_fond' ,'nom_fond','montant','objectif')    

class AdminParticipant(admin.ModelAdmin):
    list_display=('id_reunion','id_membre')    

class AdminPost(admin.ModelAdmin):
    list_display=('id_poste','nom_poste')    

class AdminPret(admin.ModelAdmin):
    list_display=('id_pret','id_tontine','id_membre','nom_pret','date_pret','montant','date_remboursement','interet','sanction','raison') 

class AdminReunion(admin.ModelAdmin):
    list_display=('id_reunion','id_tontine','date_reunion' ,'beneficiare','lieu','heure','regle','motif')

class AdminTontine(admin.ModelAdmin):
    list_display=('id_tontine','nom','date_creation','slogan','regle')

class AdminVote(admin.ModelAdmin):
    list_display=('id_membre','id_election' ,'id_poste','id_candidat')

class AdminRembourserPret(admin.ModelAdmin):
    list_display=('id_pret','id_membre','montant','date_remboursement') 


#admin.site.register(User)
admin.site.register(AppartenirTontine,AdminAppartenir)
admin.site.register(Candidat,AdminCandidat)
admin.site.register(Cotisation,AdminCotisation)
admin.site.register(Cotiser,AdminCotiser)
admin.site.register(Election,AdminElection)
admin.site.register(Fond,AdminFond)
admin.site.register(Membre,AdminMembre)
admin.site.register(ParticipantReunion,AdminParticipant)
admin.site.register(Poste,AdminPost)
admin.site.register(Pret,AdminPret)
admin.site.register(Reunion,AdminReunion)
admin.site.register(Tontine,AdminTontine)
admin.site.register(Vote,AdminVote)
admin.site.register(Rembourserpret, AdminRembourserPret)