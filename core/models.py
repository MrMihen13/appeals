from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from markdown import markdown


USER = get_user_model()


class Appeal(models.Model):
    class PriorityTypes(models.TextChoices):
        HIGH = 'HG', _('Высокий')
        MEDIUM = 'MD', _('Средний')
        LOW = 'LW', _('Низкий')

    class GroupTypes(models.TextChoices):
        IT = 'IT', _('ИТ')
        DEV_OPS = 'DO', _('Автоматизация')
        SYS_ADMIN = 'SA', _('Системный администратор')

    class StatusTypes(models.TextChoices):
        CREATED = 'CR', _('Создано')
        IN_WORK = 'IW', _('В работе')
        DONE = 'DN', _('Выполнена')
        CLOSED = 'CL', _('Закрыта')

    title = models.CharField(verbose_name='Тема', max_length=128)

    owner = models.ForeignKey(USER, verbose_name='Пользователь', on_delete=models.CASCADE)

    group = models.CharField(verbose_name='Группа', max_length=2, choices=GroupTypes.choices, default=GroupTypes.IT)
    status = models.CharField(verbose_name='Статус', max_length=2, choices=StatusTypes.choices,
                              default=StatusTypes.CREATED)
    priority = models.CharField(verbose_name='Приоритет', max_length=2, choices=PriorityTypes.choices,
                                default=PriorityTypes.LOW)

    markdown_body = models.TextField()
    html_body = models.TextField(editable=False)

    image = ...

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.body = markdown(self.markdown_body)
        super().save(self, force_insert, force_update, using)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'