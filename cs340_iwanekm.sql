-- phpMyAdmin SQL Dump
-- version 5.2.0-1.el7.remi
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 08, 2023 at 02:12 PM
-- Server version: 10.6.11-MariaDB-log
-- PHP Version: 8.2.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cs340_iwanekm`
--

-- --------------------------------------------------------

--
-- Table structure for table `Astronauts`
--

CREATE TABLE `Astronauts` (
  `id_astronaut` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `mission_role` varchar(45) DEFAULT NULL,
  `id_spacecraft` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Dumping data for table `Astronauts`
--

INSERT INTO `Astronauts` (`id_astronaut`, `name`, `age`, `gender`, `mission_role`, `id_spacecraft`) VALUES
(1, 'Buzz Aldrin', 93, 'Male', 'Pilot', 6),
(2, 'Joe Acaba', 55, 'Male', 'Engineer', 6),
(3, 'Kayla Barron', 35, 'Female', 'Specialist', 6),
(4, 'Stephen Bowen', 58, 'Male', 'Specialist', NULL),
(5, 'Tracy Dyson', 53, 'Female', 'Specialist', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `Clients`
--

CREATE TABLE `Clients` (
  `id_client` int(11) NOT NULL,
  `EIN` double DEFAULT NULL,
  `name` varchar(45) NOT NULL,
  `contribution_amount` decimal(19,2) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Dumping data for table `Clients`
--

INSERT INTO `Clients` (`id_client`, `EIN`, `name`, `contribution_amount`, `address`) VALUES
(1, 521610424, 'Lockheed Martin', '52300300.00', '3251 Hanover St, Palo Alto, CA 94304'),
(2, 133243459, 'Airbus', '99800000.00', '1855 Innovation Blvd. Wichita, KS 67208 - U.S'),
(3, 910425694, 'Boeing', '677000000.00', '19000 NE Sandy Blvd, Portland, OR 97230'),
(4, 912166281, 'Millennium Space Systems', '64000000.00', '2265 E El Segundo Blvd, El Segundo, CA 90245'),
(5, 951055798, 'Northrop Grumman', '32500000.00', '2980 Fairview Park Drive, Falls Church, VA 22'),
(6, 910425797, 'NASA', '1000000000.00', '4800 Oak Grove Dr, Pasadena, CA 91109'),
(7, 962653562, 'Garmin', '900000.00', '1200 E 151st St, Olathe, KS'),
(8, 951055998, 'ESA', '1200000000.00', '24 rue du Général Bertrand CS 30798 Paris');

-- --------------------------------------------------------

--
-- Table structure for table `Missions`
--

CREATE TABLE `Missions` (
  `id_mission` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `contract_revenues` decimal(19,2) DEFAULT NULL,
  `contract_costs` decimal(19,2) DEFAULT NULL,
  `contract_profit` decimal(19,2) GENERATED ALWAYS AS (`contract_revenues` - `contract_costs`) STORED,
  `is_external` tinyint(4) DEFAULT NULL,
  `mission_description` varchar(300) DEFAULT NULL,
  `id_spacecraft` int(11) DEFAULT NULL,
  `id_client` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Dumping data for table `Missions`
--

INSERT INTO `Missions` (`id_mission`, `name`, `contract_revenues`, `contract_costs`, `is_external`, `mission_description`, `id_spacecraft`, `id_client`) VALUES
(1, 'Garmin GPS Network Launch Service', '152300000.00', '37520000.00', 1, 'A mission to launch a satellite for the Garmin GPS network into a geosynchronous orbit around Earth.  ', 1, 7),
(2, 'Space Sentry System', '5000000.00', '3450000.00', 1, 'A mission to lauch multiple low orbit defense satellites.', 3, 1),
(3, 'Polar Icecap Observatory', '450000000.00', '92300000.00', 1, 'Track and Survey ice levels at the north pole.', 2, 6),
(4, 'Jupiter Ultraviolet Exploration', '799000000.00', '487000000.00', 1, 'A mission with the goal of capturing the most detailed ultraviolet data from jupiter ever.', 4, 6),
(5, 'Universal Iodine Detection', '1000000.00', '7500000.00', 0, 'A mission to deploy a new space telescope that specifically detects iodine.', 5, 8),
(6, 'Lunar Gateway', '3000000000.00', '1250000000.00', 1, 'A mission to launch and maintain an extraterrestrial space station in lunar orbit.  With associated craft and cargo resupply.  ', 6, 6);

-- --------------------------------------------------------

--
-- Table structure for table `Parts`
--

CREATE TABLE `Parts` (
  `id_part` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `manufacturer` varchar(45) NOT NULL,
  `mass_kg` decimal(19,2) NOT NULL,
  `cost` decimal(19,2) NOT NULL,
  `part_description` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Dumping data for table `Parts`
--

INSERT INTO `Parts` (`id_part`, `name`, `manufacturer`, `mass_kg`, `cost`, `part_description`) VALUES
(1, 'Roll Out Solar Array (ROSA)', 'Redwire', '325.00', '17000000.00', '120 KW solar array that is 20 percent lighter and 1/4th the volume of rigid panel arrays.\r\n\r\nhttps://spaceflightnow.com/2022/12/03/iss-eva-82/#:~:text=NASA%20is%20upgrading%20the%20space,station\'s%20eight%20original%20solar%20panels.'),
(2, 'RDR 68 Reaction Wheel', 'Collins Aerospace', '8.00', '50000.00', 'The wheels accommodate the requirements of attitude control systems for spacecraft weighing between 30 kg and 7,000 kg.\r\n\r\nhttps://www.satcatalog.com/component/rdr-68-3/'),
(3, 'PEPT-200 Diaphragm Propellant Tank', 'Rafael Advanced Defense Systems', '0.91', '2000.00', 'Spherical tank used to store monopropellant (Krypton/Hydrazine) for RCS thrusters. \r\n\r\nhttps://www.satcatalog.com/component/pept-200-diaphragm-propellant-tank/'),
(4, 'R-800 Hall Effect Thruster (HET)', 'Rafael Space Propulsion', '1.50', '100000.00', 'A Xenon/Krypton ion thruster for low mass, less than 1000kg, satellites.  Produces 23-50 mN (Millinewtons) of thrust.'),
(5, 'Smallsat Perimeter Truss (SPT) Reflector ', 'L3Harris', '18.60', '75000.00', 'HCR is a high-accuracy, large aperture antenna optimized accurate enough for high\r\nfrequency missions (e.g. Ka or V band). \r\n https://www.l3harris.com/sites/default/files/2020-09/l3harris-smallsat-perimeter-truss-spec-sheet-sas.pdf'),
(6, 'Crew Dragon Manned Capsule', 'SpaceX', '6000.00', '100000000.00', 'A manned space capsule capable of carrying 3,307 kg or 7,291 lbs of cargo to the ISS, and up to 4 astronauts. '),
(7, 'LIFE (Large Integrated Flexible Environment) ', 'Sierra Space', '5000.00', '40000000.00', 'Inflatable habitat that expands in-orbit to a large structure that is three stories tall, and 27 feet in diameter. \r\n\r\nhttps://www.sierraspace.com/space-destinations/life-space-habitat/');

-- --------------------------------------------------------

--
-- Table structure for table `Planetary_Objects`
--

CREATE TABLE `Planetary_Objects` (
  `id_planetary_object` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `surface_gravity_g` decimal(19,2) NOT NULL,
  `avg_distance_from_sun_au` decimal(19,2) NOT NULL,
  `is_planet` tinyint(4) DEFAULT NULL,
  `is_moon` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Dumping data for table `Planetary_Objects`
--

INSERT INTO `Planetary_Objects` (`id_planetary_object`, `name`, `surface_gravity_g`, `avg_distance_from_sun_au`, `is_planet`, `is_moon`) VALUES
(1, 'Mercury', '0.38', '0.39', 1, 0),
(2, 'Venus', '0.91', '0.72', 1, 0),
(3, 'Earth', '1.00', '1.00', 1, 0),
(4, 'Mars', '0.38', '1.52', 1, 0),
(5, 'Jupiter', '2.36', '5.20', 1, 0),
(6, 'Saturn', '0.92', '9.57', 1, 0),
(7, 'Uranus', '0.89', '19.17', 1, 0),
(8, 'Neptune', '1.12', '30.18', 1, 0),
(9, 'Pluto', '0.07', '39.48', 0, 0),
(10, 'Moon (Earth)', '0.17', '1.00', 0, 1),
(11, 'Dimorphos (Asteroid)', '0.00', '1.62', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `Spacecrafts`
--

CREATE TABLE `Spacecrafts` (
  `id_spacecraft` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `in_orbit` tinyint(4) DEFAULT NULL,
  `launched` tinyint(4) DEFAULT NULL,
  `id_planetary_object` int(11) NOT NULL,
  `delta_v_remaining` decimal(19,2) DEFAULT NULL,
  `mission_elapsed_time_days` decimal(19,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Dumping data for table `Spacecrafts`
--

INSERT INTO `Spacecrafts` (`id_spacecraft`, `name`, `in_orbit`, `launched`, `id_planetary_object`, `delta_v_remaining`, `mission_elapsed_time_days`) VALUES
(1, 'Garmin GPS Satellite 34', 1, 1, 3, '500.00', '43.00'),
(2, 'Artic Glacier Satellite 02', 1, 1, 3, '240.00', '105.00'),
(3, 'Sentry', 0, 0, 4, '600.00', '21.00'),
(4, 'Extraterrestrial Ultraviolet Explorer', 0, 0, 5, '100.00', '212.00'),
(5, 'Iodine Space Telescope', 0, 1, 8, '355.00', '149.00'),
(6, 'Lunar Gateway Station', 1, 1, 3, '500.00', '146.00');

-- --------------------------------------------------------

--
-- Table structure for table `Spacecraft_has_Parts`
--

CREATE TABLE `Spacecraft_has_Parts` (
  `id_spacecraft` int(11) NOT NULL,
  `id_part` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Dumping data for table `Spacecraft_has_Parts`
--

INSERT INTO `Spacecraft_has_Parts` (`id_spacecraft`, `id_part`) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(6, 1),
(6, 7);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Astronauts`
--
ALTER TABLE `Astronauts`
  ADD PRIMARY KEY (`id_astronaut`),
  ADD UNIQUE KEY `id_astronaut_UNIQUE` (`id_astronaut`),
  ADD KEY `fk_Astronauts_Spacecraft1_idx` (`id_spacecraft`);

