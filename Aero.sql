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
-- Table structure for table `ansys`
--

DROP TABLE IF EXISTS `ansys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ansys` (
  `nome` varchar(200) DEFAULT NULL,
  `dia` date DEFAULT NULL,
  `link` varchar(200) DEFAULT NULL,
  `downforce` decimal(10,4) DEFAULT NULL,
  `drag` decimal(10,4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ansys`
--

LOCK TABLES `ansys` WRITE;
/*!40000 ALTER TABLE `ansys` DISABLE KEYS */;
INSERT INTO `ansys` VALUES ('Report-New.Ga2-Version-0953.txt','2023-02-13','',-33.1398,14.0342),('Report-New.s1223rtl-Version-1189.txt','2023-02-13','',-98.4376,17.9100),('Report-New.s1223rtl-Version-0493.txt','2023-02-14','',-106.4619,17.3246),('Report-New.Ga2-Version-0953.txt','2023-02-15','',-33.1398,14.0342),('Report-New.s1223rtl-Version-0493.txt','2023-02-15','',-106.4619,17.3246),('Report-New.s1223rtl-Version-1189.txt','2023-02-15','',-98.4376,17.9100);
/*!40000 ALTER TABLE `ansys` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `simulacoes`
--

DROP TABLE IF EXISTS `simulacoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `simulacoes` (
  `nome` varchar(1000) DEFAULT NULL,
  `link` varchar(10000) DEFAULT NULL,
  `dia` date DEFAULT NULL,
  `cl` decimal(3,2) DEFAULT NULL,
  `cd` decimal(3,2) DEFAULT NULL,
  `config` enum('completo','asaTraseira','asaDianteira','radiador') DEFAULT NULL,
  `velocidade` tinyint DEFAULT '60',
  `Area` decimal(10,5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `simulacoes`
--

LOCK TABLES `simulacoes` WRITE;
/*!40000 ALTER TABLE `simulacoes` DISABLE KEYS */;
INSERT INTO `simulacoes` VALUES ('Simulacao_e2020_completo_1 (não esta rodada)','https://drive.google.com/file/d/1MPg3Ai5gu6GxgsPuxZeShwBhs23rMwKO/view?usp=sharing','2020-09-21',0.00,0.00,'completo',0,NULL),('Asa_dentro_regra','https://drive.google.com/file/d/1qHN9TksdGVqGM1mCth5sIHOcBDFmp0tf/view?usp=sharing','2020-12-14',0.36,0.22,'completo',60,1.00000),('Asa_fora_regra','https://drive.google.com/file/d/1R-4jGNinfOYSZLf3UIXeeHid1Y1HovaI/view?usp=sharing','2020-12-14',0.36,0.22,'completo',60,1.00000),('CoP_E2021','https://drive.google.com/file/d/1l0Ug0CG3LH2jb3WOV43y5rFevKTDwmE5/view?usp=sharing','2020-11-25',2.12,1.19,'completo',36,0.52491),('Gurney_flap_big','https://drive.google.com/file/d/1hprc4OJH1U_PkP_KFut-pVvnywBGij0r/view?usp=sharing','2020-09-03',0.02,0.01,'asaDianteira',60,0.08441),('gurney_flap_2mm_60kph','https://drive.google.com/file/d/1SALt_E6_jCcghwtNgjWsGAFrVKJmaVLL/view?usp=sharing','2020-09-09',8.04,1.71,'asaDianteira',60,0.08441),('R75 teste posição asas','https://drive.google.com/file/d/1quWKK8R0ZFRFef8NDDyduST7KjgonzN5/view?usp=sharing','2020-08-18',1.40,1.22,'completo',60,0.53050),('inicial teste posição asas','https://drive.google.com/file/d/1XhuES95h1BYRF_HTL_f9iwgrOrVkL28N/view?usp=share_link','2020-08-26',1.57,1.13,'completo',60,0.53050),('R45_45 teste posição asas','https://drive.google.com/file/d/1opPkNBEtqz1eOjjk0fq8bjJrnbJ9WG2N/view?usp=share_link','2020-08-18',1.41,1.23,'completo',60,0.53050),('R35 teste posição asas','https://drive.google.com/file/d/1IOtevgL8M8wb07xiffRWwlzA5ReKrZtD/view?usp=share_link','2020-08-20',1.43,1.22,'completo',60,0.53050),('Sim1 teste posição asas','https://drive.google.com/file/d/1tPOIIyUE8Tp8b8ztVONg-L8gQOGfML1w/view?usp=share_link','2020-08-21',1.82,1.32,'completo',60,0.53050),('Sim2 teste posição asas','https://drive.google.com/file/d/1uQ2wo8ZuTcLlPhG8F7ScHMiz0NJKONwK/view?usp=share_link','2020-08-21',1.88,1.45,'completo',60,0.53050),('Rear Wing teste ângulo das asas (diversos resultados no link)','https://drive.google.com/drive/folders/1JimRVV-vNxLd28vpfMVLvLxer7HA1Rd-?usp=share_link','2020-07-27',0.00,0.00,'asaTraseira',60,0.53050),('Front Wing teste ângulo das asas (diversos resultados no link)','https://drive.google.com/drive/folders/1oujvzOj-bsU-YJwJGOaCqZp_F0TjFYbl?usp=share_link','2020-07-27',0.00,0.00,'asaTraseira',60,0.53050),('Front Wing Projeto Endplate (diversos resultados no link)','https://drive.google.com/drive/folders/1tG9RsNImNN1Z9Nksws8czh8ebgLawqdk?usp=share_link','2020-07-28',0.00,0.00,'asaDianteira',60,0.08441),('Rear Wing Projeto Endplate (diversos resultados no link)','https://drive.google.com/drive/folders/1ljwcexMQc_sYXSTwboKckNcmSRYAQOce?usp=share_link','2020-08-03',0.00,0.00,'asaTraseira',60,0.15742),('Simus 2D Ansys (diversas)','https://drive.google.com/drive/folders/1tIynBfpwhza0xJfyB0klqf4BohFPzock?usp=share_link','2020-07-19',0.00,0.00,'asaTraseira',0,0.00000),('sim_v1 Endplate rw','https://drive.google.com/file/d/1gv68XJD9sDaoXetfFpTw1umRD_6iOzNR/view?usp=share_link','2022-09-18',0.89,0.31,'asaTraseira',60,1.00000),('sim_base Endplate rw','https://drive.google.com/file/d/1P0NwEs-bzIEoiPS3jglAX04hWHoH-8LK/view?usp=share_link','2022-09-18',0.97,0.34,'asaTraseira',60,1.00000),('Front wing controle (não está rodada)','https://drive.google.com/file/d/1-Pysz9YmPwFIqysS8BZPjku4yUjQsFmt/view?usp=share_link','2021-09-21',0.00,0.00,'completo',0,0.00000),('front wing 5mm (melhorias asa dianteira)','https://drive.google.com/file/d/1I7G2FoTrfF-5QYFOl0KO93R0bZvDWMnB/view?usp=share_link','2021-09-27',0.37,0.42,'completo',60,0.52491),('e2021_base','https://drive.google.com/file/d/1M6fRukocr9I0l3MwFqmHYIZVD2LXknUw/view?usp=share_link','2021-09-29',1.98,1.21,'completo',60,0.52491),('front wing footplate','https://drive.google.com/file/d/1pJ_WBopqzo85dw-6Re1gIREb37J1YZcO/view?usp=share_link','2021-05-14',2.79,0.58,'asaDianteira',60,0.09078),('front wing footplate raised 20mm','https://drive.google.com/file/d/1dYkddj2XmZAWvs6s6LtsYkTUCu_W44K8/view?usp=share_link','2021-05-15',2.78,0.59,'asaDianteira',60,0.09294),('e2021_base_rear_tilt_2_flaps drs (não está rodada)','https://drive.google.com/file/d/1RXlS6va_pkYASqzpD2xmVHArBXfGncjC/view?usp=share_link','2021-08-23',0.00,0.00,'completo',60,0.52491),('e2021 up 10mm heave','https://drive.google.com/file/d/1JpZ6fTMA2w_Vqf3m6qxKSal4duH58XHx/view','2021-10-23',2.52,1.43,'completo',60,1.00000),('e2021 down 30mm heave','https://drive.google.com/file/d/1_VEE73L5uCviIdeQshEtx7HKutEL0Tdx/view','2021-10-23',2.35,1.33,'completo',60,1.00000),('e2021 down 20mm heave','https://drive.google.com/file/d/1xvk8py8-2JiZtDsi5o9sxC_ycH8ZCvNV/view','2021-10-23',2.37,1.62,'completo',60,1.00000),('e2021 up 0.25 graus pitch','https://drive.google.com/file/d/1EwiryRJFxsd1hAkBw5eFXYnebKjxfVg2/view','2021-11-09',2.35,1.35,'completo',60,1.00000),('e2021 up 0.5 graus pitch','https://drive.google.com/file/d/1rXbRWtRbWtZkp-20WVRKbtqGZGZ2ixqY/view','2021-11-09',2.27,1.40,'completo',60,1.00000),('e2021 up 0.75 graus pitch','https://drive.google.com/file/d/1pRlapi5_RhUmOF5Z5c8PfLK06AWZeOUR/view','2021-11-09',2.28,1.40,'completo',60,1.00000),('e2021 up 1 grau pitch','https://drive.google.com/file/d/1XhfV32PQIuZUYg8LFu9s6w9vYpM8EkaD/view','2021-11-11',2.09,1.38,'completo',60,1.00000),('e2021 roll 0.75 graus','https://drive.google.com/file/d/1Apy2rfr2wGkkfGtYd2BuVeTXSuIUm0qG/view','2021-11-28',1.98,1.24,'completo',60,1.00000),('e2021 roll 1 grau','https://drive.google.com/file/d/1PrRkHdwlO5WTGrclBuyF8w5wINSCnRtG/view','2021-11-28',2.01,1.25,'completo',60,1.00000),('footplate reta ','https://drive.google.com/file/d/1KUbrO3Y8pWaO3k_lRZughP_FPALEaR7W/view?usp=share_link','2021-11-03',0.70,0.29,'asaDianteira',60,0.17836),('footplate curva','https://drive.google.com/file/d/1KhuVx5sVBHyIg044p3B1f2n0tQeI1d7S/view?usp=share_link','2021-09-01',1.06,0.35,'asaDianteira',60,0.17870),('e2021 base rear tilt','https://drive.google.com/file/d/15HQUQiQZxOyW5AGcx_puyLx9S8yRrdta/view?usp=share_link','2021-08-21',1.67,0.95,'completo',60,0.52490),('DRS Leading Edge (não consigo abrir)','https://drive.google.com/file/d/147NNOxBjJILBCgIVqvgcs21IWwi92aal/view?usp=share_link','2021-08-20',0.00,0.00,'completo',60,0.52490),('CoP simu curva','https://drive.google.com/file/d/1Jk_xmG1r6eAV4xDGaDAZ4aglgGCQbWCo/view?usp=share_link','2021-10-04',0.00,0.00,'completo',36,0.52491),('CoP simu curva full','https://drive.google.com/file/d/1Ux5FiS9MHBoFxaSP4YskUYHOOOY8aXz8/view?usp=share_link','2021-11-11',0.00,0.00,'completo',36,0.52491),('asa dianteira efeito solo','https://drive.google.com/file/d/1eR4rSOLbf9TnZSSYV6qGPUp0Ycd3OQlV/view?usp=share_link','2021-05-21',0.00,0.00,'asaDianteira',60,0.07064),('roda girando','https://drive.google.com/file/d/1MOb_CaX4NuRrjDEFjpWeySUKL6mip8xU/view?usp=share_link','2021-05-24',0.96,0.50,'completo',60,1.00000),('roda parada','https://drive.google.com/file/d/1OFSEIh9gS2XpWqH0Y5dOPNC2n4j8R05p/view?usp=share_link','2021-05-24',0.93,0.52,'completo',60,1.00000),('difusor v2','https://drive.google.com/file/d/1z3e0vqTn9t0IoeLKouAoOVKGYUYtpT3P/view?usp=share_link','2021-04-29',1.68,1.15,'completo',36,0.52491),('difusor v3','https://drive.google.com/file/d/1doZ2FZXv5Wiyz8O9LyIH_wSgWBlGdwNC/view?usp=share_link','2021-05-10',2.14,1.20,'completo',36,0.52491),('bargeboards v1','https://drive.google.com/file/d/1kSUYtNSoFsjMrLhFDsymRMsqnY-vqkV_/view?usp=share_link','2021-04-23',1.36,0.79,'completo',36,0.52491),('e2021 raised 35mm with footplate VG inlet','https://drive.google.com/file/d/1khgXut2Z75UEupfvxYxULXkMVxesSGy2/view?usp=share_link','2021-05-17',2.08,1.21,'completo',36,0.52491);
/*!40000 ALTER TABLE `simulacoes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testes`
--

DROP TABLE IF EXISTS `testes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `testes` (
  `nome` varchar(200) DEFAULT NULL,
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
INSERT INTO `testes` VALUES (NULL,NULL,NULL,NULL,NULL,60,0,NULL,NULL);
/*!40000 ALTER TABLE `testes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-15 11:08:55
