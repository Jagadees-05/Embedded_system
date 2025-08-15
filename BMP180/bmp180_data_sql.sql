-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 15, 2025 at 06:44 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `practice`
--

-- --------------------------------------------------------

--
-- Table structure for table `bmp180_data`
--

CREATE TABLE `bmp180_data` (
  `id` int(11) NOT NULL,
  `temperature` float DEFAULT NULL,
  `pressure` float DEFAULT NULL,
  `altitude` float DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bmp180_data`
--

INSERT INTO `bmp180_data` (`id`, `temperature`, `pressure`, `altitude`, `timestamp`) VALUES
(1, 20, 973.62, 104, '2025-08-01 17:40:28'),
(2, 31.19, 1032.62, 165, '2025-08-01 17:40:31'),
(3, 26.87, 1024.9, 132, '2025-08-01 17:40:34'),
(4, 24.82, 1037.47, 237, '2025-08-01 17:40:38'),
(5, 22.14, 984.9, 109, '2025-08-01 17:40:39'),
(6, 28.58, 1027.93, 93, '2025-08-01 17:40:43'),
(7, 20.78, 988.14, 226, '2025-08-01 17:40:46'),
(8, 22.52, 1029.93, 153, '2025-08-01 17:40:48'),
(9, 31.68, 980.04, 141, '2025-08-01 17:40:52'),
(10, 32.75, 979.28, 198, '2025-08-01 17:40:54'),
(11, 32.64, 1029.14, 103, '2025-08-01 17:40:58'),
(12, 33.8, 1015.98, 89, '2025-08-01 17:41:01'),
(13, 32.65, 1025.83, 159, '2025-08-01 17:41:03'),
(14, 30.5, 968.99, 227, '2025-08-01 17:41:07'),
(15, 28.14, 1029.91, 204, '2025-08-01 17:41:10');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bmp180_data`
--
ALTER TABLE `bmp180_data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bmp180_data`
--
ALTER TABLE `bmp180_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
