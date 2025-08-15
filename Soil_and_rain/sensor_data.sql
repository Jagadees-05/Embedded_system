-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 15, 2025 at 12:58 PM
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
-- Database: `agriculture`
--

-- --------------------------------------------------------

--
-- Table structure for table `sensor_data`
--

CREATE TABLE `sensor_data` (
  `soil` int(11) DEFAULT NULL,
  `rain` int(11) DEFAULT NULL,
  `timestamp` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sensor_data`
--

INSERT INTO `sensor_data` (`soil`, `rain`, `timestamp`) VALUES
(0, 1, '2025-08-03 00:06:53'),
(0, 0, '2025-08-03 00:06:59'),
(1, 1, '2025-08-03 00:07:20'),
(0, 1, '2025-08-03 00:07:26'),
(0, 1, '2025-08-03 00:07:38'),
(0, 0, '2025-08-03 00:07:56'),
(1, 1, '2025-08-03 00:08:11'),
(1, 1, '2025-08-03 00:08:20'),
(1, 1, '2025-08-03 00:08:32'),
(1, 0, '2025-08-03 00:08:50'),
(0, 1, '2025-08-03 00:09:26'),
(0, 1, '2025-08-03 00:10:10'),
(0, 1, '2025-08-03 00:10:33'),
(0, 1, '2025-08-03 00:11:05'),
(0, 1, '2025-08-03 00:11:24'),
(1, 0, '2025-08-03 00:11:59'),
(0, 0, '2025-08-03 00:12:16'),
(1, 0, '2025-08-03 00:13:28'),
(0, 1, '2025-08-03 00:14:17'),
(0, 1, '2025-08-03 00:15:07'),
(1, 1, '2025-08-03 00:17:24'),
(1, 0, '2025-08-03 00:18:11'),
(0, 0, '2025-08-03 00:18:23'),
(1, 1, '2025-08-03 00:18:38'),
(0, 1, '2025-08-03 00:19:19'),
(1, 0, '2025-08-03 00:20:18'),
(0, 0, '2025-08-03 00:21:07'),
(0, 0, '2025-08-03 00:21:42'),
(1, 0, '2025-08-03 00:22:01'),
(0, 0, '2025-08-03 00:22:27'),
(0, 1, '2025-08-03 00:24:01'),
(0, 0, '2025-08-03 00:24:55'),
(1, 1, '2025-08-03 00:29:48'),
(1, 1, '2025-08-03 00:30:51'),
(0, 1, '2025-08-03 00:31:12'),
(1, 0, '2025-08-03 00:31:27'),
(1, 0, '2025-08-03 00:32:12'),
(0, 1, '2025-08-03 00:32:28'),
(1, 1, '2025-08-03 00:32:58'),
(1, 0, '2025-08-03 00:33:33'),
(1, 0, '2025-08-03 00:33:48'),
(1, 0, '2025-08-03 00:34:31');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
