from django.contrib import admin
from .models import *
import sys

@admin.register(visitor)
class VisitorAdmin(admin.ModelAdmin):
    search_fields = ['path', 'method', 'scheme', 'headers', 'body', 'user', 'info', 'COOKIES', 'METAdata', 'time',]
    list_filter = ('path', 'method', 'scheme', 'body', 'user', 'info', 'time',)
    list_display = ('path', 'method', 'scheme', 'body', 'user', 'info', 'time',)
    readonly_fields = ['path', 'method', 'scheme', 'headers', 'body', 'user', 'info', 'COOKIES', 'METAdata', 'time',]
    list_per_page = sys.maxsize

    def has_add_permission(self, request):
        return False
