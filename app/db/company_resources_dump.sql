CREATE DATABASE  IF NOT EXISTS `company_resources` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `company_resources`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: company_resources
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `assigned_equipment`
--

DROP TABLE IF EXISTS `assigned_equipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `assigned_equipment` (
  `assigned_equipment_id` int NOT NULL AUTO_INCREMENT,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `id_employee` int NOT NULL,
  `equipment_id` int NOT NULL,
  PRIMARY KEY (`assigned_equipment_id`),
  KEY `id_employee` (`id_employee`),
  KEY `equipment_id` (`equipment_id`),
  CONSTRAINT `assigned_equipment_ibfk_1` FOREIGN KEY (`id_employee`) REFERENCES `employees` (`id_employee`),
  CONSTRAINT `assigned_equipment_ibfk_2` FOREIGN KEY (`equipment_id`) REFERENCES `equipment` (`equipment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assigned_equipment`
--

LOCK TABLES `assigned_equipment` WRITE;
/*!40000 ALTER TABLE `assigned_equipment` DISABLE KEYS */;
INSERT INTO `assigned_equipment` VALUES (2,'2020-08-13','2020-09-13',2,2),(4,'2020-08-13','2020-09-13',1,4),(5,'2020-08-13','2020-09-13',2,5),(6,'2020-08-13','2020-09-13',3,6),(7,'2020-08-13','2020-09-13',1,7),(8,'2020-08-13',NULL,2,8),(9,'2020-08-13',NULL,1,1),(10,'2020-08-13',NULL,3,3);
/*!40000 ALTER TABLE `assigned_equipment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client_contracts`
--

DROP TABLE IF EXISTS `client_contracts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `client_contracts` (
  `client_contract_id` int NOT NULL AUTO_INCREMENT,
  `contract_code` varchar(100) NOT NULL,
  `start_date` date NOT NULL,
  `contract_description` varchar(500) DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `client_id` int NOT NULL,
  PRIMARY KEY (`client_contract_id`),
  UNIQUE KEY `contract_code` (`contract_code`),
  UNIQUE KEY `end_date` (`end_date`),
  KEY `client_id` (`client_id`),
  CONSTRAINT `client_contracts_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `clients` (`client_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client_contracts`
--

LOCK TABLES `client_contracts` WRITE;
/*!40000 ALTER TABLE `client_contracts` DISABLE KEYS */;
INSERT INTO `client_contracts` VALUES (1,'ABC123','2020-01-01','Structural Engineering Services','2022-02-01',1),(2,'XYZ456','2020-03-02','Building Materials Supply Services',NULL,2),(3,'QWE789','2020-05-03','Customer Support Services','2022-07-03',3),(4,'LKJ321','2020-08-04','Masonry Services','2022-10-04',4),(5,'FGH567','2020-01-10','Landscaping Services','2022-12-08',2),(6,'KLM234','2020-03-09','Excavation and Grading Services',NULL,3);
/*!40000 ALTER TABLE `client_contracts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clients`
--

DROP TABLE IF EXISTS `clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clients` (
  `client_id` int NOT NULL AUTO_INCREMENT,
  `client_name` varchar(100) NOT NULL,
  `contact` varchar(50) NOT NULL,
  PRIMARY KEY (`client_id`),
  UNIQUE KEY `client_name` (`client_name`),
  UNIQUE KEY `contact` (`contact`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clients`
--

LOCK TABLES `clients` WRITE;
/*!40000 ALTER TABLE `clients` DISABLE KEYS */;
INSERT INTO `clients` VALUES (1,'ABC Construction','jsmith@abcconstruction.com'),(2,'XYZ Builders','lwilson@bestbuilders.com'),(3,'Structures Unlimited','slee@structuresunlimited.com'),(4,'High Quality Contractors ','smiller@highqualitycontractors.com');
/*!40000 ALTER TABLE `clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cost_centers`
--

DROP TABLE IF EXISTS `cost_centers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cost_centers` (
  `cost_center_id` int NOT NULL AUTO_INCREMENT,
  `center_name` varchar(100) NOT NULL,
  `center_code` varchar(50) NOT NULL,
  PRIMARY KEY (`cost_center_id`),
  UNIQUE KEY `center_name` (`center_name`),
  UNIQUE KEY `center_code` (`center_code`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cost_centers`
--

LOCK TABLES `cost_centers` WRITE;
/*!40000 ALTER TABLE `cost_centers` DISABLE KEYS */;
INSERT INTO `cost_centers` VALUES (1,'Aerodrom Nikola Tesla','ANT'),(2,'Prokop','P'),(3,'Inženjering put - Preljina','IP'),(4,'Road Design','RD');
/*!40000 ALTER TABLE `cost_centers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `id_employee` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `contact` varchar(50) NOT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `user_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_employee`),
  UNIQUE KEY `contact` (`contact`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'Maja','Dombi','0669511449',1,'cc3143b5-bfd7-4587-b713-ef0229d69b6d'),(2,'Mira','Dombi','0669612',1,NULL),(3,'Marko','Dombi','06695114478',1,NULL);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employment_contracts`
--

DROP TABLE IF EXISTS `employment_contracts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employment_contracts` (
  `id_row` int NOT NULL AUTO_INCREMENT,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `contract_type` varchar(50) NOT NULL,
  `paycheck` float NOT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `fk_employee_id` int NOT NULL,
  PRIMARY KEY (`id_row`),
  KEY `fk_employee_id` (`fk_employee_id`),
  CONSTRAINT `employment_contracts_ibfk_1` FOREIGN KEY (`fk_employee_id`) REFERENCES `employees` (`id_employee`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employment_contracts`
--

LOCK TABLES `employment_contracts` WRITE;
/*!40000 ALTER TABLE `employment_contracts` DISABLE KEYS */;
INSERT INTO `employment_contracts` VALUES (1,'2022-10-10',NULL,'neodredjeno',120000,1,1),(2,'2023-01-10','2023-03-10','odredjeno',100000,1,2),(3,'2022-10-10','2023-01-10','odredjeno',100000,0,3),(4,'2023-01-10','2023-04-10','odredjeno',150000,1,3);
/*!40000 ALTER TABLE `employment_contracts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipment`
--

DROP TABLE IF EXISTS `equipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipment` (
  `equipment_id` int NOT NULL AUTO_INCREMENT,
  `invoice_code` varchar(45) NOT NULL,
  `name` varchar(200) NOT NULL,
  `category` varchar(200) NOT NULL,
  `serial_number` varchar(200) NOT NULL,
  `net` float NOT NULL,
  `vat` float NOT NULL,
  `date_of_purchase` date NOT NULL,
  `date_of_transaction` date DEFAULT NULL,
  `shop_name` varchar(200) NOT NULL,
  PRIMARY KEY (`equipment_id`),
  UNIQUE KEY `serial_number` (`serial_number`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipment`
--

LOCK TABLES `equipment` WRITE;
/*!40000 ALTER TABLE `equipment` DISABLE KEYS */;
INSERT INTO `equipment` VALUES (1,'AAS-2345-6789','Laptop','Computer','AFG-12345-67890',1500,300,'2020-08-12','2020-08-13','Tech-Store'),(2,'BBS-4567-8901','Laptop Bag','Accessories','BGF-45678-90123',150,30,'2020-08-12','2020-08-13','Tech-Store'),(3,'CCS-6789-0123','Printer','Computer','CGH-67890-12345',500,100,'2020-08-12','2020-08-13','BC Group'),(4,'DDS-8901-2345','Printer Ink Cartridge','Accessories','DHI-89012-34567',60,12,'2020-08-12','2020-08-13','Tech-Store'),(5,'EES-0123-4567','External Hard Drive','Computer','EIJ-01234-56789',200,40,'2020-08-12','2020-08-13','Tech-Store'),(6,'FFS-2345-6789','Mouse','Accessories','FJK-23456-78901',30,6,'2020-08-12','2020-08-13','Tech-Store'),(7,'GGS-4567-8901','Keyboard','Accessories','GKL-45678-90123',40,8,'2020-08-12','2020-08-13','Tech-Store'),(8,'HHS-6789-0123','Monitor','Computer','HLM-67890-12345',400,80,'2020-08-12','2020-08-13','Tech-Store'),(9,'IIS-8901-2345','Headphones','Accessories','INP-89012-34567',35,7,'2020-08-12','2020-08-13','Tech-Store'),(10,'JJS-0123-4567','Laptop Stand','Accessories','JQR-01234-56789',20,4,'2020-08-12','2020-08-13','Tech-Store');
/*!40000 ALTER TABLE `equipment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `incoming_invoices`
--

DROP TABLE IF EXISTS `incoming_invoices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `incoming_invoices` (
  `incoming_invoice_id` int NOT NULL AUTO_INCREMENT,
  `reference_code_invoice` varchar(50) NOT NULL,
  `number_invoice` varchar(50) NOT NULL,
  `invoice_date` date NOT NULL,
  `net` float DEFAULT NULL,
  `vat` float DEFAULT NULL,
  `gross` float DEFAULT NULL,
  `description_invoice` varchar(500) DEFAULT NULL,
  `supplier_id` int NOT NULL,
  `cost_center_id` int DEFAULT NULL,
  PRIMARY KEY (`incoming_invoice_id`),
  KEY `supplier_id` (`supplier_id`),
  KEY `cost_center_id` (`cost_center_id`),
  CONSTRAINT `incoming_invoices_ibfk_1` FOREIGN KEY (`supplier_id`) REFERENCES `suppliers` (`supplier_id`),
  CONSTRAINT `incoming_invoices_ibfk_2` FOREIGN KEY (`cost_center_id`) REFERENCES `cost_centers` (`cost_center_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `incoming_invoices`
--

LOCK TABLES `incoming_invoices` WRITE;
/*!40000 ALTER TABLE `incoming_invoices` DISABLE KEYS */;
INSERT INTO `incoming_invoices` VALUES (1,'ABC123','INV123','2020-08-20',54.6,10.92,65.52,'Stationery supplies',4,1),(2,'XYZ456','INV456','2020-09-15',37.2,7.44,44.64,'Printing services',3,2),(3,'LKJ789','INV789','2020-10-20',128,25.6,153.6,'Software license',2,3),(4,'MNB901','INV901','2020-11-17',90,18,108,'IT maintenance services',1,4),(5,'QRS234','INV234','2020-12-01',56,11.2,67.2,'Office furniture',4,2),(6,'STU567','INV567','2020-12-30',78,15.6,93.6,'Cleaning services',3,1);
/*!40000 ALTER TABLE `incoming_invoices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `incoming_invoices_payments`
--

DROP TABLE IF EXISTS `incoming_invoices_payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `incoming_invoices_payments` (
  `incoming_invoice_payment_id` int NOT NULL AUTO_INCREMENT,
  `payment_date` date NOT NULL,
  `payment_description` varchar(500) DEFAULT NULL,
  `payment` float NOT NULL,
  `incoming_invoice_id` int NOT NULL,
  PRIMARY KEY (`incoming_invoice_payment_id`),
  KEY `incoming_invoice_id` (`incoming_invoice_id`),
  CONSTRAINT `incoming_invoices_payments_ibfk_1` FOREIGN KEY (`incoming_invoice_id`) REFERENCES `incoming_invoices` (`incoming_invoice_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `incoming_invoices_payments`
--

LOCK TABLES `incoming_invoices_payments` WRITE;
/*!40000 ALTER TABLE `incoming_invoices_payments` DISABLE KEYS */;
INSERT INTO `incoming_invoices_payments` VALUES (1,'2020-08-21','First payment',35,1),(2,'2020-08-25','Second payment',30.52,1),(3,'2020-09-17','Full payment',44.64,2),(4,'2020-10-21','First payment',75,3),(5,'2020-11-18','Full payment',108,4),(6,'2020-12-02','First payment',40,5),(7,'2020-12-15','Second payment',26.2,5),(8,'2020-12-31','Full payment',93.6,6);
/*!40000 ALTER TABLE `incoming_invoices_payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `outgoing_invoices`
--

DROP TABLE IF EXISTS `outgoing_invoices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `outgoing_invoices` (
  `outgoing_invoice_id` int NOT NULL AUTO_INCREMENT,
  `reference_code_invoice` varchar(50) NOT NULL,
  `start_date` date NOT NULL,
  `date_of_transaction` date NOT NULL,
  `net` float DEFAULT NULL,
  `vat` float DEFAULT NULL,
  `gross` float DEFAULT NULL,
  `description_invoice` varchar(500) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `certified_invoice` varchar(10) DEFAULT NULL,
  `client_id` int NOT NULL,
  `cost_center_id` int NOT NULL,
  PRIMARY KEY (`outgoing_invoice_id`),
  KEY `client_id` (`client_id`),
  KEY `cost_center_id` (`cost_center_id`),
  CONSTRAINT `outgoing_invoices_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `clients` (`client_id`),
  CONSTRAINT `outgoing_invoices_ibfk_2` FOREIGN KEY (`cost_center_id`) REFERENCES `cost_centers` (`cost_center_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `outgoing_invoices`
--

LOCK TABLES `outgoing_invoices` WRITE;
/*!40000 ALTER TABLE `outgoing_invoices` DISABLE KEYS */;
INSERT INTO `outgoing_invoices` VALUES (1,'XBLK-INV-1','2020-02-19','2020-03-19',4000,800,4800,'Construction of a new office building',1,'+',1,2),(2,'XBLK-INV-2','2020-02-19','2020-03-19',5000,1000,6000,'Construction of a new warehouse',1,'+',3,2),(3,'XBLK-INV-3','2020-02-19','2020-03-19',3000,600,3600,'Construction of a new carport',1,'+',1,3),(4,'XBLK-INV-4','2020-02-19','2020-03-19',2000,400,2400,'Construction of a new fence',1,'+',4,3),(5,'XBLK-INV-5','2020-02-19','2020-03-19',5000,1000,6000,'Construction of a new retaining wall',1,'+',2,4),(6,'XBLK-INV-6','2020-02-19','2020-03-19',3000,600,3600,'Construction of a new driveway',1,'+',4,1);
/*!40000 ALTER TABLE `outgoing_invoices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `outgoing_invoices_payments`
--

DROP TABLE IF EXISTS `outgoing_invoices_payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `outgoing_invoices_payments` (
  `outgoing_invoice_payment_id` int NOT NULL AUTO_INCREMENT,
  `payment_date` date NOT NULL,
  `payment_description` varchar(500) DEFAULT NULL,
  `payment` float NOT NULL,
  `outgoing_invoice_id` int NOT NULL,
  PRIMARY KEY (`outgoing_invoice_payment_id`),
  KEY `outgoing_invoice_id` (`outgoing_invoice_id`),
  CONSTRAINT `outgoing_invoices_payments_ibfk_1` FOREIGN KEY (`outgoing_invoice_id`) REFERENCES `outgoing_invoices` (`outgoing_invoice_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `outgoing_invoices_payments`
--

LOCK TABLES `outgoing_invoices_payments` WRITE;
/*!40000 ALTER TABLE `outgoing_invoices_payments` DISABLE KEYS */;
INSERT INTO `outgoing_invoices_payments` VALUES (1,'2020-04-19','First payment for invoice XBLK-INV-1',2000,1),(2,'2020-04-20','Second payment for invoice XBLK-INV-1',2800,1),(4,'2020-04-20','Second payment for invoice XBLK-INV-2',3000,2),(5,'2020-04-19','First payment for invoice XBLK-INV-3',1800,3),(6,'2020-04-20','Second payment for invoice XBLK-INV-3',1800,3),(7,'2020-04-19','First payment for invoice XBLK-INV-4',1200,4),(8,'2020-04-20','Second payment for invoice XBLK-INV-4',1200,4),(9,'2020-04-20','Second payment for invoice XBLK-INV-4',1200,4),(10,'2020-04-19','First payment for invoice XBLK-INV-5',3000,5),(11,'2020-04-19','First payment for invoice XBLK-INV-6',1800,6),(12,'2020-04-19','First payment for invoice XBLK-INV-5',3000,5);
/*!40000 ALTER TABLE `outgoing_invoices_payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suppliers`
--

DROP TABLE IF EXISTS `suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suppliers` (
  `supplier_id` int NOT NULL AUTO_INCREMENT,
  `supplier_name` varchar(100) NOT NULL,
  `contact` varchar(50) NOT NULL,
  PRIMARY KEY (`supplier_id`),
  UNIQUE KEY `supplier_name` (`supplier_name`),
  UNIQUE KEY `contact` (`contact`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliers`
--

LOCK TABLES `suppliers` WRITE;
/*!40000 ALTER TABLE `suppliers` DISABLE KEYS */;
INSERT INTO `suppliers` VALUES (1,'Ace Hardware ','(800) 848-4307'),(2,'Home Depot','(800) 466-3337'),(3,'Lowe\'s','(800) 445-6937'),(4,'Builders FirstSource','(800) 445-69037');
/*!40000 ALTER TABLE `suppliers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` varchar(50) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `is_admin` tinyint(1) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_name` (`user_name`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('cc3143b5-bfd7-4587-b713-ef0229d69b6d','admin','admin@mail.com','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',1,1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-22  2:45:51
