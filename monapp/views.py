# Create your views here.
from django.http import HttpResponseRedirect
from django.http import  HttpResponse
from django.shortcuts import render
from monapp.forms import ContactUsForm
from monapp.models import annotateur
from monapp.models import tweetForm
from . import forms
from .forms import annotationForm
from .forms import InscriptionAnnotateur

class annotateur():
    model = annotateur()

# Create your views here.
def login(request):
    return render(request,'login.html')
def contact(request):
    form = ContactUsForm()
    return render(request,
             'monapp\formulaire.formulaire.htmssl',
             {'form': form})

class tweetForm():
    model = tweetForm()



def acceuil(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
    """
def formulaire(request):

    context = {}
    registered = False
    if request.method == "POST":

        form = annotationForm(request.POST)
        if form.is_valid():
                LangueTweet = form.cleaned_data['LangueTweet']
                Polaritetweet = form.cleaned_data['Polaritetweet']
                Cout = form.cleaned_data['Cout']
                Nourriture = form.cleaned_data['Nourriture']        
                Parking = form.cleaned_data['Parking']
                Service = form.cleaned_data['Service']
                Hygiène = form.cleaned_data['Hygiène']
                Acceuil = form.cleaned_data['Acceuil']
                Internet = form.cleaned_data['Internet']
                formulaire = formulaire.objects.create(LangueTweet=LangueTweet, Polaritetweet=Polaritetweet, Cout=Cout, Nourriture=Nourriture,
                                                   Parking=Parking, Service=Service,Hygiène=Hygiène, Acceuil=Acceuil, Internet=Internet)
                formulaire.save()
                registered = True

          
        context['registered'] = registered
        context['form'] = form
        return render(request, 'formulaire.html', context)

    form = annotationForm()
    context['form'] = form
    return render(request, 'formulaire.html', context)   
     
    """
def formulaire(request):
    context = {}
    context['form']= annotationForm() 
    if request.method == "POST":
        form = annotationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'checkbox.html', context)
  
from django.shortcuts import render
from django.http import  HttpResponse
from .forms import Valueform

def form_view(request):
    context = {}
    context['form']= Valueform()
    if request.method == "POST":
        value = Valueform(request.POST)
        if value.is_valid():
            print("First Name: ",value.cleaned_data['first_name'])

    return  render(request,'Form_Handeling.html', context)
def inscriptions(request):

    context = {}
    registered = False
    if request.method == "POST":

        form = InscriptionAnnotateur(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']
            mail = form.cleaned_data['mail']
            user = User.objects.filter(username=username)
            if not user.exists():
                user = User.objects.create_user(
                    username, mail, password, is_active=False)
                nom = form.cleaned_data['nom']
                prenom = form.cleaned_data['prenom']
                dateNaissance = form.cleaned_data['dateNaissance']
                niveau = form.cleaned_data['niveau']
                etudiant = Etudiant.objects.create(nom=nom, prenom=prenom, dateNaissance=dateNaissance,
                                                   email=email, niveau=niveau)
                etudiant.save()
                registered = True

            else:

                if user.exists():
                    context['user_taken'] = True

                if password != re_password:
                    context['mdp'] = True

            context['registered'] = registered
            context['form'] = form
            return render(request, 'inscription.html', context)

    form = InscriptionAnnotateur()
    context['form'] = form
    return render(request, 'inscription.html', context)