--
-- Indexes for table `Clients`
--
ALTER TABLE `Clients`
  ADD PRIMARY KEY (`id_client`),
  ADD UNIQUE KEY `id_client_UNIQUE` (`id_client`);

--
-- Indexes for table `Missions`
--
ALTER TABLE `Missions`
  ADD PRIMARY KEY (`id_mission`),
  ADD UNIQUE KEY `id_mission_UNIQUE` (`id_mission`),
  ADD UNIQUE KEY `name_UNIQUE` (`name`),
  ADD KEY `fk_Missions_Spacecraft1_idx` (`id_spacecraft`),
  ADD KEY `fk_Missions_Clients1_idx` (`id_client`);

--
-- Indexes for table `Parts`
--
ALTER TABLE `Parts`
  ADD PRIMARY KEY (`id_part`),
  ADD UNIQUE KEY `id_part_UNIQUE` (`id_part`);

--
-- Indexes for table `Planetary_Objects`
--
ALTER TABLE `Planetary_Objects`
  ADD PRIMARY KEY (`id_planetary_object`),
  ADD UNIQUE KEY `id_planetary_object_UNIQUE` (`id_planetary_object`);

--
-- Indexes for table `Spacecrafts`
--
ALTER TABLE `Spacecrafts`
  ADD PRIMARY KEY (`id_spacecraft`,`id_planetary_object`),
  ADD UNIQUE KEY `id_spacecraft_UNIQUE` (`id_spacecraft`),
  ADD KEY `fk_Spacecraft_Planetary_Objects1_idx` (`id_planetary_object`);

