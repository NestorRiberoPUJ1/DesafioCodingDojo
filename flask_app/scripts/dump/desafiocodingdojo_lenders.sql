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
-- Table structure for table `lenders`
--

DROP TABLE IF EXISTS `lenders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lenders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(150) DEFAULT NULL,
  `last_name` varchar(150) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `password` varchar(250) DEFAULT NULL,
  `money` int DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lenders`
--

LOCK TABLES `lenders` WRITE;
/*!40000 ALTER TABLE `lenders` DISABLE KEYS */;
INSERT INTO `lenders` VALUES (3,'Nestor','Ribero','nestor_05ribero@hotmail.com','$2b$12$yNzIfGxWKT5nAxReBFy6TuKJA32/3wOFOIFyqPP/73oclzEP1ONaK',0,'2022-04-03 17:31:07','2022-04-03 17:39:07'),(4,'Max','Ve','max@rb.au','$2b$12$8JPnviYwSfrv9OBh2Mmk.eL75PRwRl.TT3VBMHbeaGILzscylZWCq',10000,'2022-04-03 17:43:01','2022-04-03 17:43:16'),(5,'Mattia','Binotto','Mattia@ferrari.it','$2b$12$qM6WIwOZ3VUbQxmtjKx5K.cwUimUxb7DNzEn8MjYOWmeY5X6yjQs6',26750,'2022-04-03 17:52:33','2022-04-03 18:08:21'),(6,'Christian','Horner','horner@rb.au','$2b$12$vNaPuH83n/gIPJ6lAIBdIuPnKire9IEKXPyKjY4L6Cp0IHGisEDOW',19000,'2022-04-03 18:04:15','2022-04-03 18:07:51');
/*!40000 ALTER TABLE `lenders` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-03 18:16:52
