from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    fio = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Email')
    comment = models.CharField(max_length=150, verbose_name='комментарий', **NULLABLE)

    # user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='владелец клиента')

    def __str__(self):
        return f'{self.fio}'

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Message(models.Model):
    theme = models.CharField(max_length=150, verbose_name='тема письма')
    body = models.TextField(verbose_name='содержание письма')

    # user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='владелец сообщения')

    def __str__(self):
        return f'{self.pk} {self.theme}'

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class SettingsMailing(models.Model):
    CHOICE_PERIOD = (
        ("daily", "ежедневно"),
         ("weekly", "еженедельно"),
          ("monthly", "раз в месяц"),
    )

    CHOICE_STATUS = (
        ("create", "создана"),
        ("start", "запущена"),
        ("completed", "завершена"),
    )

    name = models.CharField(max_length=150, verbose_name='название')

    clients = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиенты')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщения')

    start_time = models.DateTimeField(auto_now_add=True, verbose_name='время начала')
    end_time = models.DateTimeField(verbose_name='время окончания')
    period = models.CharField(choices=CHOICE_PERIOD, verbose_name='периодичность')
    status = models.CharField(choices=CHOICE_STATUS, verbose_name='статус рассылки')

    is_active = models.BooleanField(default=True, verbose_name='активность')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец рассылки')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Настройки рассылки"
        verbose_name_plural = "Настройки рассылок"


class LogsMailing(models.Model):
    date_time_last_attempt = models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки')
    is_status = models.BooleanField(default=True, verbose_name='статус попытки')
    answer_server = models.CharField(max_length=150, verbose_name='ответ почтового сервера', **NULLABLE)

    mailing = models.ForeignKey(SettingsMailing, on_delete=models.CASCADE, verbose_name='рассылка')

    def __str__(self):
        return f'{self.pk} {self.date_time_last_attempt}'

    class Meta:
        verbose_name = "Лог рассылки"
        verbose_name_plural = "Логи рассылки"
