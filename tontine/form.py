from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Membre, Tontine, AppartenirTontine, Cotisation, Fond, Pret, Reunion


class UserForm(UserCreationForm):
    class Meta:
        model = Membre
        fields = ['username','prenom','e_mail','adresse',
        'telephone','date_naissance','profession',
         'password1', 'password2']
    
class RowTontineForm(forms.ModelForm):

    class Meta:
        model = Tontine
        fields = '__all__'
        widgets = {
            'nom':forms.TextInput(attrs={'placeholder': 'Entrer le nom', 'style': 'width: 600px;', 'class': 'form-control'}),
            'date_creation': forms.TextInput(attrs={'placeholder': 'Entrer la date de création', 'style': 'width: 600px;', 'class': 'form-control'}),
            'slogan': forms.TextInput(attrs={'placeholder': 'Entrer le slogan', 'style': 'width: 600px;', 'class': 'form-control'}),
            'regle': forms.Textarea(attrs={'placeholder': 'Entrer le(s) regle(s)', 'style': 'width: 600px;', 'class': 'form-control', 'rows':5, 'cols':10}),
            #'author': forms.Select(attrs={'placeholder': 'Entrer le createur', 'style': 'width: 600px;', 'class': 'form-control'}),
            'author': forms.TextInput(attrs={'style': 'width: 600px;', 'class': 'form-control', 'id':'membre', 'type':'hidden'}),
        }

class AppartenirTontineForm(forms.ModelForm):

    class Meta:
        model = AppartenirTontine
        fields = '__all__'
        widgets = {
            'id_tontine':forms.NumberInput(attrs={'style': 'width: 600px;', 'class': 'form-control', 'id':'tontine', 'type':'hidden'}),
            'id_membre': forms.Select(attrs={'style': 'width: 600px;', 'class': 'form-control'}),
            'statut': forms.TextInput(attrs={'placeholder': 'Entrer son statut', 'style': 'width: 600px;', 'class': 'form-control'}),
            'nbr_parts': forms.NumberInput(attrs={'placeholder': 'Entrer le nombre de part qu\'il ou elle possède', 'style': 'width: 600px;', 'class': 'form-control'}),
        }

class CotisationForm(forms.ModelForm):

    class Meta:
        model = Cotisation
        fields = '__all__'
        widgets = {
            'id_tontine':forms.NumberInput(attrs={'style': 'width: 600px;', 'class': 'form-control', 'id':'tontine', 'type':'hidden'}),
            'nom_cotisation':forms.TextInput(attrs={'placeholder': 'Entrer le nom de la cotisation', 'style': 'width: 600px;', 'class': 'form-control'}),
            'montant': forms.NumberInput(attrs={'placeholder': 'Entrer le montant de contribution', 'style': 'width: 600px;', 'class': 'form-control'}),
            'date_debut': forms.DateInput(attrs={'placeholder': 'jj/mm/aaaa', 'style': 'width: 600px;', 'class': 'form-control'}),
            'cycle': forms.NumberInput(attrs={'placeholder': 'Entrer le cycle (en nombre de jour)', 'style': 'width: 600px;', 'class': 'form-control'}),
            'taux_interet': forms.NumberInput(attrs={'placeholder': '%', 'style': 'width: 600px;', 'class': 'form-control'}),
        }

class FondForm(forms.ModelForm):

    class Meta:
        model = Fond
        fields = '__all__'
        widgets = {
            'id_tontine':forms.NumberInput(attrs={'style': 'width: 600px;', 'class': 'form-control', 'id':'tontine', 'type':'hidden'}),
            'id_membre':forms.NumberInput(attrs={'style': 'width: 600px;', 'class': 'form-control', 'id':'membre', 'type':'hidden'}),
            'type_fond':forms.TextInput(attrs={'placeholder': 'Entrer le type du fond', 'style': 'width: 600px;', 'class': 'form-control'}),
            'nom_fond':forms.TextInput(attrs={'placeholder': 'Entrer le nom du fond', 'style': 'width: 600px;', 'class': 'form-control'}),
            'montant': forms.NumberInput(attrs={'placeholder': 'Entrer le montant du fond', 'style': 'width: 600px;', 'class': 'form-control'}),
            'objectif': forms.Textarea(attrs={'placeholder': 'Entrer l\'objectif', 'style': 'width: 600px;', 'class': 'form-control', 'rows':5, 'cols':10}),
        }

class PretForm(forms.ModelForm):

    class Meta:
        model = Pret
        fields = '__all__'
        widgets = {
            'id_tontine':forms.NumberInput(attrs={'style': 'width: 600px;', 'class': 'form-control', 'id':'tontine', 'type':'hidden'}),
            'id_membre':forms.NumberInput(attrs={'style': 'width: 600px;', 'class': 'form-control', 'id':'membre', 'type':'hidden'}),
            'nom_pret':forms.TextInput(attrs={'placeholder': 'Entrer le nom du pret', 'style': 'width: 600px;', 'class': 'form-control'}),
            'date_pret': forms.DateInput(attrs={'placeholder': 'jj/mm/aaaa', 'style': 'width: 600px;', 'class': 'form-control'}),
            'montant': forms.NumberInput(attrs={'placeholder': 'Entrer le montant du pret', 'style': 'width: 600px;', 'class': 'form-control'}),
            'date_remboursement': forms.DateInput(attrs={'placeholder': 'jj/mm/aaaa', 'style': 'width: 600px;', 'class': 'form-control'}),
            'interet': forms.NumberInput(attrs={'placeholder': '%', 'style': 'width: 600px;', 'class': 'form-control', 'type':'hidden'}),
            'sanction': forms.NumberInput(attrs={'placeholder': '%', 'style': 'width: 600px;', 'class': 'form-control', 'type':'hidden'}),
            'raison': forms.Textarea(attrs={'placeholder': 'Entrer la raison', 'style': 'width: 600px;', 'class': 'form-control', 'rows':5, 'cols':10}),
        }

class Pret2Form(forms.ModelForm):

    class Meta:
        model = Pret
        fields = ['date_remboursement']
        widgets = {
            'date_remboursement': forms.DateInput(attrs={'placeholder': 'jj/mm/aaaa', 'style': 'width: 600px;', 'class': 'form-control'}),
        }

class ReunionForm(forms.ModelForm):

    class Meta:
        model = Reunion
        fields = '__all__'
        widgets = {
            'id_tontine':forms.NumberInput(attrs={'style': 'width: 600px;', 'class': 'form-control', 'id':'tontine', 'type':'hidden'}),
            'date_reunion': forms.DateInput(attrs={'placeholder': 'jj/mm/aaaa', 'style': 'width: 600px;', 'class': 'form-control'}),
            'beneficiaire': forms.TextInput(attrs={'placeholder': 'Entrer le nom du beneficiaire', 'style': 'width: 600px;', 'class': 'form-control'}),
            'lieu': forms.TextInput(attrs={'placeholder': 'Entrer le lieu', 'style': 'width: 600px;', 'class': 'form-control'}),
            'heure': forms.TimeInput(attrs={'placeholder': 'hh:mm', 'style': 'width: 600px;', 'class': 'form-control'}),
            'regle': forms.Textarea(attrs={'placeholder': 'Entrer le(s) regle(s)', 'style': 'width: 600px;', 'class': 'form-control', 'rows':5, 'cols':10}),
            'motif': forms.TextInput(attrs={'placeholder': 'Entrer le motif', 'style': 'width: 600px;', 'class': 'form-control'}),
        }