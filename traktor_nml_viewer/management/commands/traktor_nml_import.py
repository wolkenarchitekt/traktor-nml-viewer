import datetime
import logging
from pathlib import Path

import django
from django.core.management.base import BaseCommand

from progress.bar import Bar
from traktor_nml_utils import TraktorCollection
from traktor_nml_viewer.models import Entry, NMLFile

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Import Traktor NML files"

    def add_arguments(self, parser: django.core.management.base.CommandParser):
        parser.add_argument("args", nargs="+")

    def handle(self, *args, **options):
        for arg in args:
            Entry.objects.all().delete()

            collection = TraktorCollection(path=Path(arg))
            bar = Bar("Processing", max=len(collection.nml.collection.entry))
            for nml_entry in collection.nml.collection.entry:
                db_entry = Entry()
                nml_file = NMLFile(file=Path(arg).name)
                nml_file.save()
                db_entry.nml_file = nml_file
                db_entry.artist = nml_entry.artist
                db_entry.title = nml_entry.title
                db_entry.audio_id = nml_entry.audio_id
                if nml_entry.tempo:
                    db_entry.bpm = int(nml_entry.tempo.bpm)
                db_entry.key = nml_entry.info.key
                db_entry.album = nml_entry.album.title
                db_entry.bitrate = nml_entry.info.bitrate
                db_entry.genre = nml_entry.info.genre
                db_entry.playtime = nml_entry.info.playtime_float
                db_entry.playcount = nml_entry.info.playcount
                if nml_entry.info.last_played:
                    db_entry.last_played = datetime.datetime.strptime(
                        nml_entry.info.last_played, "%Y/%m/%d"
                    )
                db_entry.ranking = nml_entry.info.ranking
                if nml_entry.modified_date:
                    db_entry.modified_date = datetime.datetime.strptime(
                        nml_entry.modified_date, "%Y/%m/%d"
                    )
                if nml_entry.info.release_date:
                    db_entry.release_date = datetime.datetime.strptime(
                        nml_entry.info.release_date, "%Y/%m/%d"
                    )
                if nml_entry.info.import_date:
                    db_entry.import_date = datetime.datetime.strptime(
                        nml_entry.info.import_date, "%Y/%m/%d"
                    )
                db_entry.file = nml_entry.location.dir + nml_entry.location.file
                db_entry.save()
                bar.next()
            bar.finish()
