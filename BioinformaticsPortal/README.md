# Up and Running 
- Install mysql or maria db 
- Run the following sql in mariadb console (mysql -uroot)
```mysql
   CREATE DATABASE BioinformaticsPortal;
   CREATE USER 'portal_admin'@'localhost' IDENTIFIED BY 'test-password';
   GRANT ALL PRIVILEGES ON BioinformaticsPortal.* TO 'portal_admin'@'localhost';
   FLUSH PRIVILEGES;
   ALTER DATABASE `BioinformaticsPortal` CHARACTER SET utf8;
```
Then 
- Run ``` pipenv install && pipenv shell```
- Run ``` python manage.py runserver```

The server should be running on localhost:8000/portal
