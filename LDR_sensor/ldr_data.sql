-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 15, 2025 at 12:18 PM
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
-- Database: `ldr`
--

-- --------------------------------------------------------

--
-- Table structure for table `ldr_data`
--

CREATE TABLE `ldr_data` (
  `id` int(11) NOT NULL,
  `ldr_value` int(11) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ldr_data`
--

INSERT INTO `ldr_data` (`id`, `ldr_value`, `timestamp`) VALUES
(1, 900, '2025-08-15 09:53:10'),
(2, 977, '2025-08-15 09:53:11'),
(3, 471, '2025-08-15 09:53:12'),
(4, 205, '2025-08-15 09:53:13'),
(5, 954, '2025-08-15 09:53:14'),
(6, 933, '2025-08-15 09:53:15'),
(7, 653, '2025-08-15 09:53:16'),
(8, 68, '2025-08-15 09:53:17'),
(9, 572, '2025-08-15 09:53:18'),
(10, 460, '2025-08-15 09:53:19'),
(11, 68, '2025-08-15 09:53:45'),
(12, 451, '2025-08-15 09:53:46'),
(13, 163, '2025-08-15 09:53:47'),
(14, 699, '2025-08-15 09:53:48'),
(15, 13, '2025-08-15 09:53:49'),
(16, 715, '2025-08-15 09:53:50'),
(17, 646, '2025-08-15 09:53:51'),
(18, 532, '2025-08-15 09:53:52'),
(19, 916, '2025-08-15 09:53:53'),
(20, 527, '2025-08-15 09:53:54'),
(21, 631, '2025-08-15 09:54:18'),
(22, 377, '2025-08-15 09:54:19'),
(23, 284, '2025-08-15 09:54:20'),
(24, 463, '2025-08-15 09:54:21'),
(25, 54, '2025-08-15 09:54:22'),
(26, 993, '2025-08-15 09:54:23'),
(27, 464, '2025-08-15 09:54:24'),
(28, 559, '2025-08-15 09:54:25'),
(29, 854, '2025-08-15 09:54:26'),
(30, 664, '2025-08-15 09:54:27');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ldr_data`
--
ALTER TABLE `ldr_data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `ldr_data`
--
ALTER TABLE `ldr_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
