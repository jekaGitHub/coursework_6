from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    fio = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Email')
    comment = models.CharField(max_length=150, verbose_name='Комментарий', **NULLABLE)

    # user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='владелец клиента')


class Message(models.Model):
    theme = models.CharField(max_length=150, verbose_name='тема письма')
    body = models.TextField(verbose_name='содержание письма')

    # user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='владелец сообщения')


class SettingsMailing(models.Model):
    CHOICE_PERIOD = {
         'daily': 'ежедневно',
         'weekly': 'еженедельно',
         'monthly': 'раз в месяц'
    }

    CHOICE_STATUS = {
         'create': 'создана',
         'start': 'запущена',
         'completed': 'завершена'
    }

    name = models.CharField(max_length=150, verbose_name='название')

    clients = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиенты')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщения')

    start_time = models.DateTimeField(auto_now_add=True, verbose_name='время начала')
    end_time = models.DateTimeField(verbose_name='время окончания')
    period = models.CharField(choices=CHOICE_PERIOD, verbose_name='периодичность')
    status = models.CharField(choices=CHOICE_STATUS, verbose_name='статус рассылки')

    is_active = models.BooleanField(default=True, verbose_name='активность')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец рассылки')


class LogsMailing(models.Model):
    pass
