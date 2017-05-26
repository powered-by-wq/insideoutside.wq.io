from django.contrib.gis.db import models


class Observation(models.Model):
    date = models.DateField(
        verbose_name="Date",
    )
    photo = models.ImageField(
        upload_to="observations",
        verbose_name="Photo",
    )
    category = models.ForeignKey(
        'category.Category',
        verbose_name="Category",
    )
    toggle = models.CharField(
        choices=(
            ("gps", "Use GPS"),
            ("interactive", "Point on Map"),
            ("manual", "Enter Manually"),
        ),
        max_length=11,
        null=True,
        blank=True,
        verbose_name="Location Mode",
    )
    geometry = models.PointField(
        srid=4326,
        null=True,
        blank=True,
        verbose_name="Location",
    )
    latitude = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Latitude",
    )
    longitude = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Longitude",
    )
    accuracy = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Accuracy",
    )
    notes = models.TextField(
        null=True,
        blank=True,
        verbose_name="Notes",
    )

    wq_label_template = "{{category_id}} on {{date}}"

    def __str__(self):
        if not self.category:
            return "New Observation"
        return "%s on %s" % (self.category, self.date)

    class Meta:
        verbose_name = "observation"
        verbose_name_plural = "observations"
        ordering = ('-pk',)
