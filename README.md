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

#### Команда `load_place` для системы управления Django загружает данные для мест из JSON-файлов.



##### Использование

Для загрузки данных о месте выполните следующую команду:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">python manage.py load_place <url json-файла>
</code></div></div></pre>

Например:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">python manage.py load_place https://github.com/devmanorg/where-to-go-places/tree</code></div></div></pre>


<a href="#" id="data-sources"></a>

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).
