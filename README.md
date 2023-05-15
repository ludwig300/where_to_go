# Куда пойти — Москва глазами Артёма

Сайт о самых интересных местах в Москве. Авторский проект Артёма.

![<span class=](.gitbook/assets/site.png)

[Демка сайта](https://mr4silent.pythonanywhere.com/)

[Админка сайта](https://mr4silent.pythonanywhere.com/admin/)
        
## Установка

Для запуска проекта локально выполните следующие шаги:

1. Клонируйте репозиторий: `git clone <repository-url>`
2. Перейдите в папку проекта: `cd <project-directory>`
3. Создайте виртуальное окружение: `python -m venv env`
4. Активируйте виртуальное окружение:
   * Для Windows: `.\env\Scripts\activate`
   * Для Unix/Linux: `source env/bin/activate`
5. Установите зависимости проекта: `pip install -r requirements.txt`
6. Примените миграции базы данных: `python manage.py migrate`
7. Создайте Суперюзера `python manage.py createsuperuser`
8. Запустите сервер разработки: `python manage.py runserver`

## Зависимости

* Django==4.2
* django-admin-sortable2==2.1.8
* django-ckeditor==6.5.1
* django-js-asset==2.0.0
* leaflet==0.0.3
* Pillow==9.5.0

## Конфигурация

Для конфигурации проекта используются переменные окружения. Создайте файл `.env` в корневой директории проекта и укажите следующие переменные:

* SECRET_KEY: Секретный ключ для приложения Django.
* DEBUG: Установите значение `True` для разработки и `False` для продакшн среды.
* ALLOWED_HOSTS: Список разрешенных хостов, разделенных запятыми.
* DB_NAME: Имя файла базы данных.
* LANGUAGE_CODE: Код языка по умолчанию.
* TIME_ZONE: Часовой пояс по умолчанию.
* USE_I18N: Установите значение `True`, чтобы включить интернационализацию.
* USE_TZ: Установите значение `True`, чтобы включить поддержку часовых поясов.
* SECURE_HSTS_SECONDS: Количество секунд для включения HTTP Strict Transport Security (HSTS).
* SECURE_SSL_REDIRECT: Установите значение `True`, чтобы перенаправлять все HTTP-запросы на HTTPS.
* SESSION_COOKIE_SECURE: Установите значение `True`, чтобы отправлять куки сеанса только через HTTPS.
* CSRF_COOKIE_SECURE: Установите значение `True`, чтобы отправлять CSRF-токен только через HTTPS.
* SECURE_HSTS_INCLUDE_SUBDOMAINS: Установите значение `True`, чтобы включить поддомены в HSTS.
* SECURE_HSTS_PRELOAD: Установите значение `True`, чтобы включить предзагрузку HSTS.

Убедитесь в том, чтобы изменить значения этих переменных в соответствии с вашей конфигурацией.

## Настройки

Внизу справа на странице можно включить отладочный режим логгирования.

![debug mode](.gitbook/assets/debug-option.png)

Настройки сохраняются в Local Storage браузера и не пропадают после обновления страницы. Чтобы сбросить настройки, удалите ключи из Local Storage с помощью Chrome Dev Tools —&gt; Вкладка Application —&gt; Local Storage.

Если что-то работает не так, как ожидалось, то начните с включения отладочного режима логгирования.

#### Команда `load_place` для системы управления Django загружает данные для мест из JSON-файлов.



##### Использование

Для загрузки данных о месте выполните следующую команду:

``` bash
>python manage.py load_place <url json-файла>
```

Например:

``` bash
>python manage.py load_place https://github.com/devmanorg/where-to-go-places/tree/master/places/anti-cafe-bizone.json
```

Пример example.json
``` json
{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
    "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения. В стоимость уже включены напитки, сладкие угощения, библиотека комиксов, большая коллекция популярных настольных и видеоигр. Также вы можете арендовать ВИП-зал для большой компании и погрузиться в мир виртуальной реальности с помощью специальных очков от топового производителя.</p><p>В течение недели организаторы проводят разнообразные встречи для меломанов и киноманов. Также можно присоединиться к английскому разговорному клубу или посетить образовательные лекции и мастер-классы. Летом организаторы запускают марафон настольных игр. Каждый день единомышленники собираются, чтобы порубиться в «Мафию», «Имаджинариум», Codenames, «Манчкин», Ticket to ride, «БЭНГ!» или «Колонизаторов». Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```
## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).
