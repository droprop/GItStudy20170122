from django.contrib import admin

from botTest.models import Talk
# Register your models here.


class TalkAdmin (admin.ModelAdmin):
    list_display = ('id', 'name', 'content', 'weight',)
    list_display_links = ('id',)
admin.site.register(Talk, TalkAdmin)
