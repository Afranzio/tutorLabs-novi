-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: vorkinsta
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `skill`
--

DROP TABLE IF EXISTS `skill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skill` (
  `id` int NOT NULL AUTO_INCREMENT,
  `skill_name` varchar(45) DEFAULT NULL,
  `skill_description` varchar(45) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `skills` json NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_skill_user_id_idx` (`user_id`),
  CONSTRAINT `fk_skill_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=INNODB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=UTF8_GENERAL_CI;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skill`
--

LOCK TABLES `skill` WRITE;
/*!40000 ALTER TABLE `skill` DISABLE KEYS */;
INSERT INTO `skill` VALUES (1,NULL,'Front end and backend',11,'{\"skills\": [\"Angular\", \"Nodejs\", \"CSS\", \"Javasript\", \"typescript\", \"ionic\"], \"userId\": 11}'),(2,NULL,NULL,11,'{\"skills\": [\"Angular\", \"Nodejs\", \"CSS\", \"Javasript\", \"typescript\", \"ionic\"], \"userId\": 11}'),(3,NULL,'frontend. backend developer',11,'{\"skills\": [\"Angular\", \"Nodejs\", \"CSS\", \"Javasript\", \"typescript\", \"ionic\"], \"userId\": 11}'),(4,NULL,NULL,12,'{\"skills\": [\"React\", \"Nodejs\", \"CSS\", \"Javasript\", \"typescript\"], \"userId\": 11}'),(5,NULL,NULL,13,'{\"skills\": [\"Devops\", \"Networking\"], \"userId\": 11}'),(6,NULL,NULL,14,'{\"skills\": [\"Java\", \"Javascript\", \"C++\"], \"userId\": 11}');
/*!40000 ALTER TABLE `skill` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-28 21:25:31
