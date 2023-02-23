
--SELECT Clients data
SELECT *
FROM Clients
WHERE name = :name_from_user;

--SELECT Astronaut data
SELECT *
FROM Astronauts
WHERE name = :name_from_user;

--SELECT Mission data
SELECT *
FROM Missions
WHERE name = :name_from_user;

--SELECT Spacecrafts data
SELECT *
FROM Spacecrafts
WHERE name = :name_from_user;

--SELECT Planetary_objects data
SELECT *
FROM Planetary_Objects
WHERE name = :name_from_user;

--SELECT Parts data
SELECT *
FROM parts
WHERE name = :name_from_user;

--get parts by spacecraft name
SELECT * 
FROM Spacecraft_has_Parts
WHERE id_spacecraft = :id;

--INSERT new Client
INSERT INTO Clients (Ein, name, contribution_amount, address)
Values (:ein, :name_from_user, :new_contribution_amount, :new_address);

--INSERT new Mission
INSERT INTO Missions (name, contract_revenue, contract_costs, is_external, mission_description)
VALUES (:name_from_user, :new_contract_revenue, :new_contract_costs, :is_external, :mission_description);

--INSERT new Spacecraft
INSERT INTO Spacecrafts (name, in_orbit, launched, delta_v_remaining, mission_elapsed_time_days)
VALUES (:name_from_user, :in_orbit, :launched, :delta_v_remaining, 0);

--INSERT new Astronaut
INSERT INTO Astronauts (name, age, gender, mission_role)
VALUE (:name_from_user, :age_input, :gender_input, :mission_role);

--INSERT new Planetary_Object
INSERT INTO Planetary_Objects (name, surface_gravity_g, avg_distance_from_sun_au, is_planet, is_moon)
VALUES (:name, :surface_gravity_g, :avg_distance_from_sun_au, :is_planet, :is_moon);

--INSERT new Part
INSERT INTO Parts (name, manufacturer, mass_kg, cost, part_description)
VALUES (:name, :manufacturer, :mass_kg, :cost, :part_description);

--INSERT into intersection table Spacecraft_has_parts
INSERT INTO Spacecraft_has_Parts (id_spacecraft, id_part)
SELECT s.id_spacecraft, p.id_part
FROM Spacecrafts s, Parts p
WHERE s.id_spacecraft = :id_spacecraft and p.id_part = :id_part;

--add Astronaut to spacecraft
UPDATE Astronauts
SET id_spacecraft = :id_input
WHERE name = :selected_astronaut_name;

--update client by id
UPDATE Client
SET Ein=:new_ein, name=:new_name, contribution_amount=:new_contribution_amount,  address=:new_address
WHERE id_client = :id;

--update mission by id
UPDATE Missions
SET name=:new_name, contract_revenue=:new_contract_revenue, contract_costs=:new_contract_cost, is_external=:new_is_external, mission_description=:new_mission_description
WHERE id_mission = :id;

--update astronaut by id
UPDATE Astronauts
SET name=:new_name, age=:new_age, gender=:new_gender, mission_role=:mission_role
WHERE id_astronaut =:id;

--update part by id
UPDATE Parts
SET name=:new_name, manufacturer=:new_manufacturer, mass_kg=:new_mass_kg, cost=:new_cost, part_description=:new_part_description
WHERE id_part =:id;

--update planetary_object by id
UPDATE Planetary_Objects
SET name=:new_name, surface_gravity_g=:new_surface_g, avg_distance_from_sun_au=:new_dist, is_planet=:new_is_planet, is_moon=:new_is_moon
WHERE id_planetary_object = :id;

UPDATE Spacecrafts
SET name=:new_name, in_orbit=:new_in_orbit, launched=:new_launched, delta_v_remaining=:new_delta_v_remaining, mission_elapsed_time_days=:new_time_elapsed
WHERE id_spacecraft = :id;

--delete discontinued part M:M
DELETE FROM Spacecraft_has_Parts
WHERE id_spacecraft = :id_spacecraft_selected and id_part = :id_part_selected;

--delete astronaut from Astronauts
DELETE FROM Astronauts
WHERE id_astronaut = :id;

--delete client from Clients
DELETE FROM Clients
WHERE id_client = :id;

--delete mission from Missions
DELETE FROM Missions
WHERE id_mission = :id;

--delete part from Parts
DELETE FROM Parts
WHERE id_part = :id;

--delete planetary_object from Planetary_Objects
DELETE FROM Planetary_Objects
WHERE id_planetary_object = :id;

--delete spacecraft from Spacecrafts
DELETE FROM Spacecrafts
WHERE id_spacecraft = :id;
