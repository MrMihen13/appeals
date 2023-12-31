# Generated by Django 4.2.3 on 2023-07-19 04:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Тема')),
                ('auditorium', models.CharField(max_length=4, verbose_name='Аудитория')),
                ('group', models.CharField(choices=[('IT', 'ИТ'), ('DO', 'Автоматизация'), ('SA', 'Системный администратор')], default='IT', max_length=2, verbose_name='Группа')),
                ('status', models.CharField(choices=[('CR', 'Создано'), ('IW', 'В работе'), ('DN', 'Выполнена'), ('CL', 'Закрыта')], default='CR', max_length=2, verbose_name='Статус')),
                ('priority', models.CharField(choices=[('HG', 'Высокий'), ('MD', 'Средний'), ('LW', 'Низкий')], default='LW', max_length=2, verbose_name='Приоритет')),
                ('markdown_body', models.TextField()),
                ('html_body', models.TextField(editable=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Обращение',
                'verbose_name_plural': 'Обращения',
            },
        ),
    ]
