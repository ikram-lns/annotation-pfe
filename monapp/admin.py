
# Register your models here.
from django.contrib import admin
from django.forms import *
from django.db.models import *
from monapp.models import annotateur, tweetForm, attribute

admin.site.register(annotateur)
admin.site.register(tweetForm)
admin.site.register(attribute)
