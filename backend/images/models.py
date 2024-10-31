from django.db import models


class Image(models.Model):
    title = models.CharField('Название', max_length=256)
    file_path = models.ImageField('Путь к фаилу', upload_to='images/')
    upload_date = models.DateTimeField('Дата загрузки', auto_now_add=True)
    resolution = models.CharField('Разрешение', max_length=50)
    size = models.PositiveIntegerField('Размер фаила')

    class Meta:
        verbose_name = 'Изображене'
        verbose_name_plural = 'Изображение'
        default_related_name = 'image'

    def __str__(self):
        return self.title
