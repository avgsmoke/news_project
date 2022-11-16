from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=256)
    content = models.TextField(verbose_name='Контент')
    image = models.ImageField(verbose_name='Изображение', upload_to='news/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comments(models.Model):
    class Status(models.TextChoices):
        ZERO = '0', 'Заблокирован',
        FIRST = '1', 'Опубликован',
        TWO = '2', 'Ожидает проверки'

    news = models.ForeignKey(News, verbose_name='Новость', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Комментарий')
    status = models.CharField(verbose_name='Статус', max_length=1, choices=Status.choices, default=Status.TWO)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Favorite(models.Model):
    news = models.ForeignKey(News, verbose_name='Новость', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'


class Mail(models.Model):
    theme = models.CharField(verbose_name='Тема письма', max_length=256)
    email = models.EmailField(verbose_name='Email')
    text = models.TextField(verbose_name='текст')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.theme

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Почта'
        verbose_name_plural = 'Почта'
