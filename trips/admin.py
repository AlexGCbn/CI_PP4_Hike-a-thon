from django.contrib import admin
from .models import Trip
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Trip)
class TripAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')
