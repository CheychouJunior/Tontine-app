from django.shortcuts import redirect ,render
from django.contrib.auth import authenticate,login
from tontine.form import *
from .models import *
from django.views.generic import ListView
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse

# Create your views here.


#la fonction qui va savoir ou nous envoyer a partir du login
def Login(request):
    error = ''
    a=""
    if request.method == 'POST':
        #on recupere le password et le username de lutilisateur
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:#si lutilisateur exist
            login(request,user)
            return redirect('/tontine/home')
                        
        else:
            error = "password or username incorect" 
               
    return render(request,'tontine/login.html',{'error':error})

def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tontine/login')
    return render(request,'tontine/register.html',{'form':form})        
#------------------------------------------------------------------------------
def home(request):
    user = request.user
    tontines = AppartenirTontine.objects.filter(id_membre=user.id_membre)
    print(tontines)
    context = {
        'tontines': tontines,
        'user': user
    }
    return render(request, 'tontine/home.html', context)   

def TontineCreate(request):
    form = RowTontineForm()
    user = request.user
    if request.method == 'POST':
        form = RowTontineForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            new = Tontine.objects.create(**form.cleaned_data)
            new.save()
            
            appartenir = AppartenirTontine(id_membre=user, id_tontine=new, statut='', nbr_parts=1)
            appartenir.save()
            #puisque quand quelqu'un cree une tontine, il en fait directement parti

            messages.success(request, f'La tontine a bien ete cree')
            return redirect('/tontine/home')
        else:
            form = RowTontineForm(request.POST)
    return render(request, 'tontine/create.html', {'form':form, 'user':user})


def TontineDetails(request, pk):
    user = request.user
    app_tontine = AppartenirTontine.objects.filter(id_tontine = pk)
    
    elt = iter(app_tontine)
    elt = elt.__next__()
    
    return render(request, 'tontine/tontine.html', {'app_tontine':app_tontine, 'user':user, 'elt':elt})

def TontineDelete(request, pk):
    item = Tontine.objects.get(id_tontine=pk)
    item.delete()
    messages.success(request, f'La tontine a bien ete supprime')
    return redirect('/tontine/home')

def TontineModify(request, pk):
    obj = Tontine.objects.get(id_tontine=pk)

    form = RowTontineForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        messages.success(request, f'La modification a ete effectue')
        return redirect('/tontine/home')

    return render(request, 'tontine/update_tontine.html', {'form':form})

def AjouterMembre(request, pk):
    test = Tontine.objects.get(id_tontine=pk)
 
    form = AppartenirTontineForm()
    
    if request.method == 'POST':
        form = AppartenirTontineForm(request.POST)
        if form.is_valid():
            new = AppartenirTontine.objects.create(**form.cleaned_data)
            new.save()

            messages.success(request, f'Le membre a bien été ajouté')
            #return redirect('/tontine/tontine/', kwargs={'pk':pk })
            return redirect('/tontine/home' )
        else:
            form = AppartenirTontineForm(request.POST)
    return render(request, 'tontine/ajouter_membre.html', {'form':form, 'test':test})

class TontineSearch(ListView):
    model = Tontine
    template_name = 'tontine/search_tontine.html'
    context_object_name = 'tontines'

    def get_queryset(self):
        query = self.request.GET.get('query_tontine')
        tontines=Tontine.objects.filter(Q(nom__icontains=query))
        return tontines

def MemberModify(request):
    user = request.user
    obj = Membre.objects.get(id_membre=user.id_membre)

    form = UserForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        messages.success(request, f'La modification a ete effectue')
        return redirect('/tontine/login')

    return render(request, 'tontine/update_membre.html', {'form':form})

#-----------------------------------------------------------------------------------------
def CotisationCreate(request, pk):
    form = CotisationForm()
    elt_tontine = Tontine.objects.get(id_tontine=pk)
    
    if request.method == 'POST':
        form = CotisationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            new = Cotisation.objects.create(**form.cleaned_data)
            new.save()

            messages.success(request, f'La cotisation a bien été crée')
            return redirect('/tontine/home')
        else:
            form = CotisationForm(request.POST)
    return render(request, 'tontine/create_cotisation.html', {'form':form, 'elt_tontine':elt_tontine})


def CotisationDetails(request, pk):
    cotisations = Cotisation.objects.filter(id_tontine = pk)
    
    return render(request, 'tontine/cotisation.html', {'cotisations':cotisations})    


def CotisationAffiche(request, pk):
    user = request.user
    cotises = Cotiser.objects.filter(id_cotisation = pk)
    cotis = Cotisation.objects.get(id_cotisation = pk)
    
    
    return render(request, 'tontine/cotiser.html', {'cotises':cotises, 'user':user, 'cotis':cotis})


