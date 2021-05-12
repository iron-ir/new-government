from django.contrib import admin
from .models import *


@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    pass


@admin.register(RegisterCandidatePerElection)
class RegisterCandidatePerElectionAdmin(admin.ModelAdmin):
    pass


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    pass


@admin.register(CandidateGroup)
class CandidateGroupAdmin(admin.ModelAdmin):
    pass
