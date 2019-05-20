# Short URL project
[Проект на heroku](https://short-url-project.herokuapp.com)

### Setup

    git clone https://github.com/ponyaid/shorturl.git
    cd shorturl
    virtualenv -p python3 venv
    source env/bin/activate
    pip install -r requirements.txt
    # DBUSERNAME, DBPASSWORD и DBNAME необходимо заменить на свои реквизиты доступа к БД
    export DATABASE_URL='postgresql://DBUSERNAME:DBPASSWORD@localhost/DBNAME'
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    python manage.py runserver
