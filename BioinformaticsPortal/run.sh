#! /bin/bash
# if [ ! -f /tmp/mysql.sock ]; then
# 	ln -s /var/run/mysqld/mysqld.sock /tmp/mysql.sock
# fi
#  pipenv install && pipenv shell
python manage.py runserver
