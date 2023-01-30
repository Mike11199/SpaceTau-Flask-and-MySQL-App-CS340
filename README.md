# Instructions to run


- Run the command 'Git clone https://github.com/Mike11199/CS-340-Group-Project.git'

- Create a .env file with the following
    - USER_NAME = 'cs340_ONID'
    - PASSWORD_LAST_4_DIGITS_STUDENT_ID = 'xxxx'

- The SQL file can be imported in PHPMyAdmin to restore the database
- The .mwb file is the schema used by MySQL workbench to forward engineer schema to the database
- Use the command 'gunicorn -b 0.0.0.0:6717 -D app:app' to run the app on the flip2 OSU server  ( I think only one group member can use the port at a time, so may have to modify app.py)



# Schema Diagram
![image](https://user-images.githubusercontent.com/91037796/215379622-3b84eb56-2ee7-4fe2-a0fc-6a07e7474c00.png)


# Entity Relationship Diagram (ERD)

![ERD](https://user-images.githubusercontent.com/91037796/215379806-03ab3883-83bb-4a6e-ad84-d0f6da1e263f.png)
