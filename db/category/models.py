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
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Description",
    )
    order = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Order",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ('order', 'name',)
