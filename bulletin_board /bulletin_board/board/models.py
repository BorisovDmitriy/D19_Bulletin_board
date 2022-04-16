from django.db import models
from django.contrib.auth.models import User


# Модель Author (Автор)
# Модель содержащая всех пользователей
# имеет поле:
# user- связь один к одному с пользователем User,
# для создания пользователя при регистрации
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'{self.user.username}'


# Модель Category (категория)
# имеет поле:
# name - Название категорий для объявлений
class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# Модель ads(объявления)
# Модель содержащая все созданные объявления
# Она имеет поля:
# author-пользователь который создал объявления
# article-заголовок
# create_time-время создания объявления
# categories-категория (связь многие со многим)
# text_ads-текст объявления
class Ad(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='ads', verbose_name='Пользователь')
    article = models.CharField(max_length=255, verbose_name='Заголовок')
    create_time = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='AdsCategory', verbose_name='Категория')
    text_ad = models.TextField(null=False, verbose_name='Текст объявления')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def preview(self):
        # возвращает начало статьи, длиной в 124 символа и добавляет многоточие
        size = 124 if len(self.text_ad) > 124 else len(self.text_ad)
        return self.text_ad[:size] + "..."

    def get_absolute_url(self):
        return f'/board/{self.id}'


# Модель Response (Отклик)
# ads - Привязка отклика к объявлению
# user- пользователь который создал отклик
# create_time - время создания отклика
# text_response - текст отклика
class Response(models.Model):
    ads = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='responses', verbose_name='Объявление')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='responses', verbose_name='Пользователь')
    create_time = models.DateTimeField(auto_now_add=True)
    text_response = models.TextField(null=False, verbose_name='Текст отклика')

    class Meta:
        verbose_name = 'Отклик'
        verbose_name = 'Отклики'

    def preview(self):
        # возвращает начало статьи, длиной в 124 символа и добавляет многоточие
        size = 124 if len(self.text_response) > 124 else len(self.text_response)
        return self.text_response[:size] + "..."


# Модель для связи таблиц Объявления и Категории, для организации 3-й формы нормализации
# Модель AdsCategory
# связь с моделью Ads
# связь многие со многим с моделью Category
class AdsCategory(models.Model):
    ads = models.ForeignKey(Ad, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
