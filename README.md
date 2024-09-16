# Pendataan Mabar VIP pada Game MLBB

## Overview

Project ini dibuat untuk memudahkan streamer perintis untuk mendata dan memanage siapa saja yang ikut mabar, request hero, dan request skin.

## Features

- soon

## Preparation

1. Clone this repository

    ```bash
    git clone https://github.com/Anon404/website_mabar.git
    ```

2. Install requirements

    ```bash
    pip install -r requirements.txt
    ```

3. Make migrations and migrate

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Create superuser and input credentials

    ```bash
    python manage.py createsuperuser
    ```

5. Run server

    ```bash
    python manage.py runserver
    ```

6. Visit the site

    ```bash
    http://127.0.0.1:8000/
    ```

## How to use

### Admin

1. Login as admin

    ```bash
    http://127.0.0.1:8000/admin/
    ```

2. Add Mabar

    ```bash
    http://127.0.0.1:8000/admin/mabar/mabar/add/
    ```

3. Add Request Hero

    ```bash
    http://127.0.0.1:8000/admin/mabar/requesthero/add/
    ```

4. Add Bonus Skin

    ```bash
    http://127.0.0.1:8000/admin/mabar/bonusskin/add/
    ```

### Public

Visit this website url:

- for mabar list

    Mengecek Status Mabar

    ```bash
    http://127.0.0.1:8000/public/list-mabar/
    ```

- for request hero list

    Mengecek Request Hero

    ```bash
    http://127.0.0.1:8000/public/list-req-hero/
    ```

- for bonus skin list

    Mengecek Bonus Skin

    ```bash
    http://127.0.0.1:8000/public/list-free-skin/
    ```

## License

[MIT License](https://github.com/ridwaanhall/management-mabar-VIP-MLBB/blob/main/LICENSE)

Copyright (c) 2024 [ridwaanhall](https://github.com/ridwaanhall)
