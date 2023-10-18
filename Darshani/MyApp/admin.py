from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import footballPlayer,footballPlayerAdmin
admin.site.register(footballPlayer,footballPlayerAdmin)