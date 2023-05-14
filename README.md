# Куда пойти — Москва глазами Артёма

Сайт о самых интересных местах в Москве. Авторский проект Артёма.

![<span class=](.gitbook/assets/site.png)&#x41A;К " />

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

<a href="#" id="data-sources"></a>

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).
