from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, Job

# Register your models here.
class ProfileInLine(admin.StackedInline):
    """
    Permet d'ajouter les informations de Profile au
    panneau d'administration.
    """
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    """
    Ajoute le Profile d'un Utilisateur dans la panneau
    d'administration.
    """
    inlines = (ProfileInLine, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Job)