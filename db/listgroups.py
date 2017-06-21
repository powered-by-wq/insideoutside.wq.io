#!/usr/bin/env python3

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "insideoutside.settings")

import django
django.setup()

from observation.models import Observation
from tfuploader import list_groups_from_queryset


if __name__ == "__main__":
    list_groups_from_queryset(
        Observation.objects.all(),
        file_attr="photo",
        class_attr="export_category",
    )
