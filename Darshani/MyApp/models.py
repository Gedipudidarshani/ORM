from django.db import models

# Create your models here.
from django.db import models
from django.contrib import admin
class footballPlayer(models.Model):
	name=models.CharField(max_length=30)
	age=models.IntegerField()
	goals=models.IntegerField()
	jerseynumber=models.IntegerField()
	team=models.CharField(max_length=25)
	NumberofMatches=models.IntegerField()
class footballPlayerAdmin(admin.ModelAdmin):
	list_display=["name","age","goals","jerseynumber","team","NumberofMatches"]