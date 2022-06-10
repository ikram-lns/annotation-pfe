from django import forms
from monapp.choices import Type_Label_Tweet

class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)
Type_langue= (('1','français'),('2','english'),('3','العربية'),('4','dialect Algerien'))
Type_Label_Tweet= (('1','positif'), ('2','negatif'),('3','objectif'),('4','indecis'),('5','non mentionné'))
Type_niveau= (('1','primaire'), ('2','secondaire'),('3','moyen'), ('4','universitaire'))
class annotationForm(forms.Form):
   LangueTweet = forms.ChoiceField(choices=Type_langue, widget=forms.Select(attrs={'class': 'custom-select d-block w-100', 'required': 'required'}))
   Polaritetweet = forms.ChoiceField(choices= Type_Label_Tweet, widget=forms.Select(attrs={'class': 'custom-select d-block w-100', 'required': 'required'}))
   Cout = forms.ChoiceField(choices= Type_Label_Tweet, widget=forms.Select(attrs={'class': 'custom-select d-block w-100', 'required': 'required'}))
   Nourriture = forms.ChoiceField(choices= Type_Label_Tweet, widget=forms.Select(attrs={'class': 'custom-select d-block w-100', 'required': 'required'}))
   Parking = forms.ChoiceField(choices= Type_Label_Tweet, widget=forms.Select(attrs={'class': 'custom-select d-block w-100', 'required': 'required'}))
   Service = forms.ChoiceField(choices= Type_Label_Tweet, widget=forms.Select(attrs={'class': 'custom-select d-block w-100', 'required': 'required'}))
   Hygiène = forms.ChoiceField(choices=Type_Label_Tweet, widget=forms.Select(attrs={'class': 'custom-select d-block w-100', 'required': 'required'}))
   Acceuil = forms.ChoiceField(choices= Type_Label_Tweet, widget=forms.Select(attrs={'class': 'custom-select d-block w-100', 'required': 'required'}))
   Internet = forms.ChoiceField(choices= Type_Label_Tweet, widget=forms.Select(attrs={'class': 'custom-select d-block w-100', 'required': 'required'}))

class Valueform(forms.Form):
   first_name = forms.CharField(max_length = 100)
   department = forms.ChoiceField(choices = (('1','CSE'),('2','IT'),('3','ECE'),('4','EEE')))

class InscriptionAnnotateur(forms.Form):
    nom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': 'required'}))
    prenom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': 'required'}))
    dateNaissance = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'required': 'required'}))
    niveau =forms.ChoiceField(choices= Type_niveau,widget=forms.Select(attrs={'class': 'custom-select d-block w-100', 'required': 'required'}))
    mail = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'required': 'required'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'required': 'required'}))
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'required': 'required'}))