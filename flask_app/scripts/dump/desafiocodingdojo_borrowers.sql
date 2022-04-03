-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: desafiocodingdojo
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
-- Table structure for table `borrowers`
--

DROP TABLE IF EXISTS `borrowers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `borrowers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(150) DEFAULT NULL,
  `last_name` varchar(150) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `password` varchar(250) DEFAULT NULL,
  `money_for` varchar(250) DEFAULT NULL,
  `description` text,
  `amount_needed` int DEFAULT NULL,
  `amount_raised` int DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `borrowers`
--

LOCK TABLES `borrowers` WRITE;
/*!40000 ALTER TABLE `borrowers` DISABLE KEYS */;
INSERT INTO `borrowers` VALUES (3,'Charles','Leclerc','Charles.Leclerc@ferrari.com','$2b$12$.4dRc7h2jo51ahCtK5rIUutgHcuhai6E/aoDysWAFr9/CGbd46CCe','Buying a new MGU-K','Blown Motor after Jeddah',20000,18200,'2022-04-03 17:32:15','2022-04-03 18:04:50'),(4,'Carlos','Sainz','smooth_operator@ferrario.it','$2b$12$FHQn5gMAUpFzmyrmjimG7uBKGwFsiPdtr8w.tQmkRV1GjUIBcxHe2','New rear wing','Need more downforce for Australia',5000,5000,'2022-04-03 17:33:13','2022-04-03 18:05:04'),(5,'Nicolas ','Latifi','Nicky@williams.en','$2b$12$rAdaK77k0jNFLd42W8DjmuGHsOVhjob2maydADt/TJgAWYql31/YS','Buy a new chassis','I destroyed it on the last race',15000,14050,'2022-04-03 17:55:22','2022-04-03 18:05:13'),(6,'Nikita','Mazepin','nikita@noteam.ru','$2b$12$ncgDrK0LzTJSoIzmb3.bN.2Cg4HBXPbI0opYEG0NAua8UMhq9daPK','Create a new f1 team','I need a new team to keep racing',20000,17000,'2022-04-03 18:06:56','2022-04-03 18:08:22');
/*!40000 ALTER TABLE `borrowers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-03 18:16:53
