from django.contrib import admin

from traktor_nml_viewer.models import CollectionEntry


class EntryAdmin(admin.ModelAdmin):
    list_display = (
        "artist",
        "title",
        "key",
        "bpm",
        "import_date",
        "playcount",
        "last_played",
    )
    ordering = ("import_date",)


admin.site.site_header = "Traktor NML viewer"
# admin.site.register(NMLFile)
admin.site.register(CollectionEntry, EntryAdmin)
