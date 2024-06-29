from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    description = models.TextField(**NULLABLE, verbose_name='Содержимое')
    image = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='Изображение')
    view_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return f"{self.title}, {self.description}"

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
