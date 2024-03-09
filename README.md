# Django + Flowbite + Tailwindcss

## Running In Development

- create your project folder to clone into

    ``` sh
    mkdir <project_folder>
    git clone <url> <project_folder>
    ```

- create virtual environment

    ``` sh
    python -m venv .venv
    source .venv/bin/activate
    ```

- install requirements

    ``` sh
    pip install -r requirements.txt
    ```

- Create database

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

- install tailwindcss & flowbite

    ``` sh
    npm install -D tailwindcss
    npm install flowbite
    ```
  
- Generate css files

    ``` sh
    npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch
    ```
  
- Run server

    ```sh
    python manage.py collectstatic --no-input
    python manage.py compress --force
    python manage.py runserver
    ```

[https://medium.com/@ganapriyakheersagar/hosting-django-application-with-nginx-and-gunicorn-in-production-99e64dc4345a](https://medium.com/@ganapriyakheersagar/hosting-django-application-with-nginx-and-gunicorn-in-production-99e64dc4345a)
