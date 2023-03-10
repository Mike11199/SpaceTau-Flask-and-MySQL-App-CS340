from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request, jsonify

# from werkzeug.exceptions import HTTPException  # reference to allow for debugging https://flask.palletsprojects.com/en/2.2.x/errorhandling/

import os
# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())


USER_NAME = 'cs340_hudsontr' #os.getenv("USER_NAME")
PASSWORD_LAST_4_DIGITS_STUDENT_ID = '9413' # os.getenv("PASSWORD_LAST_4_DIGITS_STUDENT_ID")


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



@app.route("/update_spacecraft/<int:id>", methods=["POST", "GET"])
def update_spacecraft(id):

    data = request.get_json()
    name = data["spacecraft_name_update"]
    in_orbit = data["orbit_select_option"]
    launched = data["launched_select_option"]
    sphere_of_influence = data["soi_select_option"]
    delta_v_remaining = data["spacecraft_delta_v_update"]
    MET_days = data["spacecraft_met_update"]

    query = """
            UPDATE Spacecrafts
            SET name=%s, in_orbit=%s, launched=%s, id_planetary_object=%s, delta_v_remaining=%s, mission_elapsed_time_days=%s
            WHERE id_spacecraft = %s;
            """
    cur = mysql.connection.cursor()
    cur.execute(query, (name, in_orbit, launched, sphere_of_influence, delta_v_remaining, MET_days, id,))
    mysql.connection.commit()

    return jsonify(id)


@app.route('/missions', methods=["POST", "GET"])
def missions_page():
    

    # DEFAULT ROUTE - Viewing the page executes SELECT statement or READ functionality
    if request.method == "GET":
        
        missions_query =''
        
        missions_query = """
                SELECT 
                
                Missions.id_mission as 'Mission ID', 
                Missions.name as 'Mission Name', 
                Missions.contract_revenues as 'Contract Revenues',  
                Missions.contract_costs as 'Contract Costs', 
                Missions.contract_profit as 'Contract Profit', 
                Missions.is_external as 'External?',            
                Missions.mission_description as 'Description',
                Spacecrafts.name as 'Spacecraft Name',
                Clients.name as 'Client Name'                       
                
                
                FROM Missions 
                
                LEFT JOIN Spacecrafts on Spacecrafts.id_spacecraft = Missions.id_spacecraft
                LEFT JOIN Clients on Clients.id_client = Missions.id_client;
            """
            
        client_query_1 = "SELECT id_client, name FROM Clients"
        spacecraft_query_1="SELECT id_spacecraft, name from Spacecrafts "
            
        cur = mysql.connection.cursor()
        cur.execute(missions_query)
        mission_data = cur.fetchall()    
        
        
        
        cur.execute(client_query_1)
        client_data = cur.fetchall()    
        client_dict = {client['id_client']: client['name'] for client in client_data}
        client_data = client_dict
        
        cur.execute(spacecraft_query_1)
        spacecraft_data = cur.fetchall()    
        spacecraft_dict = {spacecraft['id_spacecraft']: spacecraft['name'] for spacecraft in spacecraft_data}
        spacecraft_data = spacecraft_dict
        
        return render_template("missions.jinja", mission_data=mission_data, client_data=client_data, spacecraft_data=spacecraft_data)



    # POST ROUTE - Executes INSERT statement for CREATE functionality to add a new record.
    if request.method == "POST":
        
            mission_name = request.form["name"]
            contract_revenues = request.form["contract_revenues"]
            contract_costs = request.form["contract_costs"]
            is_external = request.form["external_contract"]
            mission_description = request.form["mission_description"]
                        
            spacecraft_id = request.form["spacecraft_id"]   # OPTIONAL
            client_id =request.form["client_id"]            # OPTIONAL
            
            # spacecraft_id = 'noneSelected'
            # client_id = 'noneSelected'
           
            cur = mysql.connection.cursor()
           
           # adding mission with NO client and NO spacecraft selected from drop down (NULL values in database OK as FKs are optional in this table)
            if spacecraft_id == 'noneSelected' and client_id =='noneSelected':
                add_mission_query = """
                INSERT INTO Missions (name, contract_revenues, contract_costs, is_external, mission_description) 
                VALUES (%s,%s,%s,%s,%s);
                """
                cur.execute(add_mission_query, (mission_name, contract_revenues, contract_costs, is_external, mission_description))
            
            # adding only client from dynamic drop down NO spacecraft
            elif spacecraft_id == 'noneSelected' and client_id !='noneSelected':
                add_mission_query = """
                INSERT INTO Missions (name, contract_revenues, contract_costs, is_external, mission_description, id_client) 
                VALUES (%s,%s,%s,%s,%s,%s);
                """
                cur.execute(add_mission_query, (mission_name, contract_revenues, contract_costs, is_external, mission_description, client_id))
            
            # adding only spacecraft from dynamic drop down NO client
            elif spacecraft_id != 'noneSelected' and client_id =='noneSelected':
                add_mission_query = """
                INSERT INTO Missions (name, contract_revenues, contract_costs, is_external, mission_description, id_spacecraft) 
                VALUES (%s,%s,%s,%s,%s,%s);
                """
                cur.execute(add_mission_query, (mission_name, contract_revenues, contract_costs, is_external, mission_description, spacecraft_id))
            
            # adding both spacecraft and client ID
            else:
                add_mission_query = """
                INSERT INTO Missions (name, contract_revenues, contract_costs, is_external, mission_description, id_spacecraft, id_client) 
                VALUES (%s,%s,%s,%s,%s,%s,%s);
                """
                cur.execute(add_mission_query, (mission_name, contract_revenues, contract_costs, is_external, mission_description, spacecraft_id, client_id))
            
            mysql.connection.commit()
            return redirect("/missions")
    



