from django.db import models


class NMLFile(models.Model):
    file = models.TextField()

    class Meta:
        db_table = "nmlfile"


class Entry(models.Model):
    album = models.TextField(null=True)
    artist = models.TextField(null=True)
    audio_id = models.TextField(null=True)
    bitrate = models.IntegerField(null=True)
    bpm = models.IntegerField(null=True)
    file = models.TextField(null=True)
    import_date = models.DateField(null=True)
    key = models.TextField(null=True)
    last_played = models.DateField(null=True)
    modified_date = models.DateField(null=True)
    nml_file = models.ForeignKey(NMLFile, on_delete=models.CASCADE)
    playcount = models.IntegerField(null=True)
    playtime = models.FloatField(null=True)
    ranking = models.IntegerField(null=True)
    release_date = models.DateField(null=True)
    genre = models.TextField(null=True)
    title = models.TextField(null=True)

    class Meta:
        db_table = "entry"

    def __str__(self):
        return f"{self.artist} - {self.title}"
