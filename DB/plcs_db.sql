-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: plcs_db
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
-- Table structure for table `costumers`
--

DROP TABLE IF EXISTS `costumers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `costumers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cst_id` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `category` varchar(45) NOT NULL,
  PRIMARY KEY (`cst_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `costumers`
--

LOCK TABLES `costumers` WRITE;
/*!40000 ALTER TABLE `costumers` DISABLE KEYS */;
/*!40000 ALTER TABLE `costumers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `items` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `description` varchar(45) DEFAULT NULL,
  `category` varchar(45) NOT NULL,
  `costumer` int NOT NULL,
  `rfid` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `costumer_idx` (`costumer`),
  CONSTRAINT `costumer` FOREIGN KEY (`costumer`) REFERENCES `costumers` (`cst_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `terminal_table`
--

DROP TABLE IF EXISTS `terminal_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `terminal_table` (
  `id` int NOT NULL AUTO_INCREMENT,
  `mac_adr` varchar(45) NOT NULL,
  `cst_id` int NOT NULL,
  `pin` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_cst_idx` (`cst_id`),
  CONSTRAINT `id_cst` FOREIGN KEY (`cst_id`) REFERENCES `costumers` (`cst_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `terminal_table`
--

LOCK TABLES `terminal_table` WRITE;
/*!40000 ALTER TABLE `terminal_table` DISABLE KEYS */;
/*!40000 ALTER TABLE `terminal_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `mail_adr` varchar(45) DEFAULT NULL,
  `hashed_pw` varchar(45) DEFAULT NULL,
  `salt` varchar(45) DEFAULT NULL,
  `rfid` int DEFAULT NULL,
  `pin` int DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `user_id_UNIQUE` (`user_id`),
  UNIQUE KEY `name_UNIQUE` (`name`),
  UNIQUE KEY `mail_adr_UNIQUE` (`mail_adr`),
  UNIQUE KEY `hashed_pw_UNIQUE` (`hashed_pw`),
  UNIQUE KEY `salt_UNIQUE` (`salt`),
  UNIQUE KEY `rfid_UNIQUE` (`rfid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users2costumers`
--

DROP TABLE IF EXISTS `users2costumers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users2costumers` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `cst_id` int NOT NULL,
  `role` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id_idx` (`user_id`),
  KEY `for_key_cst_idx` (`cst_id`),
  CONSTRAINT `for_key_cst` FOREIGN KEY (`cst_id`) REFERENCES `costumers` (`cst_id`),
  CONSTRAINT `for_key_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users2costumers`
--

LOCK TABLES `users2costumers` WRITE;
/*!40000 ALTER TABLE `users2costumers` DISABLE KEYS */;
/*!40000 ALTER TABLE `users2costumers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'plcs_db'
--

--
-- Dumping routines for database 'plcs_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-01 18:25:00
