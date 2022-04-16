# python manage.py shell
from django.contrib.auth.models import User
from board.models import Category, Ad, Response, AdsCategory, Author


def todo():
    # полезно для отладки удалять объекты
    User.objects.all().delete()
    Category.objects.all().delete()


# Создание двух пользователей, с заполнением всех обязательных полей
user_dima = User.objects.create_user(username='dima', email='texno_log_90@mail.ru', password='12345')
user_x = User.objects.create_user(username='x', email='texno_log_90@mail.ru', password='12345')

dima = Author.objects.create(user=user_dima)
x_user = Author.objects.create(user=user_x)

# Добавляем категории в модель Category
tanks = Category.objects.create(name='Танки')
xils = Category.objects.create(name='Хилы')
dd = Category.objects.create(name='ДД')
blacksmiths = Category.objects.create(name='Кузнецы')
potionbrew = Category.objects.create(name='Зельевары')
merchants = Category.objects.create(name='Торговцы')
gildmasters = Category.objects.create(name='Гилдмастеры')
kvestgiver = Category.objects.create(name='Квестгиверы')
tanners = Category.objects.create(name='Кожевники')
spellmasters = Category.objects.create(name='Мастера заклинаний')

# Описываем текст объявления
text_tanks = 'Объявления к танкам '
text_xils = 'Объявления к хилам '
text_dd = 'Объявления к ДД'
text_blacksmiths = 'Объявления кузнецы '
text_potoinbrew = 'Объявления к Зельевары '
text_mercants = 'Объявления к торговцам '
text_gildmaster = 'Объявления к гилдмастерам '
text_kvestgiver = 'Объявления к квест гиверам '
text_tanners = 'Объявления к кожевникам '
text_spellmaster = 'Объявления к мастерам заклинаний '

# создаем объявление
I = Ad.objects.create(author=dima, article='TAnk1111', text_ad=text_tanks)
II = Ad.objects.create(author=dima, article='xils222', text_ad=text_xils)
III = Ad.objects.create(author=dima, article='dd3333', text_ad=text_dd)
IV = Ad.objects.create(author=dima, article='Kuzneci444', text_ad=text_blacksmiths)
V = Ad.objects.create(author=dima, article='Zellevary555', text_ad=text_potoinbrew)
VI = Ad.objects.create(author=dima, article='torgovcy666', text_ad=text_mercants)
VII = Ad.objects.create(author=dima, article='gildmaster777', text_ad=text_gildmaster)
VIII = Ad.objects.create(author=dima, article='cvestgiver8888', text_ad=text_kvestgiver)
IX = Ad.objects.create(author=dima, article='tanners9999', text_ad=text_tanners)
X = Ad.objects.create(author=dima, article='Masterazaclinaniy101010', text_ad=text_spellmaster)


# присваиваем категории
с1 = AdsCategory.objects.create(ads=I,  category=tanks)
c2 = AdsCategory.objects.create(ads=II,  category=xils)
c3 = AdsCategory.objects.create(ads=III,  category=dd)
c4 = AdsCategory.objects.create(ads=IV,  category=blacksmiths)
c5 = AdsCategory.objects.create(ads=V, category=potionbrew)
c6 = AdsCategory.objects.create(ads=VI,  category=merchants)
c7 = AdsCategory.objects.create(ads=VII,  category=gildmasters)
c8 = AdsCategory.objects.create(ads=VIII,  category=kvestgiver)
c9 = AdsCategory.objects.create(ads=IX,  category=tanners)
c10 = AdsCategory.objects.create(ads=X,  category=spellmasters)


# отклики
o1 = Response.objects.create(ads=I, user=x_user.user, text_response='o1 x')
o2 = Response.objects.create(ads=II, user=x_user.user, text_response='o2 xx')
o3 = Response.objects.create(ads=III, user=x_user.user, text_response='o3 xxx')
o4 = Response.objects.create(ads=IV, user=x_user.user, text_response='o4 xxxx')
o5 = Response.objects.create(ads=V, user=x_user.user, text_response='o5 xxxxx')
o6 = Response.objects.create(ads=VI, user=x_user.user, text_response='o6 xxxxxx')
o7 = Response.objects.create(ads=VII, user=x_user.user, text_response='o7 xxxxxxx')
o8 = Response.objects.create(ads=VIII, user=x_user.user, text_response='o8 xxxxxxxx')
o9 = Response.objects.create(ads=IX, user=x_user.user, text_response='o9 xxxxxxxxx')
o10 = Response.objects.create(ads=X, user=x_user.user, text_response='o10 xxxxxxxxxx')
