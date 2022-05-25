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
  `name` varchar(45) NOT NULL,
  `category` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `costumers`
--

LOCK TABLES `costumers` WRITE;
/*!40000 ALTER TABLE `costumers` DISABLE KEYS */;
INSERT INTO `costumers` VALUES (1,'Leroy Merlin','Appliances'),(2,'Polito','Education');
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
  `costumer_id` int NOT NULL,
  `rfid` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `rfid_UNIQUE` (`rfid`),
  KEY `fkey_cst_idx` (`costumer_id`),
  CONSTRAINT `fkey_cst` FOREIGN KEY (`costumer_id`) REFERENCES `costumers` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
INSERT INTO `items` VALUES (1,'The girl with the dragon tattoo',NULL,'Book',2,NULL),(2,'Advanced Physics',NULL,'Book',2,NULL),(3,'Screewdriver',NULL,'Tools',1,'30'),(6,'Hammer',NULL,'Tools',1,'50'),(7,'Yellow Highlighter',NULL,'Stationary',2,NULL);
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
  `pin` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `cost_id_idx` (`cst_id`),
  KEY `fkey_cst_id_idx` (`cst_id`),
  CONSTRAINT `fkey_cst_id` FOREIGN KEY (`cst_id`) REFERENCES `costumers` (`id`) ON DELETE CASCADE
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
  `name` varchar(45) NOT NULL,
  `mail_adr` varchar(45) NOT NULL,
  `hashed_pw` varchar(90) NOT NULL,
  `salt` varchar(45) DEFAULT NULL,
  `rfid` varchar(45) DEFAULT NULL,
  `pin` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id_UNIQUE` (`id`),
  UNIQUE KEY `mail_adr_UNIQUE` (`mail_adr`),
  UNIQUE KEY `rfid_UNIQUE` (`rfid`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'John Doe','johndoe@gmail.com','$2b$12$f2bTa9nefBDJhFU2CNckNeaFqL0QrHCDxCsv0.ZP8u5c0VK3uAlIe','$2b$12$f2bTa9nefBDJhFU2CNckNe','23543',1235),(2,'Catarina Sousa','catarinasousa@gmail.com','$2b$12$Vvd27X3G5OXbvhF7MqSPbOk1Iz2MlaoZLkXX16MjhvtdxkABF6tF.','$2b$12$Vvd27X3G5OXbvhF7MqSPbO',NULL,NULL),(3,'Sofia Fiorentino','sofiafiorentino@gmail.com','$2b$12$sf4/ReWU2wyljMUOfAZRO.tvji94wlqXzO0A.xYfC.Ewn8vfcP8G6','$2b$12$sf4/ReWU2wyljMUOfAZRO.','4',0),(4,'Marcus Fiorentino','marcusfiorentino@gmail.com','$2b$12$UnKvWam1PeAJ6lK3LlJSV.pGqsMjEF.B3v.Eor3WSYM9BYTP0QH8K','$2b$12$UnKvWam1PeAJ6lK3LlJSV.',NULL,NULL),(6,'John Doe','john@test.com','$2b$12$36OVbAdI2Jy3PZ.LEeLGeON4S/AyO1DrDcwllKM1hEJF77i2OMQOe','$2b$12$36OVbAdI2Jy3PZ.LEeLGeO','37432',1234),(7,'CONTROLLER TEST USER','17c4a55e79af4490827f6685a58e069d@example.com','$2b$12$7cgmzYW8shP5s.CkylXVoeMiJwbTfKQR9bK6LsxWSTsvIX9oFd3Hi','$2b$12$7cgmzYW8shP5s.CkylXVoe',NULL,NULL),(8,'CONTROLLER TEST USER','b6eeb5807a1544159ed81dafc338e7d0@example.com','$2b$12$OqIhGuqFJETeO/7kymRsVed9r9PlOT5WqiMV1z6xj7gFBIS9nB5nO','$2b$12$OqIhGuqFJETeO/7kymRsVe',NULL,NULL),(9,'CONTROLLER TEST USER','ded2e02d4ee145b38e69fec01ad57fef@example.com','$2b$12$VmP.GI2/yi2RS.7vGteSmeFh2pi/d5r7kktxlXQtSdFqpFcY5ecSa','$2b$12$VmP.GI2/yi2RS.7vGteSme',NULL,NULL),(10,'CONTROLLER TEST USER','75d264fabcb24c6ba99aab76e3114483@example.com','$2b$12$GeCEzDfzOziKpGixFKFFHOp3LqzjKtYOgZCYFHfS60jJPgg/stzUy','$2b$12$GeCEzDfzOziKpGixFKFFHO',NULL,NULL),(11,'CONTROLLER TEST USER','d40330ec95a74350857908474ef48cf8@example.com','$2b$12$AZsK93UKwt9m0/GzZT0DB.5uzwSCISDpa5PQxPJuoYm3DtgwaV88G','$2b$12$AZsK93UKwt9m0/GzZT0DB.',NULL,NULL),(12,'CONTROLLER TEST USER','6ec1143c28d04066ac616bf2eb4720dc@example.com','$2b$12$F1zDTMcc2PwZMdEjgxPy9OSb5iEvNza4iyjIrYg2P6cZ1r54IsHYG','$2b$12$F1zDTMcc2PwZMdEjgxPy9O',NULL,NULL),(13,'CONTROLLER TEST USER','7773c67e7c8043b1983cdc6e41ea5e7b@example.com','$2b$12$mW.W9KbSMJ08QRgRQBDy1eZYK4V74D2l7h0A0pzf0jSMkfHGmeaky','$2b$12$mW.W9KbSMJ08QRgRQBDy1e',NULL,NULL),(14,'CONTROLLER TEST USER','de4871232e564d7da95832996e369b04@example.com','$2b$12$4y3yHfDgIi/L6xgKhecdFutbxSNxCzZyvJdSeLx8K5eTwnYyLHzn2','$2b$12$4y3yHfDgIi/L6xgKhecdFu',NULL,NULL),(15,'CONTROLLER TEST USER','d02b350f0bd644698239555ee7c08cae@example.com','$2b$12$ZyZx4E0xNUKvYt2xPqFQbe4WWfzBuSodIYpozBn7.AeGCiX19kDoa','$2b$12$ZyZx4E0xNUKvYt2xPqFQbe',NULL,NULL),(16,'CONTROLLER TEST USER','da0adddb59df452882bf6a6af3c12648@example.com','$2b$12$sFKnuujHtE2LaWu6K2jkIeZfIHC79SOcYW4Qn.SbHYF3BIZECia6C','$2b$12$sFKnuujHtE2LaWu6K2jkIe',NULL,NULL),(17,'CONTROLLER TEST USER','ab77650ff15f4ae38cda95e2ce523af7@example.com','$2b$12$go30S7bkeAkHyjSHPWy8xOknG72fSBhiffA6cQAyrUxhaRCpVyCZm','$2b$12$go30S7bkeAkHyjSHPWy8xO',NULL,NULL),(18,'CONTROLLER TEST USER','50693da69f3342e085360a51d6852ec1@example.com','$2b$12$fqd2VHwgxuTiP1rQaR/FYOPY/r6QeATfhCZ2r26KAqsTSizv.oBPO','$2b$12$fqd2VHwgxuTiP1rQaR/FYO',NULL,NULL),(19,'CONTROLLER TEST USER','a25dc48a261548b79ebb3168b1e8fb7a@example.com','$2b$12$1U0qSk5wo64ltMzTgZF1l.XasEZqX4dSABhd19lonNdbeJHsrsS8.','$2b$12$1U0qSk5wo64ltMzTgZF1l.',NULL,NULL),(20,'CONTROLLER TEST USER','f5e2a0589c4e43d59a7569913114fddf@example.com','$2b$12$p1uj8w5j7NXdffx0JuHujOX8IiwCfrJ4rcCgDzkeyfnXpaXC22q5G','$2b$12$p1uj8w5j7NXdffx0JuHujO',NULL,NULL),(21,'CONTROLLER TEST USER','2f86973d12204fd5909dcab0917278c1@example.com','$2b$12$0gOv9c8OwOXvW4PBgOatteMea0eZd5M1qY7WGfmvqSoTjvTyOux2m','$2b$12$0gOv9c8OwOXvW4PBgOatte','1234',5678),(22,'Lino','lino@gmail.com','$2b$12$qxWsWYcmInkI.78lFhOn/.4ZuNllyJjJrXXp0yNWZZMgbNuOUdayO','$2b$12$qxWsWYcmInkI.78lFhOn/.',NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users2costumers`
--

DROP TABLE IF EXISTS `users2costumers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users2costumers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `cst_id` int NOT NULL,
  `role` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `user_fkey_idx` (`user_id`),
  KEY `cost_id_idx` (`cst_id`),
  CONSTRAINT `cost_id` FOREIGN KEY (`cst_id`) REFERENCES `costumers` (`id`) ON DELETE CASCADE,
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users2costumers`
--

LOCK TABLES `users2costumers` WRITE;
/*!40000 ALTER TABLE `users2costumers` DISABLE KEYS */;
/*!40000 ALTER TABLE `users2costumers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-25 17:10:24
