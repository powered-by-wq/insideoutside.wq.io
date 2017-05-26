from django.db import models


class Category(models.Model):
    name = models.TextField(
        null=True,
        blank=True,
        verbose_name="Name",
    )
    photo = models.ImageField(
        upload_to="categorys",
        null=True,
        blank=True,
        verbose_name="Photo",
    )
    link = models.TextField(
        null=True,
        blank=True,
        verbose_name="Wikipedia Link",
    )

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categorys"
