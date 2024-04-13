# Generated by Django 4.2.2 on 2024-04-13 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=150, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('comment', models.CharField(blank=True, max_length=150, null=True, verbose_name='комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=150, verbose_name='тема письма')),
                ('body', models.TextField(verbose_name='содержание письма')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='SettingsMailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='название')),
                ('start_time', models.DateTimeField(auto_now_add=True, verbose_name='время начала')),
                ('end_time', models.DateTimeField(verbose_name='время окончания')),
                ('period', models.CharField(choices=[('daily', 'ежедневно'), ('weekly', 'еженедельно'), ('monthly', 'раз в месяц')], verbose_name='периодичность')),
                ('status', models.CharField(choices=[('create', 'создана'), ('start', 'запущена'), ('completed', 'завершена')], verbose_name='статус рассылки')),
                ('is_active', models.BooleanField(default=True, verbose_name='активность')),
                ('clients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.client', verbose_name='клиенты')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.message', verbose_name='сообщения')),
            ],
            options={
                'verbose_name': 'Настройки рассылки',
                'verbose_name_plural': 'Настройки рассылок',
            },
        ),
        migrations.CreateModel(
            name='LogsMailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_last_attempt', models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки')),
                ('is_status', models.BooleanField(default=True, verbose_name='статус попытки')),
                ('answer_server', models.CharField(blank=True, max_length=150, null=True, verbose_name='ответ почтового сервера')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.settingsmailing', verbose_name='рассылка')),
            ],
            options={
                'verbose_name': 'Лог рассылки',
                'verbose_name_plural': 'Логи рассылки',
            },
        ),
    ]
