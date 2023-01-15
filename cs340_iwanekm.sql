-- phpMyAdmin SQL Dump
-- version 5.2.0-1.el7.remi
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 14, 2023 at 12:39 AM
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
-- Table structure for table `planets`
--

CREATE TABLE `planets` (
  `id_planet` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `mass_trillion_trillion_kg` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Dumping data for table `planets`
--

INSERT INTO `planets` (`id_planet`, `name`, `mass_trillion_trillion_kg`) VALUES
(1, 'Mercury', '0.330'),
(2, 'Venus', '4.87'),
(3, 'Earth', '5.97'),
(4, 'Mars', '.642'),
(5, 'Jupiter', '1898'),
(6, 'Saturn', '568'),
(7, 'Uranus', '86.8'),
(8, 'Neptune', '102'),
(9, 'Pluto', '.0130'),
(10, NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `satellites`
--

CREATE TABLE `satellites` (
  `id_satellite` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `manufacturer` varchar(45) DEFAULT NULL,
  `planets_id_planet` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `planets`
--
ALTER TABLE `planets`
  ADD PRIMARY KEY (`id_planet`);

--
-- Indexes for table `satellites`
--
ALTER TABLE `satellites`
  ADD PRIMARY KEY (`id_satellite`,`planets_id_planet`),
  ADD KEY `fk_satellites_planets_idx` (`planets_id_planet`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `planets`
--
ALTER TABLE `planets`
  MODIFY `id_planet` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `satellites`
--
ALTER TABLE `satellites`
  MODIFY `id_satellite` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `satellites`
--
ALTER TABLE `satellites`
  ADD CONSTRAINT `fk_satellites_planets` FOREIGN KEY (`planets_id_planet`) REFERENCES `planets` (`id_planet`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
