CREATE DATABASE  IF NOT EXISTS `aero` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `aero`;
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: aero
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `simulacoes`
--

DROP TABLE IF EXISTS `simulacoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `simulacoes` (
  `link` varchar(10000) DEFAULT NULL,
  `dia` date DEFAULT NULL,
  `cl` decimal(3,2) DEFAULT NULL,
  `cd` decimal(3,2) DEFAULT NULL,
  `config` enum('completo','asaTraseira','asaDianteira','radiador') DEFAULT NULL,
  `velocidade` tinyint DEFAULT '60',
  `angulo` tinyint DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `simulacoes`
--

LOCK TABLES `simulacoes` WRITE;
/*!40000 ALTER TABLE `simulacoes` DISABLE KEYS */;
/*!40000 ALTER TABLE `simulacoes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testes`
--

DROP TABLE IF EXISTS `testes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `testes` (
  `dia` date DEFAULT NULL,
  `cl` decimal(3,2) DEFAULT NULL,
  `cd` decimal(3,2) DEFAULT NULL,
  `config` enum('completo','asaTraseira','asaDianteira','radiador') DEFAULT NULL,
  `velocidade` tinyint DEFAULT '60',
  `angulo` tinyint DEFAULT '0',
  `tunel` int DEFAULT NULL,
  `fatorCorrecao` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testes`
--

LOCK TABLES `testes` WRITE;
/*!40000 ALTER TABLE `testes` DISABLE KEYS */;
/*!40000 ALTER TABLE `testes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'aero'
--

--
-- Dumping routines for database 'aero'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-09 20:16:45
