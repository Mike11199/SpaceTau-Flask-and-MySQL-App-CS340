from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request, jsonify

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


@app.route('/missions')
def missions_page():
    return render_template("missions.jinja")

@app.route('/parts')
def parts_page():

    query = "SELECT * FROM Parts;"
    cur = mysql.connection.cursor()
    cur.execute(query)
    parts_data = cur.fetchall()

    return render_template("parts.jinja", parts_data=parts_data)

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

@app.route('/planetary-objects')
def planetary_objects_page():
    return render_template("planetary_objects.jinja")

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

    if request.method == "POST":
        if request.form.get('filter_relationships'):
            print("Got filter form request")
            filter_id = request.form['spacecraft_select_option']
            print(filter_id)
            query0 = """
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
            cur.execute(query0, (filter_id))
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

        #if request.form.get('addRelationship'):
        part_id = request.form["part_name"]
        spacecraft_id = request.form["spacecraft_name"]
        print("Add relationship debugging\n")
        print(part_id)
        print(spacecraft_id)
        # id_part_query = "SELECT id_part FROM Parts WHERE name=%s"
        # cur = mysql.connection.cursor()
        # cur.execute(id_part_query, (part_name))
        # id_part = cur.fetchall()
        # id_spacecraft_query = "SELECT id_part FROM Parts WHERE name=%s"
        # cur = mysql.connection.cursor()
        # cur.execute(id_spacecraft_query, (spacecraft_name))
        # id_spacecraft = cur.fetchall()
        add_relationship_query = "INSERT INTO Spacecraft_has_Parts (id_spacecraft, id_part) SELECT s.id_spacecraft, p.id_part FROM Spacecrafts s, Parts p WHERE s.id_spacecraft=%s AND p.id_part=%s;"
        cur = mysql.connection.cursor()
        cur.execute(add_relationship_query, (spacecraft_id, part_id))
        mysql.connection.commit()
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




# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted; changed to 6574 per tutorial video
    app.run(port=6779, debug=True)
