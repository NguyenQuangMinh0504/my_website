-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: blog
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `blog`
--

DROP TABLE IF EXISTS `blog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blog` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `snippet` varchar(255) NOT NULL,
  `content` text NOT NULL,
  `total_view` int DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog`
--

LOCK TABLES `blog` WRITE;
/*!40000 ALTER TABLE `blog` DISABLE KEYS */;
INSERT INTO `blog` VALUES (1,'Good leader and good worker','Trích từ The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations.','<h1>\r\n    Good leader and good worker\r\n</h1>\r\n\r\n<br>\r\n<br>\r\n\r\n<h2>Worker</h2>\r\n\r\nWe explicitly state the problem we are seeking to solve, our hypothesis of how our proposed countermeasure will solve it, our methods for testing that hypothesis, our interpretation of the results, and our use of learnings to inform the next iteration.\r\n<br>\r\n<br>\r\n\r\n<h2>Leader</h2>\r\nThe leader helps coach the person conducting the experiment with questions that may include:\r\n<li>What was your last step and what happened?</li>\r\n<li>What did you learn?</li>\r\n<li>What is your condition now?</li>\r\n<li>What is your next target condition?</li>\r\n<li>What obstacle are you working on now?</li>\r\n<li>What is your next step?</li>\r\n<li>What is your expected outcome?</li>\r\n<li>When can we check?</li>',6),(2,'Useful stuffs','Useful website, software, command, link, ...','<h1>\r\n    Useful stuffs\r\n</h1>\r\n\r\n<br>\r\n<br>\r\n\r\n<h2>Useful Websites</h2>\r\nPagespeed Insight (<a href=\"https://pagespeed.web.dev/\">https://pagespeed.web.dev/</a>): Tool đánh giá chỉ ra vấn đề website đang gặp phải.\r\n<br>\r\nGoogle Search Console (<a href=\"https://search.google.com/\">https://search.google.com/</a>): Tool theo dõi performance và ranking website. Xem các url nào đã được đánh index.\r\n<br>\r\nCodebeautify highlighter (<a href=\"https://codebeautify.org/code-highlighter\">https://codebeautify.org/code-highlighter</a>): Online syntax highlighter\r\n<br>\r\n<br>\r\n<h2>Useful commands</h2>\r\n<h5>Script cài MySQL</h5>\r\n<pre><code id=\"script_mysql\" style=\"color:rgb(68, 68, 68); font-weight:400;background-color:rgb(240, 240, 240);background:rgb(240, 240, 240);display:block;padding: .5em;\">sudo wget https:<span style=\"color:rgb(136, 136, 136); font-weight:400;\">//repo.mysql.com/mysql-apt-config_0.8.26-1_all.deb</span>\r\nsudo dpkg -i mysql-apt-config_0<span style=\"color:rgb(136, 0, 0); font-weight:400;\">.8</span><span style=\"color:rgb(136, 0, 0); font-weight:400;\">.26</span><span style=\"color:rgb(136, 0, 0); font-weight:400;\">-1</span>_all.deb\r\nsudo apt-<span style=\"color:rgb(68, 68, 68); font-weight:700;\">get</span> update\r\nsudo apt-<span style=\"color:rgb(68, 68, 68); font-weight:700;\">get</span> install mysql-server -y\r\nsudo rm mysql-apt-config_0<span style=\"color:rgb(136, 0, 0); font-weight:400;\">.8</span><span style=\"color:rgb(136, 0, 0); font-weight:400;\">.26</span><span style=\"color:rgb(136, 0, 0); font-weight:400;\">-1</span>_all.deb</code></pre>\r\n<h5>Remove known key from IP SSH</h5>\r\n<pre><code id=\"remove_key_ssh\" style=\"color:rgb(68, 68, 68); font-weight:400;background-color:rgb(240, 240, 240);background:rgb(240, 240, 240);display:block;padding: .5em;\">ssh-keygen -R <span style=\"color:rgb(68, 68, 68); font-weight:400;\">&lt;<span style=\"color:rgb(68, 68, 68); font-weight:700;\">host</span>&gt;</span></code>\r\n</pre>\r\n<h2>Useful Link</h2>\r\n<a href=\"https://dev.mysql.com/doc/refman/8.1/en/\">https://dev.mysql.com/doc/refman/8.1/en/</a>: Trang docs MySQL (Search mãi mới ra, ảo thật đấy)\r\n<br>\r\n<br>\r\n<h2>Useful Software</h2>\r\nTerminus (<a href=\"https://termius.com/\">https://termius.com/</a>): SSH Terminal. Hỗ trợ nhiều OS\r\n<br>\r\n<br>\r\n<strong>Tính năng:</strong>\r\n<li>Nhóm server lại quản lý</li>\r\n<li>SSH theo user</li>\r\n<li>Split screen</li>\r\n<li>Drag item từ các server với nhau</li>\r\n<li>Thay key ssh nếu thấy host thay đổi</li>\r\n<br>\r\n<h2>Useful Keyboard Combination</h2>\r\n<h5>Vscode</h5>\r\n<style>\r\n    kbd {\r\n      border-radius: 2px;\r\n      padding: 2px;\r\n      border: 1px solid black;\r\n    }\r\n</style>        \r\n    <p><kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>~</kbd> : Tạo terminal mới</p>\r\n    <p><kbd>Option</kbd> <kbd><span>&#8593;</span></kbd> : Di chuyển code giữa các dòng</p>\r\n<br>\r\n<br>',4);
/*!40000 ALTER TABLE `blog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user` varchar(255) DEFAULT 'anonymous',
  `content` text NOT NULL,
  `blog_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_id` (`blog_id`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`blog_id`) REFERENCES `blog` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (1,'anonymous','hello',1);
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-15  4:34:04