@app.route('/parts', methods=["POST", "GET"])
def parts_page():

 
    
    if request.method == "GET":
        query = "SELECT * FROM Parts;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        parts_data = cur.fetchall()    

        return render_template("parts.jinja", parts_data=parts_data)

    
    if request.method == "POST":
        part_name = request.form["name"]
        part_manufacturer = request.form["manufacturer"]
        part_mass = request.form["mass"]
        part_cost = request.form["cost"]
        part_description = request.form["description"]
                    
        add_parts_query = """
        INSERT INTO Parts (name, manufacturer, mass_kg, cost, part_description) 
        VALUES (%s,%s,%s,%s,%s);
        """
        
        cur = mysql.connection.cursor()
        cur.execute(add_parts_query, (part_name, part_manufacturer, part_mass, part_cost, part_description))
        mysql.connection.commit()
        return redirect("/parts")



@app.route('/astronauts', methods=["GET", "POST"])
def astronauts_page():
    #return render_template("astronauts.jinja")
    

    if request.method == "GET":
        cur = mysql.connection.cursor()
        query_all = "SELECT * FROM Astronauts;"
        cur.execute(query_all)
        astronaut_data = cur.fetchall()
        cur = mysql.connection.cursor()
        query2 = "SELECT id_spacecraft, name FROM Spacecrafts;"
        cur.execute(query2)
        spacecraft_data = cur.fetchall()
        spacecraft_dict  = {s['id_spacecraft']: s['name'] for s in spacecraft_data}
        print(spacecraft_dict)

        return render_template("astronauts.jinja", astronaut_data=astronaut_data, spacecraft_dict=spacecraft_dict)

    if request.method == "POST":
        #if request.form.get("addAstronaut"):
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        mission_role = request.form['mission_role']
        spacecraft_id = request.form['spacecraft_id']
        astronaut_insert_query = "INSERT INTO Astronauts (name, age, gender, mission_role, id_spacecraft) VALUES (%s,%s,%s,%s,%s);"
        cur = mysql.connection.cursor()
        vals = (name, age, gender, mission_role, spacecraft_id)
        cur.execute(astronaut_insert_query, vals)
        mysql.connection.commit()
        return redirect("/astronauts")

@app.route('/clients', methods=["POST", "GET"])
def clients_page():
    if request.method == "GET":
        cur = mysql.connection.cursor()
        query_all = "SELECT * FROM Clients;"
        cur.execute(query_all)
        client_data = cur.fetchall()
        return render_template("clients.jinja", client_data=client_data)
    
    if request.method =="POST":
        #if request.form.get('add_client'):
        ein = request.form['ein']
        name = request.form['name']
        contribution_amount = request.form['ein']
        address = request.form['address']
        client_insert_query = "INSERT INTO Clients (ein, name, contribution_amount, address) VALUES (%s, %s, %s, %s);"
        vals = (ein, name, contribution_amount, address)
        cur = mysql.connection.cursor()
        cur.execute(client_insert_query, vals)
        mysql.connection.commit()
        return redirect("/clients")
    
