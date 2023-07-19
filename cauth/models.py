from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from cauth.manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email', db_index=True, unique=True)

    last_name = models.CharField(verbose_name='Фамилия', max_length=128, null=True)
    first_name = models.CharField(verbose_name='Имя', max_length=128, null=True)
    middle_name = models.CharField(verbose_name='Отчество', max_length=128, null=True)

    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    is_staff = models.BooleanField(verbose_name='Is Staff', default=False)
    created_at = models.DateTimeField(verbose_name='Created t', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Update at', auto_now=True)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
