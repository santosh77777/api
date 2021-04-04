from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

REPEAT = (
    ('None', 'None'),
    ('Daily', 'Daily'),
    ('Weekly', 'Weekly'),
    )

SHIFT = (
    ('Morning Shift - 5am t0 9am', 'Morning Shift - 5am t0 9am'),
       )


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Shift(models.Model):
    user = models.ForeignKey(User, related_name='shifts', on_delete=models.CASCADE)
    start_date = models.DateField()
    select_repeat_type = models.CharField(max_length=200, null=True, choices=REPEAT)
    select_shift_type = models.CharField(max_length=200, null=True, choices=SHIFT)
    select_start_time  = models.TimeField()
    select_end_time  = models.TimeField()

    class Meta:
        unique_together = ['user', 'start_date', 'select_repeat_type']


    def __str__(self):
        return '%s: %s: %s: %s: %s' % (self.start_date, self.select_repeat_type, self.select_shift_type, self.select_start_time, self.select_end_time)