def CotisationContribuer(request, pk):
    user = request.user
    obj = Cotisation.objects.get(id_cotisation=pk)
    elt = Cotiser(id_membre = user, id_cotisation = obj)
    elt.save()
    return redirect('/tontine/home')

def CotisationSuspendre(request, pk):
    item = Cotisation.objects.get(id_cotisation=pk)
    item.delete()
    messages.success(request, f'La cotisation a bien été supprimé')
    return redirect('/tontine/home')   
#-----------------------------------------------------------------------------------------------------

def FondAffiche(request, pk):
    fonds = Fond.objects.filter(id_tontine = pk)
    elt_tontine = Tontine.objects.get(id_tontine=pk)
    elt_fond = fonds.first()
    user = request.user
    
    return render(request, 'tontine/fond.html', {'fonds':fonds, 'elt_tontine':elt_tontine, 'elt_fond':elt_fond, 'user':user}) 

def FondCreate(request, pk):
    form = FondForm()
    elt_tontine = Tontine.objects.get(id_tontine=pk)
    user = request.user
    if request.method == 'POST':
        form = FondForm(request.POST)
        if form.is_valid():
            new = Fond.objects.create(**form.cleaned_data)
            new.save()

            messages.success(request, f'La tontine a bien ete cree')
            return redirect('/tontine/home')
        else:
            form = FondForm(request.POST)
    return render(request, 'tontine/create_fond.html', {'form':form, 'user':user, 'elt_tontine':elt_tontine})

def FondParticipant(request, pk):
    user = request.user
    fonds = ContribuerFond.objects.filter(id_fond = pk)
    elt_tontine = Fond.objects.filter(id_fond = pk).first()
    c_fond = ContribuerFond.objects.filter(id_fond = pk, id_membre = user.id_membre)

    return render(request, 'tontine/afficher_fond.html', {'fonds':fonds, 'user':user, 'elt_tontine':elt_tontine, 'c_fond':c_fond})


def FondContribuer(request, pk):
    user = request.user
    obj = Fond.objects.get(id_fond=pk)
    elt = ContribuerFond(id_fond = obj, id_membre = user)
    elt.save()
    return redirect('/tontine/home')


def FondModify(request, pk):
    obj = Fond.objects.get(id_fond=pk)

    form = FondForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        messages.success(request, f'La modification a ete effectue')
        return redirect('/tontine/home')

    return render(request, 'tontine/update_fond.html', {'form':form})


def FondDelete(request, pk):
    item = Fond.objects.get(id_fond=pk)
    item.delete()
    messages.success(request, f'Le fond a bien été supprimé')
    return redirect('/tontine/home')  
#---------------------------------------------------------------------------------------------------

def PretAffiche(request, pk):
    user = request.user
    prets = Pret.objects.filter(id_tontine = pk, id_membre = user.id_membre)
    elt_tontine = Tontine.objects.get(id_tontine = pk)
    
    return render(request, 'tontine/pret.html', {'prets':prets, 'elt_tontine':elt_tontine}) 

def PretCreate(request, pk):
    form = PretForm()
    user = request.user
    elt_tontine = Tontine.objects.get(id_tontine=pk)
    
    if request.method == 'POST':
        form = PretForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            new = Pret.objects.create(**form.cleaned_data)
            new.save()

            messages.success(request, f'La tontine a bien ete cree')
            return redirect('/tontine/home')
        else:
            form = PretForm(request.POST)
    return render(request, 'tontine/create_pret.html', {'form':form, 'user':user, 'elt_tontine':elt_tontine})


def PretDetails(request, pk):
    user = request.user
    pret = Pret.objects.get(id_pret = pk)
    montant_r = pret.montant+((pret.montant*pret.interet)/100)
    r_pret = Rembourserpret.objects.filter(id_pret = pk, id_membre = user.id_membre)

    return render(request, 'tontine/pret_details.html', {'pret':pret, 'user':user, 'r_pret':r_pret, 'montant_r': montant_r})

def PretRembourser(request, pk):
    user = request.user
    obj = Pret.objects.get(id_pret=pk)
    elt = Rembourserpret(id_pret = obj, id_membre = user, montant = obj.montant+((obj.montant*obj.interet)/100))
    elt.save()
    return redirect('/tontine/home')

