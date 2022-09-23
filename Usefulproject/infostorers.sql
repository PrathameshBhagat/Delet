-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 23, 2022 at 09:48 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `infostorers`
--

-- --------------------------------------------------------

--
-- Table structure for table `indivisual`
--

CREATE TABLE `indivisual` (
  `id` int(50) NOT NULL,
  `Indexe` int(50) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Father` varchar(50) NOT NULL,
  `Surname` varchar(50) NOT NULL,
  `Mother` varchar(50) NOT NULL,
  `Phone` int(11) NOT NULL,
  `PFather` int(11) NOT NULL,
  `PMother` int(11) NOT NULL,
  `PExtra` int(11) NOT NULL,
  `DOB` date NOT NULL,
  `CPlaces` text NOT NULL,
  `PInstitutions` text NOT NULL,
  `CInstitution` text NOT NULL,
  `FInstitution` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `indivisual`
--

INSERT INTO `indivisual` (`id`, `Indexe`, `Name`, `Father`, `Surname`, `Mother`, `Phone`, `PFather`, `PMother`, `PExtra`, `DOB`, `CPlaces`, `PInstitutions`, `CInstitution`, `FInstitution`) VALUES
(3, 0, '', '', '', '', 0, 0, 0, 0, '0000-00-00', '', '', '', ''),
(5, 45, 'Hello', 'Prathamesh', 'adc', 'sacf', 123, 456, 789, 159, '2002-06-08', 'com', 'past', 'current', 'fut'),
(6, 45, 'Hello', 'Prathamesh', 'adc', 'sacf', 123, 456, 789, 159, '2002-06-08', 'com', 'past', 'current', 'fut'),
(7, 45, 'Hello', 'Prathamesh', 'adc', 'sacf', 123, 456, 789, 159, '2002-06-08', 'com', 'past', 'current', 'fut'),
(8, 45, 'Hello', 'Prathamesh', 'adc', 'sacf', 123, 456, 789, 159, '2002-08-06', 'com', 'past', 'current', 'fut'),
(9, 45, 'Hello', 'Prathamesh', 'adc', 'sacf', 123, 456, 789, 159, '2002-08-06', 'com', 'past', 'current', 'fut'),
(10, 45, 'Hello', 'Prathamesh', 'adc', 'sacf', 123, 456, 789, 159, '2006-08-06', 'com', 'past', 'current', 'fut'),
(11, 0, '', '', '', '', 0, 0, 0, 0, '2022-12-01', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `relatives`
--

CREATE TABLE `relatives` (
  `id` int(11) NOT NULL,
  `Relation` text NOT NULL,
  `Name` text NOT NULL,
  `Surname` text NOT NULL,
  `Indexe's` text NOT NULL,
  `Phone` int(11) NOT NULL,
  `Places` text NOT NULL,
  `PInstitution` text NOT NULL,
  `CInstitution` text NOT NULL,
  `FInstitution` text NOT NULL,
  `DOB` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `indivisual`
--
ALTER TABLE `indivisual`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `relatives`
--
ALTER TABLE `relatives`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `indivisual`
--
ALTER TABLE `indivisual`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `relatives`
--
ALTER TABLE `relatives`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
