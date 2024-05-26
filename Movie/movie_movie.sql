-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: movie
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `movie`
--

DROP TABLE IF EXISTS `movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie` (
  `movie_id` int NOT NULL,
  `title` varchar(50) DEFAULT NULL,
  `release_date` int DEFAULT NULL,
  `duration` int DEFAULT NULL,
  `director_id` int DEFAULT NULL,
  `genre_id` int DEFAULT NULL,
  PRIMARY KEY (`movie_id`),
  KEY `movie_ibfk_1` (`director_id`),
  KEY `movie_ibfk_2` (`genre_id`),
  CONSTRAINT `movie_ibfk_1` FOREIGN KEY (`director_id`) REFERENCES `director` (`director_id`),
  CONSTRAINT `movie_ibfk_2` FOREIGN KEY (`genre_id`) REFERENCES `genre` (`genre_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie`
--

LOCK TABLES `movie` WRITE;
/*!40000 ALTER TABLE `movie` DISABLE KEYS */;
INSERT INTO `movie` VALUES (700,'The Godfather',1972,175,100,2),(701,'Oppenheimer',2023,180,101,2),(702,'Interstellar',2014,169,101,3),(703,'Inception',2010,148,101,3),(704,'The Prestige',2006,130,101,9),(705,'The Dark Knight',2008,152,101,1),(706,'Ready Player One',2018,140,102,3),(707,'Saving Private Ryan',1998,169,102,2),(708,'Schindler\"s List',1993,195,102,2),(709,'Jurassic Park',1993,127,102,3),(710,'The Terminal',2004,128,102,5),(711,'The Lord of the Rings: The Fellowship of the Ring',2001,178,103,4),(712,'The Lord of the Rings: The Two Towers',2002,179,103,4),(713,'The Lord of the Rings: The Return of the King',2003,201,103,4),(714,'Pulp Fiction',1994,154,104,2),(715,'Reservoir Dogs',1992,99,104,9),(716,'Once Upon a Time in the America',1984,229,105,2),(717,'The Good, the Bad and the Ugly',1966,178,105,1),(718,'The Social Network',2010,120,106,2),(719,'The Curious Case of Benjamin Button',2008,166,106,2),(720,'Fight Club',1999,139,106,2),(721,'Se7en',1995,127,106,10),(722,'The Girl with the Dragon Tattoo',2011,158,106,10),(723,'Joker',2019,122,107,10),(724,'The Hangover',2009,100,107,5),(725,'Forrest Gump',1994,142,108,2),(726,'Back to the Future',1985,116,108,11),(728,'Life is Beautiful',1997,116,122,5),(730,'The Silence of the Lambs',1991,118,110,10),(731,'It\"s a Wonderful Life',1946,130,112,2),(732,'The Green Mile',1999,189,113,10),(733,'The Lion King',1994,88,114,8),(734,'The Pianist',2002,150,115,2),(735,'Avatar',2009,162,116,4),(736,'Avatar: The Way of Water',2022,192,116,4),(737,'Titanic',1997,194,116,7),(738,'The Terminator',1984,107,116,1),(739,'Terminator 2: Judgment Day',1991,137,116,1),(740,'Alien: Covenant',2017,122,117,6),(741,'The Martian',2015,144,117,11),(742,'American Gangster',2007,157,117,10),(743,'Hannibal',2001,131,117,10),(744,'Gladiator',2000,155,117,1),(745,'Avengers: Endgame',2019,181,118,1),(746,'Avengers: Infinity War',2018,149,118,1),(747,'Captain America: Civil War',2016,147,118,1),(748,'Captain America: The Winter Soldier',2014,136,118,1),(749,'Coco',2017,105,119,8),(750,'Finding Nemo',2003,100,119,8),(751,'Monsters, Inc.',2001,92,119,8),(752,'Toy Story 2',1999,92,119,8),(753,'Toy Story 3',2010,103,119,8),(754,'Braveheart',1995,178,120,2),(755,'Toy Story',1995,81,121,8),(756,'Cars',2006,117,121,8),(757,'Cars 2',2011,106,121,8);
/*!40000 ALTER TABLE `movie` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-25 15:00:51
