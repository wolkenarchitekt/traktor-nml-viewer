from django.contrib import admin

from traktor_nml_viewer.models import Entry


class EntryAdmin(admin.ModelAdmin):
    # list_display = (
    #     "artist",
    #     "title",
    #     "import_date",
    #     "file",
    #     "playcount",
    #     "last_played",
    # )
    list_display = [
        field.name
        for field in Entry._meta.get_fields()
        if field.name not in ["audio_id"]
    ]
    ordering = ("import_date",)


admin.site.site_header = "Traktor NML viewer"
# admin.site.register(NMLFile)
admin.site.register(Entry, EntryAdmin)
