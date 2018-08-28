from django.contrib import admin
from musics.models import Music
# Register your models here.

# admin.site.register(Music)
# admin.site.register(Music, MusicAdmin)
@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('song', 'singer')
    list_filter = ('last_modify_date', 'created')
    search_fields = ('song', 'singer')

    # paginator
    list_per_page = 10
