# Live Website

https://spacetau.herokuapp.com/parts-and-spacecraft

- Deployed to Heroku with continuous deployment.  The heroku build is redeployed whenever changes are pushed to the github branch 'herokudeployment'.
- Uses JawsDB Maria as an external database for MySQL, using MariaDB.  Attempted to use Google Cloud but ran into errors. 

# Overview

- A Flask (python) based web application using jinja templates for the front-end, and a MySQL backed database to store associated data.  The Flask/Jinja application allows a user to interact with the database with full CRUD functionality for the Spacecrafts, intersection table (Spacecraft/Parts), and Astronauts table.

- This project demonstrates advanced knowledge of SQL, such as data definition/manipulation queries, ON CASCADE, intersection tables to support many-to-many relationships with foreign keys, and advanced queries.

# Home Page

![image](https://user-images.githubusercontent.com/91037796/226444086-02749272-c008-49a0-bcbb-187085ae50a8.png)

![image](https://user-images.githubusercontent.com/91037796/226470102-ab91d040-141c-4404-970c-d064b7db6ce2.png)


# Spacecraft Page

![image](https://user-images.githubusercontent.com/91037796/226444153-23aa410f-2f3a-4310-9ade-7e49f8d0025a.png)

# Parts Page

![image](https://user-images.githubusercontent.com/91037796/226444191-bd31b5b4-8c83-48eb-9604-f299310842f8.png)

# Spacecraft/Parts Intersection Table Page

![image](https://user-images.githubusercontent.com/91037796/226444235-cc4d09f6-d38b-4e22-bcfc-b0bede835fb7.png)

# Missions Page

![image](https://user-images.githubusercontent.com/91037796/226444277-2abd42e0-cc97-448f-87fa-87165f8aae6a.png)

# Astronauts Page

![image](https://user-images.githubusercontent.com/91037796/226444354-b8b3ad03-dced-4f16-a90d-7f4642358745.png)

# Clients Page

![image](https://user-images.githubusercontent.com/91037796/226444408-68d49583-6e08-4ade-abed-9773d5a0ff13.png)

# Planetary Objects Page

![image](https://user-images.githubusercontent.com/91037796/226444457-16aa5b36-58ac-48a5-b130-f13cad998172.png)


# Google Cloud - Attempt

![image](https://user-images.githubusercontent.com/91037796/226478770-6c10c5ba-2b6d-44d1-9854-c361b5526f38.png)

- Managed to create database, but connection could not be established between Heroku and google cloud.

# Instructions to run in Flip


- Run the command 'Git clone https://github.com/Mike11199/CS-340-Group-Project.git'

- Create a .env file with the following
    - USER_NAME = 'cs340_ONID'
    - PASSWORD_LAST_4_DIGITS_STUDENT_ID = 'xxxx'

- The SQL file can be imported in PHPMyAdmin to restore the database
- The .mwb file is the schema used by MySQL workbench to forward engineer schema to the database
- Use the command 'gunicorn -b 0.0.0.0:6717 -D app:app' to run the app on the flip2 OSU server  ( I think only one group member can use the port at a time, so may have to modify app.py)



# Schema Diagram - Updated 2-8-2023
![image](https://user-images.githubusercontent.com/91037796/217623955-46c216ee-a5d6-4492-b7f7-6a7dc82b80b5.png)


# Entity Relationship Diagram (ERD)

![ERD](https://user-images.githubusercontent.com/91037796/215379806-03ab3883-83bb-4a6e-ad84-d0f6da1e263f.png)