@app.route("/get_client/<int:id>")
def retrieve_client(id):
    query = "Select * FROM Clients WHERE id_client = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query,(id,))
    client_data2 = cur.fetchall()
    return jsonify(client_data2), 200

@app.route("/update_client/<int:id>", methods=["POST", "GET"])
def update_client(id):
    data = request.get_json()
    ein = data['client_ein_update']
    name = data['client_name_update']
    contribution_amount = data['client_contribution_amount_update']
    address = data['client_address_update']

    query = """
            UPDATE Clients
            SET ein=%s, name=%s, contribution_amount=%s, address=%s
            WHERE id_client = %s;
            """
    cur = mysql.connection.cursor()
    cur.execute(query, (ein, name, contribution_amount, address, id,))
    mysql.connection.commit()

    return jsonify(id)

@app.route("/delete_client/<int:id>")
def delete_client(id):
    query = "DELETE FROM Spacecrafts WHERE id_spacecraft = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()
    return jsonify({'Success': 'Spacecraft Deleted!'}), 200

@app.route('/planetary-objects', methods=["POST", "GET"])
def planetary_objects_page():
    
    
    # DEFAULT ROUTE - Viewing the page executes SELECT statement or READ functionality
    if request.method == "GET":
        
        planetary_obj_query = """
                SELECT 
                
                Planetary_Objects.id_planetary_object as 'Planetary Obj ID', 
                Planetary_Objects.name as 'Object Name', 
                Planetary_Objects.surface_gravity_g as 'Surface Gravity (g)',  
                Planetary_Objects.avg_distance_from_sun_au as 'Avg Distance from Sun (AU)', 
                Planetary_Objects.is_planet as 'Is Planet?', 
                Planetary_Objects.is_moon as 'Is Moon?'            

                FROM Planetary_Objects 
            """
            
        cur = mysql.connection.cursor()
        cur.execute(planetary_obj_query)
        planetary_obj_data = cur.fetchall()    

        return render_template("planetary_objects.jinja", planetary_obj_data=planetary_obj_data)



    # POST ROUTE - Executes INSERT statement for CREATE functionality to add a new record.
    if request.method == "POST":
        
            planetary_obj_name = request.form["name"]
            planetary_obj_gravity = request.form["surface_gravity"]
            planetary_obj_distance = request.form["avg_distance"]
            planetary_obj_is_planet = request.form["is_planet"]
            planetary_obj_is_moon = request.form["is_moon"]
                        
            add_planetary_obj_query = """
            INSERT INTO Planetary_Objects (name, surface_gravity_g, avg_distance_from_sun_au, is_planet, is_moon) 
            VALUES (%s,%s,%s,%s,%s);
            """
            
            cur = mysql.connection.cursor()
            cur.execute(add_planetary_obj_query, (planetary_obj_name, planetary_obj_gravity, planetary_obj_distance, planetary_obj_is_planet, planetary_obj_is_moon))
            mysql.connection.commit()
            return redirect("/planetary-objects")
    






