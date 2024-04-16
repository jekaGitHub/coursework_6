# Generated by Django 4.2.2 on 2024-04-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0003_remove_settingsmailing_clients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingsmailing',
            name='period',
            field=models.CharField(choices=[('daily', 'ежедневно'), ('weekly', 'еженедельно'), ('monthly', 'раз в месяц')], default='daily', verbose_name='периодичность'),
        ),
        migrations.AlterField(
            model_name='settingsmailing',
            name='status',
            field=models.CharField(choices=[('create', 'создана'), ('start', 'запущена'), ('completed', 'завершена')], default='create', verbose_name='статус рассылки'),
        ),
    ]