def PretReporter(request, pk):
    obj = Pret.objects.get(id_pret=pk)

    form = Pret2Form(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        messages.success(request, f'La date a bien été reporté')
        return redirect('/tontine/home')

    return render(request, 'tontine/reporter_pret.html', {'form':form})

#-------------------------------------------------------------------------------------------------------------------------------

def Statistique(request, pk):
    ls_fond = Fond.objects.filter(id_tontine = pk)
    fonds = ContribuerFond.objects.all()
    ls_cotisation = Cotisation.objects.filter(id_tontine = pk)
    cotisations = Cotiser.objects.all()
    ls_pret = Pret.objects.filter(id_tontine = pk)
    prets = Rembourserpret.objects.all()

    return render(request, 'tontine/rapport.html', {'ls_fond':ls_fond, 'fonds':fonds, 'ls_cotisation':ls_cotisation, 'cotisations':cotisations, 'ls_pret':ls_pret, 'prets':prets}) 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ReunionAffiche(request, pk):
    user = request.user
    reunions = Reunion.objects.filter(id_tontine = pk)
    elt_tontine = Tontine.objects.get(id_tontine = pk)
    
    return render(request, 'tontine/reunion.html', {'reunions':reunions, 'elt_tontine':elt_tontine}) 


def ReunionCreate(request, pk):
    form = ReunionForm()
    user = request.user
    elt_tontine = Tontine.objects.get(id_tontine=pk)
    
    if request.method == 'POST':
        form = ReunionForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            new = Reunion.objects.create(**form.cleaned_data)
            new.save()

            messages.success(request, f'La reunion a bien ete cree')
            return redirect('/tontine/home')
        else:
            form = ReunionForm(request.POST)
    return render(request, 'tontine/create_reunion.html', {'form':form, 'user':user, 'elt_tontine':elt_tontine})


def ReunionDetails(request, pk):
    user = request.user
    elt_reunion = Reunion.objects.get(id_reunion = pk)
    reunions = ListePresence.objects.filter(id_reunion = pk)
    s_reunion = ListePresence.objects.filter(id_reunion = pk, id_membre = user.id_membre)

    return render(request, 'tontine/reunion_details.html', {'reunions':reunions, 'user':user, 's_reunion':s_reunion, 'elt_reunion':elt_reunion})


def ReunionSigner(request, pk):
    user = request.user
    obj = Reunion.objects.get(id_reunion=pk)
    elt = ListePresence(id_reunion = obj, id_membre = user)
    elt.save()
    return redirect('/tontine/home')

    

""" def MembreSearch(request):
    query = request.Get.get('query_membre')
    membre = Membre.objects.filter(username__contains=query)
    app_tontine = AppartenirTontine.objects.filter()

class MembreSearch(ListView):
    model = AppartenirTontine
    template_name = 'tontine/search_membre.html'
    context_object_name = 'membres'

    def get_queryset(self):
        query = self.request.GET.get('query_membre')

        membres = AppartenirTontine.objects.filter(Tontine__author__contains=query)
        return membres """


""" def structure(request):
    return render(request,'structure.html')

def actifs_f(request):
    return render(request,'actifs_f.html')
    
def candidat_s(request):
    return render(request,'candidat_s.html')

def home(request):
    return render(request,'home.html')

def election_s(request):
    return render(request,'election_s.html') 

def finance(request):
    return render(request,'finance.html') 

def fonds_f(request):
    return render(request,'fonds_f.html') 

def membre_s(request):
    return render(request,'membre_s.html') 

def pret_f(request):
    return render(request,'pret_f.html') 

def rapport(request):
    return render(request,'rapport.html') 

def reunion_s(request):
    return render(request,'reunion_s.html') 

def tontine_s(request):
    return render(request,'tontine_s.html') 

def cotisation_f(request):
    return render(request,'cotisation_f.html')     



def tontine(request):
    context = {
        'tontines': Tontine.objects.all()
    }
    return render(request, 'tontine/gestion_de_la_tontine.html', context)






class TontineSearch(ListView):
    model = Tontine
    template_name = 'tontine/search_tontine.html'
    context_object_name = 'tontines'

    def get_queryset(self):
        query = self.request.GET.get('query')
        tontines=Tontine.objects.filter(Q(nom__icontains=query))
        return tontines




#----------------------------------------- Membre ----------------------------------------------------------------

def MemberModify(request):
    user = request.user
    obj = Membre.objects.get(id_membre=user.id_membre)

    form = UserForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        messages.success(request, f'La modification a ete effectue')
        return redirect('membre_s')

    return render(request, 'membre/update.html', {'form':form})
    

class MembreSearch(ListView):
    model = Membre
    template_name = 'membre/search_membre.html'
    context_object_name = 'membres'

    def get_queryset(self):
        query = self.request.GET.get('search')
        membres = Membre.objects.filter(Q(username__icontains=query))
        return membres


def SearchPage(request):
    return render(request,'membre/search_page.html')  """