@app.route('/parts-and-spacecraft', methods=["POST", "GET"])
def parts_and_spacecraft_page():

    if request.method == "GET":

        query1 = """
                SELECT

                Spacecraft_has_Parts.id_spacecraft as 'Spacecraft ID',
                Spacecrafts.name as 'Spacecraft Name',
                Spacecraft_has_Parts.id_part as 'Part ID',
                Parts.name as 'Parts Name'

                FROM Spacecraft_has_Parts

                LEFT JOIN Spacecrafts on Spacecrafts.id_spacecraft = Spacecraft_has_Parts.id_spacecraft
                LEFT JOIN Parts on Parts.id_part = Spacecraft_has_Parts.id_part;
            """
        cur = mysql.connection.cursor()
        cur.execute(query1)
        # query2 = "SELECT * FROM Spacecraft_has_Parts;"
        spacecraft_parts_data = cur.fetchall()

        query2 = "SELECT id_spacecraft, name FROM Spacecrafts;"
        cur = mysql.connection.cursor()
        cur.execute(query2)

        spacecraft_for_dropdown = cur.fetchall()

        query3 = "SELECT id_part, name FROM Parts;"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        parts_for_dropdown = cur.fetchall()

        return render_template("parts_and_spacecraft.jinja", spacecraft_parts_data=spacecraft_parts_data, spacecraft_for_dropdown=spacecraft_for_dropdown, parts_for_dropdown=parts_for_dropdown)



    # POST request for FILTERING
    if request.method == "POST":        
        if request.form.get('filter_relationships',0) == 'Filter Relationships':

            filter_id = request.form['spacecraft_select_option']
            print(filter_id)
            query1 = """
                SELECT

                Spacecraft_has_Parts.id_spacecraft as 'Spacecraft ID',
                Spacecrafts.name as 'Spacecraft Name',
                Spacecraft_has_Parts.id_part as 'Part ID',
                Parts.name as 'Parts Name'

                FROM Spacecraft_has_Parts

                LEFT JOIN Spacecrafts on Spacecrafts.id_spacecraft = Spacecraft_has_Parts.id_spacecraft
                LEFT JOIN Parts on Parts.id_part = Spacecraft_has_Parts.id_part
                WHERE Spacecraft_has_Parts.id_spacecraft=%s;
            """
            cur = mysql.connection.cursor()
            cur.execute(query1, (filter_id))
            spacecraft_parts_data = cur.fetchall()

            query2 = "SELECT id_spacecraft, name FROM Spacecrafts;"
            cur = mysql.connection.cursor()
            cur.execute(query2)
            spacecraft_for_dropdown = cur.fetchall()

            query3 = "SELECT id_part, name FROM Parts;"
            cur = mysql.connection.cursor()
            cur.execute(query3)
            parts_for_dropdown = cur.fetchall()

            return render_template("parts_and_spacecraft.jinja", spacecraft_parts_data=spacecraft_parts_data, spacecraft_for_dropdown=spacecraft_for_dropdown, parts_for_dropdown=parts_for_dropdown)

        # for ADDING a relationship POST request
        elif request.form.get('Add_Spacecraft_Part_Relationship',0) == 'Add Spacecraft/Part Relationship':
            part_id = request.form["part_name"]
            spacecraft_id = request.form["spacecraft_name"]
            # print("Add relationship debugging\n")
            # print(part_id)
            # print(spacecraft_id)
            # id_part_query = "SELECT id_part FROM Parts WHERE name=%s"
            # cur = mysql.connection.cursor()
            # cur.execute(id_part_query, (part_name))
            # id_part = cur.fetchall()
            # id_spacecraft_query = "SELECT id_part FROM Parts WHERE name=%s"
            # cur = mysql.connection.cursor()
            # cur.execute(id_spacecraft_query, (spacecraft_name))
            # id_spacecraft = cur.fetchall()
            add_relationship_query = "INSERT INTO Spacecraft_has_Parts (id_spacecraft, id_part) VALUES(%s, %s);"
            cur = mysql.connection.cursor()
            cur.execute(add_relationship_query, (spacecraft_id, part_id))
            mysql.connection.commit()
            return redirect("/parts-and-spacecraft")
        else:
            return redirect("/parts-and-spacecraft")

# @app.route("/filter_spacecraft/<int:id>")
# def retrieve_spacecraft(id):
#     query = "Select * FROM Spacecrafts WHERE id_spacecraft = '%s';"
#     cur = mysql.connection.cursor()
#     cur.execute(query,(id,))
#     spacecraft_data2 = cur.fetchall()
#     return jsonify(spacecraft_data2), 200


@app.route("/update_parts_and_spacecraft/<int:id>", methods=["POST", "GET"])
def update_part_and_spacecraft_relationship(part_id, spacecraft_id):
    data = request.get_json()
    part_name = data["part_name"]
    spacecraft_name = data["spacecraft_name"]
    spacecraft_id = data["spacecraft_id"]
    add_relationship_query = "UPDATE Spacecraft_has_Parts SET id_spacecraft=%s, id_part=%s WHERE id_spacecraft=%s"
    cur = mysql.connection.cursor()
    cur.execute(add_relationship_query, (spacecraft_name, part_name, spacecraft_id))
    mysql.connection.commit()

    return jsonify(part_id, spacecraft_id)


# reference to allow for debugging https://flask.palletsprojects.com/en/2.2.x/errorhandling/
# @app.errorhandler(HTTPException)
# def handle_exception(e):
#     """Return JSON instead of HTML for HTTP errors."""
#     # start with the correct headers and status code from the error
#     response = e.get_response()
#     # replace the body with JSON
#     response.data = json.dumps({
#         "code": e.code,
#         "name": e.name,
#         "description": e.description,
#     })
#     response.content_type = "application/json"
#     return response



# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted; changed to 6574 per tutorial video
    app.run(port=6779, debug=True)
