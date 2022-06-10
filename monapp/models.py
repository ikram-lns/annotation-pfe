from django.db import models
from django import forms
from monapp.choices import Type_Label_Tweet
from monapp.choices import Type_Label_Entity

Type_langue= (('1','français'),('2','english'),('3','العربية'),('4','dialect Algerien'))
Type_Label_Tweet= (('1','positif'), ('2','negatif'),('3','objectif'),('4','indecis'),('5','non mentionné'))

# Create your models here.
class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)
   
class annotateur(models.Model):
   id = models.AutoField( primary_key=True)
   nom = models.fields.CharField(max_length=25)
   prenom = models.fields.CharField(max_length=25)
   email = models.fields.CharField(max_length=50)
   password = models.fields.CharField(max_length=30)
   fonction = models.fields.CharField(max_length=30)
   

class tweetForm(models.Model):
   def select_random_tweet():
      selection = random.choice(tweet)
      return selection if selection else select_random_tweet()
""" LangueTweet = models.CharField(max_length=1, choices=Type_langue,blank=True,null=True)
   Polarite = models.CharField(max_length=1, choices=Type_Label_Tweet,blank=True,null=True)
   Cout = models.CharField(max_length=1, choices=Type_Label_Tweet,blank=True,null=True)
   Nourriture = models.CharField(max_length=1, choices=Type_Label_Tweet,blank=True,null=True)
   Parking = models.CharField(max_length=1, choices=Type_Label_Tweet,blank=True,null=True)
   Service = models.CharField(max_length=1, choices=Type_Label_Tweet,blank=True,null=True)
   Hygiène = models.CharField(max_length=1, choices=Type_Label_Tweet,blank=True,null=True)
   Acceuil = models.CharField(max_length=1, choices=Type_Label_Tweet,blank=True,null=True)
   Internet = models.CharField(max_length=1, choices=Type_Label_Tweet,blank=True,null=True)  """

class attribute(models.Model):
   nom_attribut = models.fields.CharField(max_length=15)
   etiquette_attribut = Type_Label_Entity

