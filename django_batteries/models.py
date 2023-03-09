from django.db import models
from django.utils.translation import gettext_lazy as _

from django_batteries.fields import AutoCreatedField, AutoLastModifiedField


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """

    created = AutoCreatedField(_("created"))
    modified = AutoLastModifiedField(_("modified"))

    def save(self, *args, **kwargs):
        """
        Overriding the save method in order to make sure that
        modified field is updated even if it is not given as
        a parameter to the update field argument.
        """
        update_fields = kwargs.get("update_fields", None)
        if update_fields:
            kwargs["update_fields"] = set(update_fields).union({"modified"})

        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class TimeFramedModel(models.Model):
    """
    An abstract base class model that provides ``start``
    and ``end`` fields to record a timeframe.
    """

    start = models.DateTimeField(_("start"), null=True, blank=True)
    end = models.DateTimeField(_("end"), null=True, blank=True)

    class Meta:
        abstract = True


class DescriptionModel(models.Model):
    description = models.TextField(_("description"), null=True, blank=True)

    class Meta:
        abstract = True


class TitleModel(models.Model):
    """Title

    Model with extra ``title`` field

    """

    title = models.Charfield(max_length=50)

    class Meta:
        abstract = True


class TitleDescriptionModel(TitleModel, DescriptionModel):
    """TitleDescriptionModel

    This models contains:

    ``title`` and ``description`` field to use in your models

    """

    class Meta:
        abstract = True
