#!/usr/bin/env python3

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "insideoutside.settings")

import django
django.setup()

from observation.models import Observation
from tfuploader import upload_from_queryset
import datetime
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        zipname = sys.argv[1]
    else:
        zipname = "InsideOutside-%s" % (datetime.date.today())

    upload_from_queryset(
        Observation.objects.all(),
        name="%s.zip" % zipname,
        file_attr="photo",
        class_attr="export_category",
        size=299,
    )
