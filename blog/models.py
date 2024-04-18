from django.db import models

from users.models import NULLABLE


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(verbose_name="Содержимое")
    image = models.ImageField(upload_to="photo/article", verbose_name="Превью", **NULLABLE)
    created_at = models.DateField(verbose_name="Дата создания")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    views_count = models.IntegerField(default=0, verbose_name="Просмотры")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
