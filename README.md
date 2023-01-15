# Instructions to run


- Run the command 'Git clone https://github.com/Mike11199/CS-340-Group-Project.git'

- Create a .env file with the following
    - USER_NAME = 'cs340_ONID'
    - PASSWORD_LAST_4_DIGITS_STUDENT_ID = 'xxxx'

- The SQL file can be imported in PHPMyAdmin to restore the database
- The .mwb file is the schema used by MySQL workbench to forward engineer schema to the database
- Use the command 'gunicorn -b 0.0.0.0:6717 -D app:app' to run  ( I think only one group member can use the port at a time, so may have to modify app.py)
