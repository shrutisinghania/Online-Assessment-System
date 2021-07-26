-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 21, 2018 at 09:04 AM
-- Server version: 10.1.26-MariaDB
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `online_assesment`
--

-- --------------------------------------------------------

--
-- Table structure for table `details`
--

CREATE TABLE `details` (
  `email` varchar(50) NOT NULL,
  `stream` varchar(50) NOT NULL,
  `university` varchar(50) NOT NULL,
  `yearofpassing` int(50) NOT NULL,
  `mobileno` int(20) NOT NULL,
  `address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `exam`
--

CREATE TABLE `exam` (
  `email` varchar(100) NOT NULL,
  `1given` varchar(50) NOT NULL DEFAULT '0',
  `2given` varchar(50) NOT NULL DEFAULT '0',
  `3given` varchar(50) NOT NULL DEFAULT '0',
  `4given` varchar(50) NOT NULL DEFAULT '0',
  `5given` varchar(50) NOT NULL DEFAULT '0',
  `6given` varchar(50) NOT NULL DEFAULT '0',
  `7given` varchar(50) NOT NULL DEFAULT '0',
  `8given` varchar(50) NOT NULL DEFAULT '0',
  `9given` varchar(50) NOT NULL DEFAULT '0',
  `10given` varchar(50) NOT NULL DEFAULT '0',
  `finalscore` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `exam`
--

INSERT INTO `exam` (`email`, `1given`, `2given`, `3given`, `4given`, `5given`, `6given`, `7given`, `8given`, `9given`, `10given`, `finalscore`) VALUES
('sh2@gmzil.com', '10', '10', '0', '10', '10', '10', '10', '10', '10', '10', 90),
('shrutisinghania75@gmail.com', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 0),
('xx@cc', '10', '10', '10', '10', '10', '10', '10', '10', '0', '0', 80);

-- --------------------------------------------------------

--
-- Table structure for table `exam2`
--

CREATE TABLE `exam2` (
  `email` varchar(50) NOT NULL,
  `1given` varchar(50) NOT NULL,
  `2given` varchar(50) NOT NULL,
  `3given` varchar(50) NOT NULL,
  `4given` varchar(50) NOT NULL,
  `5given` varchar(50) NOT NULL,
  `6given` varchar(50) NOT NULL,
  `7given` varchar(50) NOT NULL,
  `8given` varchar(50) NOT NULL,
  `9given` varchar(50) NOT NULL,
  `10given` varchar(50) NOT NULL,
  `finalscore` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `exam2`
--

INSERT INTO `exam2` (`email`, `1given`, `2given`, `3given`, `4given`, `5given`, `6given`, `7given`, `8given`, `9given`, `10given`, `finalscore`) VALUES
('sh2@gmzil.com', '10', '10', '0', '0', '0', '0', '0', '10', '0', '0', 30),
('shrutisinghania75@gmail.com', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 0);

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `name` varchar(100) NOT NULL,
  `college` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `gender` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`name`, `college`, `email`, `password`, `gender`) VALUES
('shru', 'tict', 'aadd@vhjk', 'None', 'male'),
('shru', 'tict', 'gjj@hj', '12345', 'male'),
('shru', 'tict', 'iuui@fgh', '12345', 'female'),
('None', 'None', 'None', 'None', 'male'),
('shru', 'tict', 'sh2@gmzil.com', '12345', 'female'),
('Shruti Singhania', 'msit', 'shrutisinghania75@gmail.com', '12345', 'female'),
('shru', 'tict', 'xx@cc', '12345', 'female');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `details`
--
ALTER TABLE `details`
  ADD KEY `email` (`email`);

--
-- Indexes for table `exam`
--
ALTER TABLE `exam`
  ADD PRIMARY KEY (`email`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `email_2` (`email`);

--
-- Indexes for table `exam2`
--
ALTER TABLE `exam2`
  ADD PRIMARY KEY (`email`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `registration`
--
ALTER TABLE `registration`
  ADD PRIMARY KEY (`email`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `details`
--
ALTER TABLE `details`
  ADD CONSTRAINT `email` FOREIGN KEY (`email`) REFERENCES `registration` (`email`);

--
-- Constraints for table `exam`
--
ALTER TABLE `exam`
  ADD CONSTRAINT `exam_ibfk_1` FOREIGN KEY (`email`) REFERENCES `registration` (`email`);

--
-- Constraints for table `exam2`
--
ALTER TABLE `exam2`
  ADD CONSTRAINT `exam2_ibfk_1` FOREIGN KEY (`email`) REFERENCES `registration` (`email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
