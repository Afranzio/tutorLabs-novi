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
-- Table structure for table `profile`
--

DROP TABLE IF EXISTS `profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profile` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `country_id` int DEFAULT NULL,
  `state_id` int DEFAULT NULL,
  `mobile_number` varchar(10) DEFAULT NULL,
  `skype_id` varchar(45) DEFAULT NULL,
  `skill_id` int DEFAULT NULL,
  `experience` varchar(45) DEFAULT NULL,
  `current_position` varchar(45) DEFAULT NULL,
  `portfolio_link` varchar(100) DEFAULT NULL,
  `hours_per_week` varchar(45) DEFAULT NULL,
  `resume_url` varchar(100) DEFAULT NULL,
  `bio` varchar(1000) DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_profile_user_id_idx` (`user_id`),
  KEY `fk_profile_user_id2_idx` (`user_id`),
  CONSTRAINT `fk_profile_userId` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=INNODB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=UTF8_GENERAL_CI;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profile`
--

LOCK TABLES `profile` WRITE;
/*!40000 ALTER TABLE `profile` DISABLE KEYS */;
INSERT INTO `profile` VALUES (1,'Mayur','G',2,5,'9767099437','mayur2727',3,' 3 Years','Software developer','https://www.testurl.com/testlink.pdf','20 hours','https://www.testurl.com/testlink.pdf','Working as a software developer',11),(2,'Mohit','Kumar',2,5,'9767099437','mayur2727',4,' 3 Years','Software developer','https://www.testurl.com/testlink.pdf','20 hours','https://www.testurl.com/testlink.pdf','Working as a software developer',12),(3,'Rajiv','Kumar',2,5,'9767099437','mayur2727',5,' 3 Years','Software developer','https://www.testurl.com/testlink.pdf','20 hours','https://www.testurl.com/testlink.pdf','Working as a software developer',13),(4,'Kunal','Jadhav',2,5,'9767099437','mayur2727',6,' 3 Years','Software developer','https://www.testurl.com/testlink.pdf','20 hours','https://www.testurl.com/testlink.pdf','Working as a software developer',14);
/*!40000 ALTER TABLE `profile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-28 21:25:29
