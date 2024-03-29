# Проект YaMDb

# Описание
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Category) может быть расширен администратором (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха.
Произведению может быть присвоен жанр (Genre) из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

Аутентификация по JWT-токену

Поддерживает методы GET, POST, PUT, PATCH, DELETE

Предоставляет данные в формате JSON

Cоздан в команде из трёх человек с использованим Git в рамках учебного курса Яндекс.Практикум.
### Запуск проекта:

- Клонируйте репозиторий:
```
git clone git@github.com:korecbtc/api_yamdb.git
```
 - Перейдите в папку с проектом

 - Установите и активируйте виртуальное окружение:
```
python -m venv venv

source venv/Scripts/activate
```

 - Зайдите в папку с проектом и установите зависимости из файла requirements.txt

``` 
pip install -r requirements.txt
```

- В папке с файлом manage.py выполните команды:

``` 
python manage.py makemigrations 

python manage.py migrate

python manage.py runserver 
```
***

# Регистрация
/api/v1/auth/signup/ - отправить username и email,
проверить почту, скопировать проверочный код и отправить его на эндпоинт /api/v1/auth/token/
# Примеры
/api/v1/users/me/ - Получить данные своей учетной записи.

/api/v1/categories/ - Получить список всех категорий.

/api/v1/genres/ - Получить список всех жанров.

Полный список запросов API можно посмотреть в документации
http://127.0.0.1:8000/redoc/
# Технологии
- проект написан на Python с использованием Django REST Framework
- библиотека Simple JWT - работа с JWT-токеном
# Авторы
Станислав Хныкин  

Георгий Муромцев  

Корец Иван
