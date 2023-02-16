
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
INSERT INTO Parts (name, maufacturer, mass_kg, cost, part_description)
VALUES (:name, :maufacturer, :mass_kg, :cost, :part_description);

--add Astronaut to spacecraft
UPDATE Astronauts
SET id_spacecraft = :id_input
WHERE name = :selected_astronaut_name;

--update client contribution amount
UPDATE Client
SET contribution_amount = :new_contribution_amount
WHERE client_id = :id;

--delete discontinued part M:M
DELETE FROM Space_craft_has_Parts
WHERE id_spacecraft = :id_spacecraft_selected and id_part = :id_part_selected;
