from django.contrib import admin
from .models import Trip, Review, Request
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Trip)
class TripAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('name', 'destination', 'date_start', 'date_end', 'price')
    list_display = ('name', 'destination', 'date_start', 'date_end', 'price')
    search_fields = ['name', 'destination']
    summernote_fields = ('description')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('user', 'trip', 'rating', 'submitted_on')
    list_filter = ('user', 'trip', 'rating', 'submitted_on')
    search_fields = ['user', 'trip']


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):

    list_display = ('user', 'destination', 'submitted_on', 'approved')
    list_filter = ('user', 'submitted_on', 'approved')
    search_fields = ['user']
    actions = ['approve_request']

    def approve_request(self, request, queryset):
        queryset.update(approved=True)
