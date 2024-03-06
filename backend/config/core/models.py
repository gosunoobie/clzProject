from django.core.cache import cache
from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _
from .managers import SoftDeleteManager
from django.utils import timezone


class TimeStampedModel(models.Model):
    """
    Abstract model for adding timestamps.
    """

    date_created = models.DateTimeField(
        _("created date"), auto_now_add=True, null=True, blank=True
    )
    date_modified = models.DateTimeField(
        _("modified date"), auto_now=True, null=True, blank=True
    )

    class Meta:
        abstract = True


class SingletonModel(models.Model):
    """Singleton Django Model"""

    class Meta:
        abstract = True

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    def save(self, *args, **kwargs):
        """
        Save object to the database. Removes all other entries if there
        are any.
        """
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)
        self.set_cache()

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def flush_cache(cls):
        cache.delete(cls.__name__)

    @classmethod
    def load(cls):
        """
        Load object from the database. Failing that, create a new empty
        (default) instance of the object and return it (without saving it
        to the database).
        """
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)


class SoftDeleteModel(models.Model):
    """
    Abstract model to handle soft deletion of data.
    """

    is_deleted = models.BooleanField(_("is deleted"), default=False)
    deleted_date = models.DateTimeField(_("deleted date"), null=True, blank=True)

    objects = SoftDeleteManager()

    class Meta:
        abstract = True

    def soft_delete(self, *args, **kwargs):
        """
        Soft delete the model instance.
        """
        if not self.is_deleted:

            self.is_deleted = True
            self.deleted_date = timezone.now()
            return super().save(*args, **kwargs)

    def restore(self, *args, **kwargs):
        """
        Restore(Undelete) only soft deleted instance.
        """
        if self.is_deleted:
            self.is_deleted = False
            self.deleted_date = None
            return super().save(*args, **kwargs)


class BaseModel(TimeStampedModel, SoftDeleteModel):
    """
    Abstract model to inherit default models.
    """

    class Meta:
        abstract = True


class SMTP(SingletonModel):
    host = models.TextField(verbose_name=_("host"), help_text=_("Host url of smtp"))
    host_user = models.EmailField(
        verbose_name=_("host user"), help_text=_("Email address/host user of smtp")
    )
    host_pass = models.TextField(
        verbose_name=_("host password"), help_text=_("Password of smtp")
    )
    host_port = models.IntegerField(
        verbose_name=_("host port"), help_text=_("Host port of smtp"), default=587
    )
    use_tls = models.BooleanField(
        verbose_name=_("use tls"),
        help_text=_("Should tls be used for smtp"),
        default=True,
    )

    def __str__(self) -> str:
        return self.host_user

    @classmethod
    def load(cls):
        """
        Load object from the database. Failing that, create a new empty
        (default) instance of the object and return it (without saving it
        to the database).
        """
        use_tls = settings.EMAIL_USE_TLS
        host = settings.EMAIL_HOST
        host_user = settings.EMAIL_HOST_USER
        host_pass = settings.EMAIL_HOST_PASSWORD
        host_port = settings.EMAIL_PORT
        if cache.get(cls.__name__) is None:
            try:
                obj = cls.objects.get(pk=1)
            except:
                obj = cls.objects.create(
                    host=host,
                    host_user=host_user,
                    host_pass=host_pass,
                    host_port=host_port,
                    use_tls=use_tls,
                )
            obj.set_cache()
        return cache.get(cls.__name__)

    class Meta:
        verbose_name = "SMTP Setting"




class Bank(models.Model):
    name = models.CharField(max_length=300)
    head_office = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
