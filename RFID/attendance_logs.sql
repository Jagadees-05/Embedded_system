-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 15, 2025 at 01:56 PM
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
-- Database: `rfid`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance_logs`
--

CREATE TABLE `attendance_logs` (
  `name` varchar(100) DEFAULT NULL,
  `uid` varchar(20) DEFAULT NULL,
  `in_time` datetime DEFAULT NULL,
  `out_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `attendance_logs`
--

INSERT INTO `attendance_logs` (`name`, `uid`, `in_time`, `out_time`) VALUES
('shalini', '4122B11B', '2025-08-01 23:15:18', '2025-08-01 23:16:13'),
('jagadees', '6A18FA80', '2025-08-01 23:15:38', '2025-08-01 23:16:08'),
('Martin', '7382F5F6', '2025-08-01 23:15:23', '2025-08-01 23:15:58'),
('shalini', '4122B11B', '2025-08-01 23:16:23', '2025-08-01 23:17:08'),
('jagadees', '6A18FA80', '2025-08-01 23:16:28', '2025-08-01 23:16:58'),
('Martin', '7382F5F6', '2025-08-01 23:16:18', '2025-08-01 23:17:13'),
('shalini', '4122B11B', '2025-08-01 23:17:33', '2025-08-01 23:18:13'),
('jagadees', '6A18FA80', '2025-08-01 23:17:18', '2025-08-01 23:17:58'),
('Martin', '7382F5F6', '2025-08-01 23:17:23', '2025-08-01 23:18:08'),
('shalini', '4122B11B', '2025-08-01 23:21:07', '2025-08-01 23:21:40'),
('jagadees', '6A18FA80', '2025-08-01 23:21:25', '2025-08-01 23:21:50'),
('Martin', '7382F5F6', '2025-08-01 23:21:15', '2025-08-01 23:22:00');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
