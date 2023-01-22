-- phpMyAdmin SQL Dump
-- version 5.2.0-1.el7.remi
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 22, 2023 at 04:13 AM
-- Server version: 10.6.11-MariaDB-log
-- PHP Version: 8.2.1

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
  `age` varchar(45) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `mission_role` varchar(45) DEFAULT NULL,
  `days_in_space` double DEFAULT NULL,
  `Spacecraft_id_satellite` int(11) NOT NULL,
  `Spacecraft_Planetary Objects_id_object` int(11) NOT NULL,
  `Spacecraft_Planetary Objects_id_object1` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Clients`
--

CREATE TABLE `Clients` (
  `id_client` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `contribution_amount` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Missions`
--

CREATE TABLE `Missions` (
  `id_mission` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `contract_revenues` float DEFAULT NULL,
  `contract_costs` float DEFAULT NULL,
  `contract_profit` float DEFAULT NULL,
  `external` tinyint(4) DEFAULT NULL,
  `Spacecraft_id_satellite` int(11) NOT NULL,
  `Spacecraft_Planetary Objects_id_object` int(11) NOT NULL,
  `Spacecraft_Planetary Objects_id_object1` int(11) NOT NULL,
  `Clients_id_client` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Parts`
--

CREATE TABLE `Parts` (
  `id_part` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `manufacturer` varchar(45) DEFAULT NULL,
  `mass_kg` varchar(45) DEFAULT NULL,
  `cost` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Parts_has_Spacecraft`
--

CREATE TABLE `Parts_has_Spacecraft` (
  `Parts_id_satellite` int(11) NOT NULL,
  `Spacecraft_id_satellite` int(11) NOT NULL,
  `Spacecraft_Planetary Objects_id_object` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Planetary Objects`
--

CREATE TABLE `Planetary Objects` (
  `id_planetary_object` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `mass` varchar(45) DEFAULT NULL,
  `distance_from_sun` float DEFAULT NULL,
  `isPlanet` varchar(45) DEFAULT NULL,
  `isMoon` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Spacecraft`
--

CREATE TABLE `Spacecraft` (
  `id_spacecraft` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `Planetary Objects_id_object` int(11) NOT NULL,
  `Planetary Objects_id_object1` int(11) NOT NULL,
  `InOrbit?` tinyint(4) DEFAULT NULL,
  `Launched?` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Astronauts`
--
ALTER TABLE `Astronauts`
  ADD PRIMARY KEY (`id_astronaut`,`Spacecraft_id_satellite`,`Spacecraft_Planetary Objects_id_object`,`Spacecraft_Planetary Objects_id_object1`),
  ADD KEY `fk_Astronauts_Spacecraft1_idx` (`Spacecraft_id_satellite`,`Spacecraft_Planetary Objects_id_object`,`Spacecraft_Planetary Objects_id_object1`);

--
-- Indexes for table `Clients`
--
ALTER TABLE `Clients`
  ADD PRIMARY KEY (`id_client`);

--
-- Indexes for table `Missions`
--
ALTER TABLE `Missions`
  ADD PRIMARY KEY (`id_mission`,`Spacecraft_id_satellite`,`Spacecraft_Planetary Objects_id_object`,`Spacecraft_Planetary Objects_id_object1`,`Clients_id_client`),
  ADD KEY `fk_Missions_Spacecraft1_idx` (`Spacecraft_id_satellite`,`Spacecraft_Planetary Objects_id_object`,`Spacecraft_Planetary Objects_id_object1`),
  ADD KEY `fk_Missions_Clients1_idx` (`Clients_id_client`);

--
-- Indexes for table `Parts`
--
ALTER TABLE `Parts`
  ADD PRIMARY KEY (`id_part`);

--
-- Indexes for table `Parts_has_Spacecraft`
--
ALTER TABLE `Parts_has_Spacecraft`
  ADD PRIMARY KEY (`Parts_id_satellite`,`Spacecraft_id_satellite`,`Spacecraft_Planetary Objects_id_object`),
  ADD KEY `fk_Parts_has_Spacecraft_Spacecraft1_idx` (`Spacecraft_id_satellite`,`Spacecraft_Planetary Objects_id_object`),
  ADD KEY `fk_Parts_has_Spacecraft_Parts1_idx` (`Parts_id_satellite`);

--
-- Indexes for table `Planetary Objects`
--
ALTER TABLE `Planetary Objects`
  ADD PRIMARY KEY (`id_planetary_object`);

--
-- Indexes for table `Spacecraft`
--
ALTER TABLE `Spacecraft`
  ADD PRIMARY KEY (`id_spacecraft`,`Planetary Objects_id_object`,`Planetary Objects_id_object1`),
  ADD KEY `fk_Spacecraft_Planetary Objects1_idx` (`Planetary Objects_id_object1`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Astronauts`
--
ALTER TABLE `Astronauts`
  MODIFY `id_astronaut` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Clients`
--
ALTER TABLE `Clients`
  MODIFY `id_client` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Missions`
--
ALTER TABLE `Missions`
  MODIFY `id_mission` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Parts`
--
ALTER TABLE `Parts`
  MODIFY `id_part` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Planetary Objects`
--
ALTER TABLE `Planetary Objects`
  MODIFY `id_planetary_object` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Spacecraft`
--
ALTER TABLE `Spacecraft`
  MODIFY `id_spacecraft` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Astronauts`
--
ALTER TABLE `Astronauts`
  ADD CONSTRAINT `fk_Astronauts_Spacecraft1` FOREIGN KEY (`Spacecraft_id_satellite`,`Spacecraft_Planetary Objects_id_object`,`Spacecraft_Planetary Objects_id_object1`) REFERENCES `Spacecraft` (`id_spacecraft`, `Planetary Objects_id_object`, `Planetary Objects_id_object1`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `Missions`
--
ALTER TABLE `Missions`
  ADD CONSTRAINT `fk_Missions_Clients1` FOREIGN KEY (`Clients_id_client`) REFERENCES `Clients` (`id_client`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Missions_Spacecraft1` FOREIGN KEY (`Spacecraft_id_satellite`,`Spacecraft_Planetary Objects_id_object`,`Spacecraft_Planetary Objects_id_object1`) REFERENCES `Spacecraft` (`id_spacecraft`, `Planetary Objects_id_object`, `Planetary Objects_id_object1`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `Parts_has_Spacecraft`
--
ALTER TABLE `Parts_has_Spacecraft`
  ADD CONSTRAINT `fk_Parts_has_Spacecraft_Parts1` FOREIGN KEY (`Parts_id_satellite`) REFERENCES `Parts` (`id_part`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Parts_has_Spacecraft_Spacecraft1` FOREIGN KEY (`Spacecraft_id_satellite`,`Spacecraft_Planetary Objects_id_object`) REFERENCES `Spacecraft` (`id_spacecraft`, `Planetary Objects_id_object`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `Spacecraft`
--
ALTER TABLE `Spacecraft`
  ADD CONSTRAINT `fk_Spacecraft_Planetary Objects1` FOREIGN KEY (`Planetary Objects_id_object1`) REFERENCES `Planetary Objects` (`id_planetary_object`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
