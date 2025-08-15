-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 15, 2025 at 12:28 PM
-- Server version: 10.6.15-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ir_sensor_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `ir_data`
--

CREATE TABLE `ir_data` (
  `id` int(11) NOT NULL,
  `ir_status` int(11) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ir_data`
--

INSERT INTO `ir_data` (`id`, `ir_status`, `timestamp`) VALUES
(1, 0, '2025-08-15 08:03:15'),
(2, 0, '2025-08-15 08:03:16'),
(3, 1, '2025-08-15 08:03:17'),
(4, 0, '2025-08-15 08:03:18'),
(5, 1, '2025-08-15 08:03:19'),
(6, 1, '2025-08-15 08:03:20'),
(7, 0, '2025-08-15 08:03:21'),
(8, 1, '2025-08-15 08:03:22'),
(9, 0, '2025-08-15 08:03:23'),
(10, 0, '2025-08-15 08:03:24'),
(11, 0, '2025-08-15 08:06:30'),
(12, 0, '2025-08-15 08:06:32'),
(13, 0, '2025-08-15 08:06:33'),
(14, 0, '2025-08-15 08:06:34'),
(15, 0, '2025-08-15 08:06:35'),
(16, 1, '2025-08-15 08:06:36'),
(17, 0, '2025-08-15 08:06:37'),
(18, 0, '2025-08-15 08:06:38'),
(19, 1, '2025-08-15 08:06:39'),
(20, 0, '2025-08-15 08:06:40');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ir_data`
--
ALTER TABLE `ir_data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `ir_data`
--
ALTER TABLE `ir_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
