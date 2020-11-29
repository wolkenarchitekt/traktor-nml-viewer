import datetime
import logging
from pathlib import Path

import django
from django.core.management.base import BaseCommand

from progress.bar import Bar
from traktor_nml_utils import TraktorCollection, TraktorHistory, is_history_file
from traktor_nml_viewer.models import Entry, NMLFile

logger = logging.getLogger(__name__)


def import_nml(path: Path):
    print(f"parsing file: {path.name}")
    if is_history_file(path):
        history = TraktorHistory(path=path)
        from ipdb import set_trace
        set_trace()
    else:
        collection = TraktorCollection(path=path)
        bar = Bar(
            f"Processing file: {path.name}", max=len(collection.nml.collection.entry)
        )

        for nml_entry in collection.nml.collection.entry:
            db_entry = Entry()
            nml_file = NMLFile(file=path.name)
            nml_file.save()
            db_entry.nml_file = nml_file
            db_entry.artist = nml_entry.artist
            db_entry.title = nml_entry.title
            db_entry.audio_id = nml_entry.audio_id
            if nml_entry.tempo and nml_entry.tempo.bpm:
                db_entry.bpm = int(nml_entry.tempo.bpm)
            if nml_entry.album:
                db_entry.album = nml_entry.album.title
            if nml_entry.modified_date:
                db_entry.modified_date = datetime.datetime.strptime(
                    nml_entry.modified_date, "%Y/%m/%d"
                )
            if nml_entry.info:
                db_entry.ranking = nml_entry.info.ranking
                db_entry.bitrate = nml_entry.info.bitrate
                db_entry.genre = nml_entry.info.genre
                db_entry.playtime = nml_entry.info.playtime_float
                db_entry.playcount = nml_entry.info.playcount
                db_entry.comment = nml_entry.info.comment
                db_entry.comment2 = nml_entry.info.rating
                if nml_entry.info.last_played:
                    db_entry.last_played = datetime.datetime.strptime(
                        nml_entry.info.last_played, "%Y/%m/%d"
                    )
                db_entry.key = nml_entry.info.key
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


class Command(BaseCommand):
    help = "Import Traktor NML files"

    def add_arguments(self, parser: django.core.management.base.CommandParser):
        parser.add_argument("args", nargs="+")

    def handle(self, *args, **options):
        for arg in args:
            p = Path(arg)
            if p.is_dir():
                for nml_file in p.glob("**/*.nml"):
                    import_nml(path=nml_file)
            else:
                import_nml(path=p)
