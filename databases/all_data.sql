-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: my_data
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
-- Current Database: `my_data`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `my_data` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `my_data`;

--
-- Table structure for table `daily_activities`
--

DROP TABLE IF EXISTS `daily_activities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `daily_activities` (
  `date` date NOT NULL,
  `study_time` float NOT NULL,
  `play_time` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `daily_activities`
--

LOCK TABLES `daily_activities` WRITE;
/*!40000 ALTER TABLE `daily_activities` DISABLE KEYS */;
INSERT INTO `daily_activities` VALUES ('2023-08-27',225,285);
/*!40000 ALTER TABLE `daily_activities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `running_data`
--

DROP TABLE IF EXISTS `running_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `running_data` (
  `day` date DEFAULT NULL,
  `duration` int DEFAULT NULL,
  `distance` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `running_data`
--

LOCK TABLES `running_data` WRITE;
/*!40000 ALTER TABLE `running_data` DISABLE KEYS */;
INSERT INTO `running_data` VALUES ('2023-04-10',30,2),('2023-04-11',30,3.02),('2023-04-12',30,4.02),('2023-04-13',30,3.55),('2023-04-14',30,3.03),('2023-04-15',45,4.76),('2023-04-16',30,3.02),('2023-04-17',30,2.77),('2023-04-18',30,2.67),('2023-04-19',30,3.17),('2023-04-20',30,3.45),('2023-04-21',30,3.42),('2023-04-22',45,4.54),('2023-04-23',45,5.3),('2023-04-24',30,2.86),('2023-04-25',30,3.68),('2023-04-26',30,3.76),('2023-04-27',30,3.84),('2023-04-28',30,3.83),('2023-04-29',45,5.62),('2023-04-30',45,4.45),('2023-05-01',30,3.85),('2023-05-02',45,5.51),('2023-05-03',45,5.52),('2023-05-04',45,4.43),('2023-05-05',45,4.74),('2023-05-06',45,5.05),('2023-05-07',45,5.42),('2023-05-08',30,2.7),('2023-05-09',45,6.12),('2023-05-10',30,3.88),('2023-05-11',30,2.53),('2023-05-12',60,6.1),('2023-05-13',30,3.84),('2023-05-14',30,2.33),('2023-05-15',30,3.06),('2023-05-16',38,5.05),('2023-05-17',45,5.85),('2023-05-18',30,3.72),('2023-05-19',45,5.18),('2023-05-20',60,7.23),('2023-05-21',45,4.83),('2023-05-22',45,5.3),('2023-05-23',45,5.89),('2023-05-24',45,5.4),('2023-05-25',45,5.51),('2023-05-26',45,5.01),('2023-05-27',60,6.42),('2023-05-28',60,6.75),('2023-05-29',45,5.38),('2023-05-30',45,5.9),('2023-05-31',45,5.8),('2023-06-01',45,5.73),('2023-06-02',45,5.4),('2023-06-03',60,5.45),('2023-06-04',60,6.68),('2023-06-05',45,4.11),('2023-06-06',30,3.39),('2023-06-07',30,3.42),('2023-06-08',30,3.68),('2023-06-09',60,5.02),('2023-06-10',30,2.07),('2023-06-11',30,2.25),('2023-06-12',30,2.62),('2023-06-13',30,2.49),('2023-06-14',30,3.71),('2023-06-15',30,3.77),('2023-06-16',30,3.86),('2023-06-17',30,3.28),('2023-06-18',30,2.47),('2023-06-19',30,1.94),('2023-06-20',30,3.07),('2023-06-21',45,4.75),('2023-06-23',30,3.64),('2023-06-26',15,1.58),('2023-06-28',30,3.03),('2023-06-29',15,1.47),('2023-07-01',37,3.92),('2023-07-03',150,9.67),('2023-07-04',46,5.04),('2023-07-10',43,3.91),('2023-07-20',45,3.72),('2023-07-21',46,4.06),('2023-07-22',45,5.16),('2023-08-03',73,5.35),('2023-08-04',65,5.5),('2023-08-06',45,4.35),('2023-08-09',72,6.32),('2023-08-11',61,5.57),('2023-08-12',76,4.91),('2023-08-14',62,5.23),('2023-08-15',60,5.33),('2023-08-16',75,6.85),('2023-08-17',90,7.04),('2023-08-10',0,0),('2023-08-08',0,0),('2023-08-07',0,0),('2023-08-05',0,0),('2023-08-02',0,0),('2023-08-01',0,0),('2023-07-31',0,0),('2023-07-30',0,0),('2023-07-29',0,0),('2023-07-28',0,0),('2023-07-27',0,0),('2023-07-26',0,0),('2023-07-25',0,0),('2023-07-24',0,0),('2023-07-23',0,0),('2023-07-19',0,0),('2023-07-18',0,0),('2023-07-17',0,0),('2023-07-16',0,0),('2023-07-15',0,0),('2023-07-14',0,0),('2023-07-13',0,0),('2023-07-12',0,0),('2023-07-11',0,0),('2023-07-09',0,0),('2023-07-08',0,0),('2023-07-07',0,0),('2023-07-06',0,0),('2023-07-05',0,0),('2023-07-02',0,0),('2023-06-30',0,0),('2023-06-27',0,0),('2023-06-25',0,0),('2023-06-24',0,0),('2023-06-22',0,0),('2023-08-18',60,5.07),('2023-08-19',0,0),('2023-08-20',75,6.35),('2023-08-21',75,5.36),('2023-08-22',60,5.07),('2023-08-23',60,4.92),('2023-08-24',30,2.68),('2023-08-25',30,2.41),('2023-08-26',0,0),('2023-08-27',0,0);
/*!40000 ALTER TABLE `running_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Current Database: `blog`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `blog` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `blog`;

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
  `date` date DEFAULT (curdate()),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog`
--

LOCK TABLES `blog` WRITE;
/*!40000 ALTER TABLE `blog` DISABLE KEYS */;
INSERT INTO `blog` VALUES (1,'DevOps useful stuffs','Trích từ The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations.','<h1>\r\n    DevOps useful stuffs\r\n</h1>\r\n<hr>\r\n<h2>Các đoạn hay từ quyển The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations.</h2>\r\n<br>\r\n<h3>Leader and Worker</h3>\r\n<h4>Worker</h4>\r\nWe explicitly state the problem we are seeking to solve, our hypothesis of how our proposed countermeasure will solve it, our methods for testing that hypothesis, our interpretation of the results, and our use of learnings to inform the next iteration.\r\n<br>\r\n<br>\r\n<h4>Leader</h4>\r\nThe leader helps coach the person conducting the experiment with questions that may include:\r\n<li>What was your last step and what happened?</li>\r\n<li>What did you learn?</li>\r\n<li>What is your condition now?</li>\r\n<li>What is your next target condition?</li>\r\n<li>What obstacle are you working on now?</li>\r\n<li>What is your next step?</li>\r\n<li>What is your expected outcome?</li>\r\n<li>When can we check?</li>\r\n<br>\r\n<h3>Invite Ops to our dev standups</h3>\r\n<p>\r\nOne of the Dev rituals popularized by Scrum is the daily standup (although physically standing up have become distinctly optional in remote teams), a quick meeting where everyone on the team gets together and presents to each other three things: what was done yesterday, what is going to be done today, and what is preventing you from getting your work done. \r\n</p>\r\n<p>\r\n    The purpose of this ceremony is to radiate information throughout the team and to understand the work that is being done and is going to be done. By having team members present this information to each other, we learn about any tasks that are experiencing roadblocks and discover ways to help each other move our work toward completion. Furthermore, by having managers present, we can quickly resolve prioritization and resource conflicts.\r\n</p>\r\n<h3>Development process</h3>\r\n<p>at the end of each development interval, we must have integrated, tested, working, and potentially shippable code, demonstrated in a production-like environment, created from trunk using a one-click process, and validated with automated tests.</p>\r\n<hr>\r\n<h2>Docker</h2>\r\n<p>Docker can containerize everything, from webserver, web app, to database. It is really easy to clean. Although microservices seem to take lots of space and memory -> Help deliver and set up an app between dev using 1 click, making it independent from programming language and database selections.</p>\r\n<p>\r\nDocker helps not to separate between prod env and dev env. This helps dev stay as close to the prod environment as possible.\r\n<li>Same path</li>\r\n<li>Same config</li>\r\n<li>Same package information</li>\r\n</p>\r\n<br>\r\n<br>\r\n<br>',30,'2023-08-16'),(2,'Useful stuffs','Useful website, software, command, link, ...','<h1>\r\n    Useful stuffs\r\n</h1>\r\n<br>\r\n<h2>Useful Websites</h2>\r\nPagespeed Insight (<a href=\"https://pagespeed.web.dev/\">https://pagespeed.web.dev/</a>): Tool đánh giá chỉ ra vấn đề website đang gặp phải.\r\n<br>\r\nGoogle Search Console (<a href=\"https://search.google.com/\">https://search.google.com/</a>): Tool theo dõi performance và ranking website. Xem các url nào đã được đánh index.\r\n<br>\r\nCodebeautify highlighter (<a href=\"https://codebeautify.org/code-highlighter\">https://codebeautify.org/code-highlighter</a>): Online syntax highlighter\r\n<br>\r\nDBDiagram (<a href=\"https://dbdiagram.io/\">https://dbdiagram.io/</a>): Giúp drawn database. Có thể import file MySQL và export lệnh tạo MySQL. Mình dùng để vẽ database tự động khi import file MySQL và sửa lại lệnh tạo table khi thay đổi cấu trúc database.\r\n<br>\r\nGoogle Bard (<a href=\"https://bard.google.com/\">https://bard.google.com/</a>): Google Chatbot. Trả lời khá OK. Có thể đưa nhiều link đọc tham khảo.\r\n<br>\r\nJira Atlassian (<a href=\"https://www.atlassian.com/software/jira\">https://www.atlassian.com/software/jira</a>): Kanban Board. Mình dùng để note việc cần làm theo queue.\r\n<br>\r\n<br>\r\n<h2>Useful commands</h2>\r\n<h5>Script cài MySQL</h5>\r\n<pre><code id=\"script_mysql\" style=\"color:rgb(68, 68, 68); font-weight:400;background-color:rgb(240, 240, 240);background:rgb(240, 240, 240);display:block;padding: .5em;\">sudo wget https:<span style=\"color:rgb(136, 136, 136); font-weight:400;\">//repo.mysql.com/mysql-apt-config_0.8.26-1_all.deb</span>\r\nsudo dpkg -i mysql-apt-config_0<span style=\"color:rgb(136, 0, 0); font-weight:400;\">.8</span><span style=\"color:rgb(136, 0, 0); font-weight:400;\">.26</span><span style=\"color:rgb(136, 0, 0); font-weight:400;\">-1</span>_all.deb\r\nsudo apt-<span style=\"color:rgb(68, 68, 68); font-weight:700;\">get</span> update\r\nsudo apt-<span style=\"color:rgb(68, 68, 68); font-weight:700;\">get</span> install mysql-server -y\r\nsudo rm mysql-apt-config_0<span style=\"color:rgb(136, 0, 0); font-weight:400;\">.8</span><span style=\"color:rgb(136, 0, 0); font-weight:400;\">.26</span><span style=\"color:rgb(136, 0, 0); font-weight:400;\">-1</span>_all.deb</code></pre>\r\n<h5>Remove known key from IP SSH</h5>\r\n<pre><code style=\"color:rgb(68, 68, 68); font-weight:400;background-color:rgb(240, 240, 240);background:rgb(240, 240, 240);display:block;padding: .5em;\">ssh-keygen -R <span style=\"color:rgb(68, 68, 68); font-weight:400;\">&lt;<span style=\"color:rgb(68, 68, 68); font-weight:700;\">host</span>&gt;</span></code></pre>\r\n<h5>Liệt kê các tiến trình đang chạy Linux</h5>\r\n<pre><code style=\"color:rgb(68, 68, 68); font-weight:400;background-color:rgb(240, 240, 240);background:rgb(240, 240, 240);display:block;padding: .5em;\">systemctl --<span style=\"color:rgb(57, 115, 0); font-weight:400;\">type</span>=service --state=running</code></pre>\r\n<h5>Tạo cert thủ công certbot</h5>\r\n<pre><code style=\"color:rgb(68, 68, 68); font-weight:400;background-color:rgb(240, 240, 240);background:rgb(240, 240, 240);display:block;padding: .5em;\">certbot certonly <span style=\"color:rgb(136, 136, 136); font-weight:400;\">--manual --preferred-challenges=dns </span></code></pre>\r\n<h2>Useful Link</h2>\r\n<a href=\"https://dev.mysql.com/doc/refman/8.1/en/\">https://dev.mysql.com/doc/refman/8.1/en/</a>: Trang docs MySQL (Search mãi mới ra, ảo thật đấy)\r\n<br>\r\n<br>\r\n<h2>Useful Software</h2>\r\nTerminus (<a href=\"https://termius.com/\">https://termius.com/</a>): SSH Terminal. Hỗ trợ nhiều OS\r\n<br>\r\n<br>\r\n<strong>Tính năng:</strong>\r\n<li>Nhóm server lại quản lý</li>\r\n<li>SSH theo user</li>\r\n<li>Split screen</li>\r\n<li>Drag item từ các server với nhau</li>\r\n<li>Thay key ssh nếu thấy host thay đổi</li>\r\n<br>\r\n<h2>Useful Keyboard Combination MacOS</h2>\r\n<p><kbd>Ctrl</kbd> <kbd>Space</kbd> <kbd>~</kbd> : Đổi input source</p>\r\n<p><kbd>Click</kbd> 3 lần: Bôi đen dòng</p>\r\n<h5>Vscode</h5>\r\n    <p><kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>~</kbd> : Tạo terminal mới</p>\r\n    <p><kbd>Option</kbd> <kbd><span>&#8593;</span></kbd> : Di chuyển code giữa các dòng</p>\r\n    <p><kbd>Command</kbd> <kbd><span>&#8592;</span></kbd> : Về đầu dòng</p>\r\n    <p><kbd>Command</kbd> <kbd>&#92;</kbd> : Split Terminal</p>\r\n<br>\r\n<br>\r\n<style>\r\n    kbd {\r\n      border-radius: 2px;\r\n      padding: 2px;\r\n      border: 1px solid black;\r\n    }\r\n</style>   ',43,'2023-08-16'),(3,'WSGI Server Django','Một số link liên quan đến WSGI','<h1>WSGI</h1>\r\n<br>\r\n<li>\r\n    Gunicorn and NGINX: <a href=\"https://vsupalov.com/gunicorn-and-nginx/\">https://vsupalov.com/gunicorn-and-nginx/</a> (Really useful, clear and concise explanation)\r\n</li>\r\n<li>\r\n    Django Deployment Book: <a href=\"https://djangodeployment.com/\">https://djangodeployment.com/</a>\r\n</li>\r\n<li>\r\n    PEP 333: <a href=\"https://peps.python.org/pep-0333/\">https://peps.python.org/pep-0333/</a>\r\n</li>\r\n<li>\r\n    WSGI: <a href=\"https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface\">https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface</a>\r\n</li>\r\n<li>\r\n    CGI: <a href=\"https://en.wikipedia.org/wiki/Common_Gateway_Interface\">https://en.wikipedia.org/wiki/Common_Gateway_Interface</a>\r\n</li>\r\n<li>\r\n    FastCGI: <a href=\"https://en.wikipedia.org/wiki/FastCGI\">https://en.wikipedia.org/wiki/FastCGI</a>\r\n</li>',9,'2023-08-16'),(4,'FLUSH PRIVILEGES command in MySQL','','<h1>FLUSH PRIVILEGES Command MySQL</h1>\r\nThe <code class=\"bg-light border\">FLUSH PRIVILEGES</code> command in MySQL is used to reload the grant tables. This means that it forces MySQL to read the grant tables from disk again and apply any changes that have been made to them.\r\n<br>\r\n<br>\r\nThe grant tables contain information about the privileges that have been granted to users and roles. When you change the privileges for a user or role, the changes are not applied immediately. Instead, they are cached in memory. The <code class=\"bg-light border\">FLUSH PRIVILEGES</code> command forces MySQL to flush the cache and read the grant tables from disk again.\r\n<br>\r\nThe <code class=\"bg-light border\">FLUSH PRIVILEGES</code> command is typically used after you have made changes to the grant tables. For example, if you create a new user or grant a new privilege to an existing user, you should run the <code class=\"bg-light border\">FLUSH PRIVILEGES</code> command to make sure that the changes are applied to all connections.\r\n<br>\r\n<br>\r\nThe <code class=\"bg-light border\">FLUSH PRIVILEGES</code> command can also be used to troubleshoot problems with privileges. If you are having problems connecting to a database or accessing a table, you can try running the FLUSH PRIVILEGES command to see if it resolves the problem.\r\nHere is an example of how to use the <code class=\"bg-light border\">FLUSH PRIVILEGES</code> command:\r\n<pre>\r\n    <code id=\"htmlViewer\" style=\"color:rgb(68, 68, 68); font-weight:400;background-color:rgb(240, 240, 240);background:rgb(240, 240, 240);display:block;padding: .5em;\">mysql&gt; FLUSH PRIVILEGES;\r\nQuery OK, <span style=\"color:rgb(136, 0, 0); font-weight:400;\">0</span> rows <span class=\"hljs-title function_\">affected</span> <span style=\"color:rgb(68, 68, 68); font-weight:400;\">(<span style=\"color:rgb(136, 0, 0); font-weight:400;\">0.00</span> sec)</span></code></pre>\r\n\r\nThis command will force MySQL to flush the grant tables and read them from disk again.\r\n<br><br>\r\nIt is important to note that the <code class=\"bg-light border\">FLUSH PRIVILEGES</code> command will disconnect all current connections to the MySQL server. This means that any users who are currently logged in will be disconnected.\r\n<br><br>\r\nIf you are running the <code class=\"bg-light border\">FLUSH PRIVILEGES</code> command on a production server, you should make sure that there are no users who are currently logged in. You can use the <code class=\"bg-light border\">SHOW PROCESSLIST;</code> command to check the list of active connections.\r\n<br><br>\r\nThe <code class=\"bg-light border\">FLUSH PRIVILEGES</code> command is a powerful tool that can be used to manage privileges in MySQL. However, it is important to use it carefully and to understand the potential consequences.\r\n<br><br>\r\nHere are some of the benefits of using the <code class=\"bg-light border\">FLUSH PRIVILEGES</code> command:\r\n<li>It ensures that all changes to the grant tables are applied to all connections.</li>\r\n<li>It can be used to troubleshoot problems with privileges.</li>\r\n<li>It can be used to reset the privileges for a user or role.</li>\r\n<br>\r\nHere are some of the risks of using the <code class=\"bg-light border\">FLUSH PRIVILEGES</code> command:\r\n<li>It can disconnect all current connections to the MySQL server.</li>\r\n<li>It can be used to accidentally grant or revoke privileges to users.</li>\r\n<li>It is important to weigh the benefits and risks of using the <code class=\"bg-light border\">FLUSH PRIVILEGES</code> command before using it.</li>\r\n<br>\r\nSource: Google Bard\r\n<br>\r\n<br>',20,'2023-08-16'),(5,'Các câu lệnh tạo bảng MySQL dùng với trang web của tôi','','<h1>Các câu lệnh tạo bảng MySQL dùng với website database</h1>\r\n<pre>\r\n <code id=\"htmlViewer\" style=\"color:rgb(68, 68, 68); font-weight:400;background-color:rgb(240, 240, 240);background:rgb(240, 240, 240);display:block;padding: .5em;\"><span style=\"color:rgb(68, 68, 68); font-weight:700;\">CREATE</span> DATABASE my_data;\r\nUSE my_data;\r\n\r\n<span style=\"color:rgb(68, 68, 68); font-weight:700;\">CREATE</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">TABLE</span> `running_data` (\r\n  `<span style=\"color:rgb(68, 68, 68); font-weight:700;\">day</span>` <span style=\"color:rgb(136, 0, 0); font-weight:400;\">date</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">DEFAULT</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">NULL</span>,\r\n  `duration` <span style=\"color:rgb(136, 0, 0); font-weight:400;\">int</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">DEFAULT</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">NULL</span>,\r\n  `distance` <span style=\"color:rgb(136, 0, 0); font-weight:400;\">float</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">DEFAULT</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">NULL</span>\r\n);\r\n\r\n<span style=\"color:rgb(68, 68, 68); font-weight:700;\">CREATE</span> DATABASE blog;\r\nUSE blog;\r\n\r\n<span style=\"color:rgb(68, 68, 68); font-weight:700;\">CREATE</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">TABLE</span> `blog` (\r\n  `id` <span style=\"color:rgb(136, 0, 0); font-weight:400;\">int</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">PRIMARY</span> KEY <span style=\"color:rgb(68, 68, 68); font-weight:700;\">NOT</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">NULL</span> AUTO_INCREMENT,\r\n  `title` <span style=\"color:rgb(136, 0, 0); font-weight:400;\">varchar</span>(<span style=\"color:rgb(136, 0, 0); font-weight:400;\">255</span>) <span style=\"color:rgb(68, 68, 68); font-weight:700;\">NOT</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">NULL</span>,\r\n  `snippet` <span style=\"color:rgb(136, 0, 0); font-weight:400;\">varchar</span>(<span style=\"color:rgb(136, 0, 0); font-weight:400;\">255</span>) <span style=\"color:rgb(68, 68, 68); font-weight:700;\">NOT</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">NULL</span>,\r\n  `content` text <span style=\"color:rgb(68, 68, 68); font-weight:700;\">NOT</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">NULL</span>,\r\n  `total_view` <span style=\"color:rgb(136, 0, 0); font-weight:400;\">int</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">DEFAULT</span> &quot;0&quot;,\r\n  `<span style=\"color:rgb(136, 0, 0); font-weight:400;\">date</span>` <span style=\"color:rgb(136, 0, 0); font-weight:400;\">date</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">DEFAULT</span> (curdate())\r\n);\r\n\r\n<span style=\"color:rgb(68, 68, 68); font-weight:700;\">CREATE</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">TABLE</span> `comment` (\r\n  `id` <span style=\"color:rgb(136, 0, 0); font-weight:400;\">int</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">PRIMARY</span> KEY <span style=\"color:rgb(68, 68, 68); font-weight:700;\">NOT</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">NULL</span> AUTO_INCREMENT,\r\n  `<span style=\"color:rgb(68, 68, 68); font-weight:700;\">user</span>` <span style=\"color:rgb(136, 0, 0); font-weight:400;\">varchar</span>(<span style=\"color:rgb(136, 0, 0); font-weight:400;\">255</span>) <span style=\"color:rgb(68, 68, 68); font-weight:700;\">DEFAULT</span> &quot;anonymous&quot;,\r\n  `content` text <span style=\"color:rgb(68, 68, 68); font-weight:700;\">NOT</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">NULL</span>,\r\n  `blog_id` <span style=\"color:rgb(136, 0, 0); font-weight:400;\">int</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">NOT</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">NULL</span>\r\n);\r\n\r\n<span style=\"color:rgb(68, 68, 68); font-weight:700;\">CREATE</span> INDEX `blog_id` <span style=\"color:rgb(68, 68, 68); font-weight:700;\">ON</span> `comment` (`blog_id`);\r\n\r\n<span style=\"color:rgb(68, 68, 68); font-weight:700;\">ALTER</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">TABLE</span> `comment` <span style=\"color:rgb(68, 68, 68); font-weight:700;\">ADD</span> <span style=\"color:rgb(68, 68, 68); font-weight:700;\">CONSTRAINT</span> `comment_ibfk_1` <span style=\"color:rgb(68, 68, 68); font-weight:700;\">FOREIGN</span> KEY (`blog_id`) <span style=\"color:rgb(68, 68, 68); font-weight:700;\">REFERENCES</span> `blog` (`id`);</code></pre>\r\n<br>',9,'2023-08-18'),(6,'kswapd0 process','','<h1>kswapd0 process</h1>\r\n<p>\r\n    The kswapd0 process is a kernel thread in the Linux operating system that manages virtual memory and swap space. It is responsible for freeing up memory when the system is running low.\r\n    When the system is running low on memory, kswapd0 will move inactive pages (pages that are not being used by any running process) to swap space. Swap space is a portion of the hard drive that is used to store memory pages that are not currently being used.\r\n    Moving pages to swap space can free up memory for other processes, but it can also cause the system to slow down. This is because accessing pages from swap space is slower than accessing pages from memory.\r\n    If kswapd0 is using a high percentage of CPU, it is a sign that the system is running low on memory. There are a few things you can do to fix this:\r\n</p>\r\n<li>Increase the amount of RAM in your system.</li>\r\n<li>Close any unnecessary programs.</li>\r\n<li>\r\n    Adjust the swappiness value. The swappiness value is a setting that controls how aggressively the kernel will swap memory pages to disk. A higher swappiness value means that the kernel will be more likely to swap pages to disk, which can free up memory for other processes. However, a higher swappiness value can also slow down the system.\r\n</li>\r\n<li>\r\n    Scan for malware. Malware can sometimes cause high CPU usage by kswapd0.\r\n</li>\r\n<br>\r\n<p>\r\n    If you are still having problems with kswapd0, you can try rebooting your system. This will clear out any temporary files that may be causing the problem.\r\n    Here are some additional things to keep in mind about the kswapd0 process:\r\n</p>\r\n<li>\r\n    The kswapd0 process is a normal part of the Linux operating system. It is not a virus or malware.\r\n</li>\r\n<li>\r\n    The kswapd0 process will only run when the system is running low on memory.\r\n</li>\r\n<li>\r\n    The kswapd0 process will not cause any permanent damage to your system.\r\n</li>\r\n<br>\r\nSource: Google Bard\r\n<br>\r\n<br>',3,'2023-08-26'),(7,'Một số lỗi gặp phải trong quá trình deploy và vận hành website','Note lại chi tiết những lỗi gặp phải để sau tránh ...','<h1>Một số lỗi gặp phải trong quá trình deploy và vận hành website</h1>\r\n<br>\r\n<h2>Website treo</h2>\r\n<strong>Hiện tượng</strong>\r\n<li>Kết nối đến server bị timeout</li>\r\n<li>Không thể ssh đến server</li>\r\n<li>Website trả kết quả ra quá chậm</li>\r\n<br>\r\n<strong>Những gì thực hiện</strong>\r\n<li>Tạo server mới, deploy 1 click.</li>\r\n<li>Sau khi tạo, 1 thời gian server cũng đơ.</li>\r\n<li>Xóa đi tạo lại, tích hợp monitor agent của Google Cloud</li>\r\n<li>Check được thông tin process, thông tin CPU, thông tin RAM. CPU 100%, trong đó 70% CPU usage thuộc về process kswapd0. Memory 85%</li>\r\n<li>Debug process nào chiếm nhiều RAM và CPU, fix.</li>\r\n<br>\r\n<strong>Nguyên nhân:</strong> <p>mysql dùng nhiều ram -> kswapd0 tăng -> cpu tăng -> treo server.</p>\r\n<strong>Cách khắc phục: </strong> Làm theo hướng dẫn tại <a href=\"https://stackoverflow.com/questions/45516971/why-is-mysql-consuming-so-much-memory\">https://stackoverflow.com/questions/45516971/why-is-mysql-consuming-so-much-memory</a>\r\n<br>\r\n<br>\r\n<strong>Kết quả</strong>\r\n<li>Memory 85% -> 61%</li>\r\n<li>Process by memory /usr/sbin/mysqld 376 -> 154 MiB</li>\r\n<li>Process by state 861 -> 614 / 1000 MiB</li>\r\n<li>CPU 66% (100% khi treo) -> 10% </li>\r\n<br>\r\n<strong>Rút ra</strong>\r\n<li>Khả năng monitor (Ram/CPU/process) và deploy 1 click là rất quan trọng.</li>\r\n<br>\r\n<hr>\r\n<h2>Deploy web application lỗi</h2>\r\n<strong>Nguyên nhân: </strong>Không đẩy toàn bộ code lên git. Do đó code chạy bình thường trên local nhưng code trên git bị thiếu mất module dẫn đến không chạy.\r\n<br><br><br><br>',5,'2023-08-26');
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

-- Dump completed on 2023-08-27 14:14:40
