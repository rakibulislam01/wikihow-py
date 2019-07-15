from django.contrib import admin
from .models import Content


class ContentAdmin(admin.ModelAdmin):
    list_display = ('url_text', 'url', 'scrape_time', 'time')
    search_fields = ['url_text']


admin.site.register(Content, ContentAdmin)