--
-- Indexes for table `Spacecraft_has_Parts`
--
ALTER TABLE `Spacecraft_has_Parts`
  ADD PRIMARY KEY (`id_spacecraft`,`id_part`),
  ADD KEY `fk_Spacecraft_has_Parts_Parts1_idx` (`id_part`),
  ADD KEY `fk_Spacecraft_has_Parts_Spacecraft1_idx` (`id_spacecraft`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Astronauts`
--
ALTER TABLE `Astronauts`
  MODIFY `id_astronaut` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `Clients`
--
ALTER TABLE `Clients`
  MODIFY `id_client` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `Missions`
--
ALTER TABLE `Missions`
  MODIFY `id_mission` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `Parts`
--
ALTER TABLE `Parts`
  MODIFY `id_part` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `Planetary_Objects`
--
ALTER TABLE `Planetary_Objects`
  MODIFY `id_planetary_object` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `Spacecrafts`
--
ALTER TABLE `Spacecrafts`
  MODIFY `id_spacecraft` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Astronauts`
--
ALTER TABLE `Astronauts`
  ADD CONSTRAINT `fk_Astronauts_Spacecraft1` FOREIGN KEY (`id_spacecraft`) REFERENCES `Spacecrafts` (`id_spacecraft`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `Missions`
--
ALTER TABLE `Missions`
  ADD CONSTRAINT `fk_Missions_Clients1` FOREIGN KEY (`id_client`) REFERENCES `Clients` (`id_client`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Missions_Spacecraft1` FOREIGN KEY (`id_spacecraft`) REFERENCES `Spacecrafts` (`id_spacecraft`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `Spacecrafts`
--
ALTER TABLE `Spacecrafts`
  ADD CONSTRAINT `fk_Spacecraft_Planetary_Objects1` FOREIGN KEY (`id_planetary_object`) REFERENCES `Planetary_Objects` (`id_planetary_object`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `Spacecraft_has_Parts`
--
ALTER TABLE `Spacecraft_has_Parts`
  ADD CONSTRAINT `fk_Spacecraft_has_Parts_Parts1` FOREIGN KEY (`id_part`) REFERENCES `Parts` (`id_part`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Spacecraft_has_Parts_Spacecraft1` FOREIGN KEY (`id_spacecraft`) REFERENCES `Spacecrafts` (`id_spacecraft`) ON DELETE CASCADE ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
