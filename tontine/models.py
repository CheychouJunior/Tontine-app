from distutils.command.upload import upload
from email.policy import default
from django.db import models
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from datetime import date

# Create your models here.


class AppartenirTontine(models.Model):
    id_membre = models.ForeignKey('Membre', models.CASCADE, db_column='id_membre' )
    id_tontine = models.ForeignKey('Tontine', models.CASCADE, db_column='id_tontine')
    statut = models.CharField(max_length=30, blank=True, null=True)
    nbr_parts = models.IntegerField()

    class Meta:
    
        db_table = 'Appartenir_tontine'
        unique_together = (('id_membre', 'id_tontine'),)


    def __str__(self):
        return str(self.nbr_parts)


class Candidat(models.Model):
    id_candidat = models.AutoField(primary_key=True)
    id_membre = models.ForeignKey('Membre', models.CASCADE, db_column='id_membre')
    id_election = models.ForeignKey('Election', models.CASCADE, db_column='id_election')
    id_poste = models.ForeignKey('Poste', models.CASCADE, db_column='id_poste')

    class Meta:
    
        db_table = 'Candidat'

    def __str__(self):
        return str(self.id_candidat)  

class ContribuerFond(models.Model):
    id_fond = models.ForeignKey('Fond', models.CASCADE, db_column='id_fond')
    id_membre = models.ForeignKey('Membre', models.CASCADE, db_column='id_membre')
    date = models.DateField(default=date.today)

    class Meta:
    
        db_table = 'Contribuer_fond'
        unique_together = (('id_fond', 'id_membre', 'date'),)


class Cotisation(models.Model):
    id_cotisation = models.AutoField(primary_key=True)
    id_tontine = models.ForeignKey('Tontine', models.CASCADE, db_column='id_tontine')
    nom_cotisation = models.CharField(max_length=25)
    montant = models.IntegerField()
    date_debut = models.DateField()
    cycle = models.IntegerField()
    nb_participant = models.IntegerField()
    taux_interet = models.IntegerField()

    class Meta:
    
        db_table = 'Cotisation'
    def __str__(self):
        return self.nom_cotisation

class Cotiser(models.Model):
    id_membre = models.ForeignKey('Membre', models.CASCADE, db_column='id_membre')
    id_cotisation = models.ForeignKey('Cotisation', models.CASCADE, db_column='id_cotisation')
    date = models.DateField(default=date.today)

    class Meta:
    
        db_table = 'Cotiser'
        unique_together = (('id_membre', 'id_cotisation', 'date'),)

    def __str__(self):
        return str(self.id_membre)        


class Election(models.Model):
    id_election = models.AutoField(primary_key=True)
    id_tontine = models.ForeignKey('Tontine', models.CASCADE, db_column='id_tontine')
    date = models.DateField()
    heure_election = models.TimeField()
    temps_renouvelable = models.IntegerField()

    class Meta:
    
        db_table = 'Election'

    def __str__(self):
        return str(self.id_election)           


class Fond(models.Model):
    id_fond = models.AutoField(primary_key=True)
    id_tontine = models.ForeignKey('Tontine', models.CASCADE, db_column='id_tontine')
    id_membre = models.ForeignKey('Membre', models.CASCADE, db_column='id_membre')
    type_fond = models.CharField(max_length=25)
    nom_fond = models.CharField(max_length=25, blank=True, null=True)
    montant = models.IntegerField()
    objectif = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
    
        db_table = 'Fond'

    def __str__(self):
        return str(self.id_fond)   

class Membre(AbstractUser):
    id_membre = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25,unique=True,null=True)
    prenom = models.CharField(max_length=25, blank=True, null=True)
    e_mail = models.EmailField (max_length=50, blank=True, null=True)
    adresse = models.CharField(max_length=15)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    date_naissance = models.DateField(null=True)
    profession = models.CharField(max_length=25,null=True)

    class Meta:
    
        db_table = 'Membre'
    

    def __str__(self):
        return str(self.username)   



class ParticipantReunion(models.Model):
    id_reunion = models.ForeignKey('Reunion', models.CASCADE, db_column='id_reunion')
    id_membre = models.ForeignKey(Membre, models.CASCADE, db_column='id_membre')

    class Meta:
    
        db_table = 'Participant_Reunion'
        unique_together = (('id_reunion', 'id_membre'),)


class Poste(models.Model):
    id_poste = models.AutoField(primary_key=True)
    nom_poste = models.CharField(max_length=25)

    class Meta:
    
        db_table = 'Poste'
    def __str__(self):
        return str(self.id_poste)

class Pret(models.Model):
    id_pret = models.AutoField(primary_key=True)
    id_tontine = models.ForeignKey('Tontine', models.CASCADE, db_column='id_tontine')
    id_membre = models.ForeignKey(Membre, models.CASCADE, db_column='id_membre')
    nom_pret = models.CharField(max_length=25, blank=True, null=True)
    date_pret = models.DateField()
    montant = models.IntegerField()
    date_remboursement = models.DateField()
    interet = models.IntegerField(default=10)
    sanction = models.IntegerField(default=10)
    raison = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        
        db_table = 'Pret'

    def __str__(self):
        return str(self.id_pret)   

class Rembourserpret(models.Model):
    id_pret = models.ForeignKey('Pret', models.CASCADE, db_column='id_pret')
    id_membre = models.ForeignKey(Membre, models.CASCADE, db_column='id_membre')
    montant = models.IntegerField()
    date_remboursement = models.DateField(default=date.today)

    class Meta:
        
        db_table = 'Rembourser_pret'


class Reunion(models.Model):
    id_reunion = models.AutoField(primary_key=True)
    id_tontine = models.ForeignKey('Tontine', models.CASCADE, db_column='id_tontine')
    date_reunion = models.DateField()
    beneficiare = models.CharField(max_length=25)
    lieu = models.CharField(max_length=25)
    heure = models.TimeField()
    regle = models.CharField(max_length=1000, blank=True, null=True)
    motif = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        
        db_table = 'Reunion'

    def __str__(self):
        return str(self.id_reunion)   

class ListePresence(models.Model):
    id_reunion = models.ForeignKey('Reunion', models.CASCADE, db_column='id_reunion')
    id_membre = models.ForeignKey('Membre', models.CASCADE, db_column='id_membre')

    class Meta:
        db_table = 'Liste_Presence'
        unique_together = (('id_membre', 'id_reunion'),)

class Tontine(models.Model):
    id_tontine = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=15)
    date_creation = models.DateField()
    slogan = models.CharField(max_length=100, blank=True, null=True)
    regle = models.CharField(max_length=1000, blank=True, null=True)
    author = models.ForeignKey('Membre', models.CASCADE, db_column='username')

    class Meta:
        db_table = 'Tontine'

    def __str__(self):
        return str(self.id_tontine)   

    def get_absolute_url(self):
        return reverse("update_tontine", kwargs={"pk": self.pk})

class Vote(models.Model):
    id_membre = models.ForeignKey('Membre', models.CASCADE, db_column='id_membre')
    id_election = models.ForeignKey('Election', models.CASCADE, db_column='id_election')
    id_poste = models.ForeignKey('Poste', models.CASCADE, db_column='id_poste')
    id_candidat = models.ForeignKey('Candidat', models.CASCADE, db_column='id_candidat')

    class Meta:
        
        db_table = 'Vote'
        unique_together = (('id_membre', 'id_election', 'id_poste'),)


