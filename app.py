from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request, jsonify

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


USER_NAME = os.getenv("USER_NAME")
PASSWORD_LAST_4_DIGITS_STUDENT_ID = os.getenv("PASSWORD_LAST_4_DIGITS_STUDENT_ID")


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = USER_NAME
app.config['MYSQL_PASSWORD'] = PASSWORD_LAST_4_DIGITS_STUDENT_ID #last 4 of onid
app.config['MYSQL_DB'] = USER_NAME
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)


# Routes
@app.route('/')
def root():
    return render_template("main.jinja")



@app.route('/spacecraft', methods=["POST", "GET"])
def spacecraft_page():
    
    
    if request.method == "GET":
        cur = mysql.connection.cursor()
        
        query1 = "SELECT * FROM Spacecrafts;"    
        cur.execute(query1)
        spacecraft_data = cur.fetchall()
        
        query2 = "SELECT id_planetary_object, name FROM Planetary_Objects;"
        cur.execute(query2)
        planetary_data = cur.fetchall()
        
        planetary_dict = {planet['id_planetary_object']: planet['name'] for planet in planetary_data}
        

                
        query3 = """
                    SELECT 
                    
                    Spacecrafts.id_spacecraft as 'Spacecraft ID', 
                    Spacecrafts.name as 'Spacecraft Name', 
                    Spacecrafts.in_orbit as 'In Orbit?',  
                    Spacecrafts.launched as 'Launched?', 
                    Spacecrafts.delta_v_remaining as 'Delta V Remaining', 
                    Spacecrafts.mission_elapsed_time_days as 'Mission Elapsed Time (Days)', 
                    Planetary_Objects.name as 'Sphere of Influence' 

                    FROM Spacecrafts 

                    LEFT JOIN Planetary_Objects on Planetary_Objects.id_planetary_object = Spacecrafts.id_planetary_object;
                """
                    
        cur.execute(query3)
        spacecraft_data2 = cur.fetchall()
        spacecraft_data_dictionary =  {spacecraft['Spacecraft ID']: {'Spacecraft Name': spacecraft['Spacecraft Name'], 'In Orbit?': spacecraft['In Orbit?'],'Launched?': spacecraft['Launched?'],'Delta V Remaining': spacecraft['Delta V Remaining'],'Mission Elapsed Time (Days)': spacecraft['Mission Elapsed Time (Days)'],'Sphere of Influence': spacecraft['Sphere of Influence'], } for spacecraft in spacecraft_data2}
        
        # DON'T USE - PRIOR VERSION WHERE SPACECRAFT AND PLANETARY OBJECTS TABLE WERE PASSED INTO JINJA AND FUNCTION WAS USED TO LOOKUP PLANET BY PLANET ID.  
        # NOW USING A SQL LEFT JOIN - KEEPING THIS AS AN EXAMPLE OF HOW TO PASS A PYTHON FUNCTION INTO
        def get_planetary_object_by_id(planetary_objects, planet_id):
            for planet in planetary_objects:
                if planet['id_planetary_object'] == planet_id:
                    return planet
            return None    
        
        
            
        # return "<h1>MySQL Results" + str(results)
        # return "<h1>MySQL Results" + str(results[0])
        # return render_template("spacecraft.jinja", spacecraft_data=spacecraft_data2, planetary_data=planetary_data)
        return render_template("spacecraft.jinja", spacecraft_data=spacecraft_data2, planetary_data=planetary_dict, spacecraft_data_dictionary=spacecraft_data_dictionary)

        # OLD VERSION WHERE PYTHON FUNCTION WAS PASSED TO FILTER PLANETARY DATA BY ID - NOW USING SQL LEFT JOIN INSTEAD
        # return render_template("spacecraft.jinja", spacecraft_data=spacecraft_data2, planetary_data=planetary_data, get_planetary_object_by_id=get_planetary_object_by_id)

    if request.method == "POST":
        
         if request.form.get('add_spacecraft'):
             
            name = request.form["name"]
            in_orbit = request.form["in_orbit"]
            launched = request.form["launched"]
            sphere_of_influence = request.form["sphere_of_influence"]
            delta_v_remaining = request.form["delta_v_remaining"]      
            MET_days  = request.form["MET_days"]      
                      
            query5 = "INSERT INTO Spacecrafts (name, in_orbit, launched, id_planetary_object, delta_v_remaining, mission_elapsed_time_days) VALUES (%s,%s,%s,%s,%s,%s)"
            cur = mysql.connection.cursor()
            cur.execute(query5, (name, in_orbit, launched, sphere_of_influence, delta_v_remaining, MET_days))
            mysql.connection.commit()
        
         return redirect("/spacecraft")
    
       
@app.route("/delete_spacecraft/<int:id>")
def delete_spacecraft(id):


    query = "DELETE FROM Spacecrafts WHERE id_spacecraft = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    # redirect back to people page
    # message = jsonify({'Success': 'Spacecraft Deleted!'}) 
    return jsonify({'Success': 'Spacecraft Deleted!'}), 200
    return redirect("/spacecraft")




@app.route("/get_spacecraft/<int:id>")
def retrieve_spacecraft(id):
    query = "Select * FROM Spacecrafts WHERE id_spacecraft = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query,(id,))
    spacecraft_data2 = cur.fetchall()
    return jsonify(spacecraft_data2), 200
     
       
        

@app.route('/missions')
def missions_page():
    return render_template("missions.jinja")

@app.route('/parts')
def parts_page():
    # query = "SELECT * FROM parts;"
    # cur = mysql.connection.cursor()
    # cur.execute(query)
    # results = cur.fetchall()    
    # print(results)   
    return render_template("parts.jinja")

@app.route('/astronauts')
def astronauts_page():
    return render_template("astronauts.jinja")

@app.route('/clients')
def clients_page():
    return render_template("clients.jinja")

@app.route('/planetary-objects')
def planetary_objects_page():
    return render_template("planetary_objects.jinja")

@app.route('/parts-and-spacecraft')
def parts_and_spacecraft_page():
    return render_template("parts_and_spacecraft.jinja")


# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted; changed to 6574 per tutorial video
    app.run(port=6728, debug=True)