from django.contrib import admin
from .models import User, Game, Guide

# Register your models here.

admin.site.register(User)
admin.site.register(Game)
admin.site.register(Guide)
