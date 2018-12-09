-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: 52.66.82.245    Database: smsystem
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add announcement',1,'add_announcement'),(2,'Can change announcement',1,'change_announcement'),(3,'Can delete announcement',1,'delete_announcement'),(4,'Can view announcement',1,'view_announcement'),(5,'Can add coach',2,'add_coach'),(6,'Can change coach',2,'change_coach'),(7,'Can delete coach',2,'delete_coach'),(8,'Can view coach',2,'view_coach'),(9,'Can add complaint',3,'add_complaint'),(10,'Can change complaint',3,'change_complaint'),(11,'Can delete complaint',3,'delete_complaint'),(12,'Can view complaint',3,'view_complaint'),(13,'Can add performance',4,'add_performance'),(14,'Can change performance',4,'change_performance'),(15,'Can delete performance',4,'delete_performance'),(16,'Can view performance',4,'view_performance'),(17,'Can add player',5,'add_player'),(18,'Can change player',5,'change_player'),(19,'Can delete player',5,'delete_player'),(20,'Can view player',5,'view_player'),(21,'Can add schedule',6,'add_schedule'),(22,'Can change schedule',6,'change_schedule'),(23,'Can delete schedule',6,'delete_schedule'),(24,'Can view schedule',6,'view_schedule'),(25,'Can add sport',7,'add_sport'),(26,'Can change sport',7,'change_sport'),(27,'Can delete sport',7,'delete_sport'),(28,'Can view sport',7,'view_sport'),(29,'Can add student',8,'add_student'),(30,'Can change student',8,'change_student'),(31,'Can delete student',8,'delete_student'),(32,'Can view student',8,'view_student'),(33,'Can add tournament',9,'add_tournament'),(34,'Can change tournament',9,'change_tournament'),(35,'Can delete tournament',9,'delete_tournament'),(36,'Can view tournament',9,'view_tournament'),(37,'Can add log entry',10,'add_logentry'),(38,'Can change log entry',10,'change_logentry'),(39,'Can delete log entry',10,'delete_logentry'),(40,'Can view log entry',10,'view_logentry'),(41,'Can add permission',11,'add_permission'),(42,'Can change permission',11,'change_permission'),(43,'Can delete permission',11,'delete_permission'),(44,'Can view permission',11,'view_permission'),(45,'Can add group',12,'add_group'),(46,'Can change group',12,'change_group'),(47,'Can delete group',12,'delete_group'),(48,'Can view group',12,'view_group'),(49,'Can add user',13,'add_user'),(50,'Can change user',13,'change_user'),(51,'Can delete user',13,'delete_user'),(52,'Can view user',13,'view_user'),(53,'Can add content type',14,'add_contenttype'),(54,'Can change content type',14,'change_contenttype'),(55,'Can delete content type',14,'delete_contenttype'),(56,'Can view content type',14,'view_contenttype'),(57,'Can add session',15,'add_session'),(58,'Can change session',15,'change_session'),(59,'Can delete session',15,'delete_session'),(60,'Can view session',15,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$120000$lBcmB3L73OWx$MdyiVQU4dh8ztLNxiDaUztciBiw4VM/e3A3rTztGXag=','2018-11-16 19:15:48.025764',1,'charangv','','','charan@gmail.com',1,1,'2018-11-01 18:26:06.012494');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-11-01 19:02:39.753227','2','2',3,'',3,1),(2,'2018-11-01 19:02:47.571429','1','1',3,'',3,1),(3,'2018-11-02 03:13:01.559020','3','3',3,'',5,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (10,'admin','logentry'),(12,'auth','group'),(11,'auth','permission'),(13,'auth','user'),(14,'contenttypes','contenttype'),(15,'sessions','session'),(1,'smsystem','announcement'),(2,'smsystem','coach'),(3,'smsystem','complaint'),(4,'smsystem','performance'),(5,'smsystem','player'),(6,'smsystem','schedule'),(7,'smsystem','sport'),(8,'smsystem','student'),(9,'smsystem','tournament');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-11-01 18:24:02.660674'),(2,'auth','0001_initial','2018-11-01 18:24:05.209247'),(3,'admin','0001_initial','2018-11-01 18:24:05.916133'),(4,'admin','0002_logentry_remove_auto_add','2018-11-01 18:24:06.125591'),(5,'admin','0003_logentry_add_action_flag_choices','2018-11-01 18:24:06.335453'),(6,'contenttypes','0002_remove_content_type_name','2018-11-01 18:24:06.822374'),(7,'auth','0002_alter_permission_name_max_length','2018-11-01 18:24:07.063565'),(8,'auth','0003_alter_user_email_max_length','2018-11-01 18:24:07.338060'),(9,'auth','0004_alter_user_username_opts','2018-11-01 18:24:07.558759'),(10,'auth','0005_alter_user_last_login_null','2018-11-01 18:24:07.848052'),(11,'auth','0006_require_contenttypes_0002','2018-11-01 18:24:08.095902'),(12,'auth','0007_alter_validators_add_error_messages','2018-11-01 18:24:09.035037'),(13,'auth','0008_alter_user_username_max_length','2018-11-01 18:24:09.300856'),(14,'auth','0009_alter_user_last_name_max_length','2018-11-01 18:24:09.566115'),(15,'sessions','0001_initial','2018-11-01 18:24:09.984222'),(16,'smsystem','0001_initial','2018-11-01 18:24:15.132389');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('06u56i4rmx0ygna34duaevfba6ixl7u3','ZTRhNWM5OTQ4Nzg4NWEzMTRiZTJkNTNlOWI1MTU4NWIyNjdiNjNkNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiMjZmMTMwZDhhZWQ0MzVlOTQxZjQwOGNiOWFiYTUyMjRkYTc2N2VmMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2018-11-23 06:16:44.481856'),('0iguf6tklgejql256pct0ew7kh8muzec','MmI2NDY5YTc2MDZkYzYxNzc3MGEwYTQ3NmUwNmNjZTFiMWQ2OTQxZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyNmYxMzBkOGFlZDQzNWU5NDFmNDA4Y2I5YWJhNTIyNGRhNzY3ZWYzIn0=','2018-11-16 04:23:13.791731'),('9dh3pygz7wjlakuwxmawujqsgnqctfyk','MzZhMzU5OTRjZGI4NDM0NDBmMmEyNWI0YmJkYmZjNzIxMGVhNmMwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5N2Q3YmQwZWRhMmE4MjQwMWE4ZGQyNzIwMzExMDQ0NjI0YmNmZDZkIn0=','2018-11-30 19:12:11.289346'),('d5t7pxfd6f0mae6dhgf11fb3xqx4mird','MmI2NDY5YTc2MDZkYzYxNzc3MGEwYTQ3NmUwNmNjZTFiMWQ2OTQxZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyNmYxMzBkOGFlZDQzNWU5NDFmNDA4Y2I5YWJhNTIyNGRhNzY3ZWYzIn0=','2018-11-30 05:33:17.384923'),('ir9eb9qhr0pww4z2zdwlr3z30gijq6zs','NzY4ZTE3NTAxYWM3ZjkxNmViNjJmOWM3OTNjYTY4ODAwOGMxNGMyYzp7Il9hdXRoX3VzZXJfaGFzaCI6IjI2ZjEzMGQ4YWVkNDM1ZTk0MWY0MDhjYjlhYmE1MjI0ZGE3NjdlZjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2018-11-23 06:55:47.223806'),('m648c1ivw03vr18v39zzqc5g0x3zes7f','MzZhMzU5OTRjZGI4NDM0NDBmMmEyNWI0YmJkYmZjNzIxMGVhNmMwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5N2Q3YmQwZWRhMmE4MjQwMWE4ZGQyNzIwMzExMDQ0NjI0YmNmZDZkIn0=','2018-11-30 19:15:48.159157'),('pn3zbtb604dxlo8ztehc3irsx3lcnzyj','NzYxYzIxNWVhZGNlODY3YzBjNmE5MDA0NmQzMzhlNDEwNjAyNzJmZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjI2ZjEzMGQ4YWVkNDM1ZTk0MWY0MDhjYjlhYmE1MjI0ZGE3NjdlZjMiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2018-11-16 05:06:34.383678'),('vh1fhay960jd6jxf7xoi6c2vzosiy91k','MmI2NDY5YTc2MDZkYzYxNzc3MGEwYTQ3NmUwNmNjZTFiMWQ2OTQxZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyNmYxMzBkOGFlZDQzNWU5NDFmNDA4Y2I5YWJhNTIyNGRhNzY3ZWYzIn0=','2018-11-29 13:54:16.790051');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `smsystem_announcement`
--

DROP TABLE IF EXISTS `smsystem_announcement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `smsystem_announcement` (
  `announcement_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender` varchar(50) NOT NULL,
  `message` varchar(500) NOT NULL,
  `datetime` datetime(6) NOT NULL,
  `created_by` varchar(50) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `modified_by` varchar(50) NOT NULL,
  `modified_at` varchar(50) NOT NULL,
  PRIMARY KEY (`announcement_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `smsystem_announcement`
--

LOCK TABLES `smsystem_announcement` WRITE;
/*!40000 ALTER TABLE `smsystem_announcement` DISABLE KEYS */;
INSERT INTO `smsystem_announcement` VALUES (1,'charan','hai','2018-11-01 18:31:37.897254','','2018-11-01 18:31:37.897385','',''),(2,'admin','welcome to iiits sportsclub','2018-11-01 20:18:21.430775','','2018-11-01 20:18:21.431013','',''),(3,'charan','hai to all','2018-11-02 01:04:10.786498','','2018-11-02 01:04:10.786692','',''),(4,'manoj','hai every one','2018-11-02 01:04:35.542032','','2018-11-02 01:04:35.542183','',''),(5,'manoj','hai','2018-11-02 01:38:59.502451','','2018-11-02 01:38:59.502522','',''),(6,'charan','hai all','2018-11-02 02:04:27.881059','','2018-11-02 02:04:27.881242','',''),(7,'admin','hai','2018-11-02 03:37:52.068817','','2018-11-02 03:37:52.068989','',''),(8,'manoj','hello guys','2018-11-02 03:41:30.056431','','2018-11-02 03:41:30.056528','',''),(9,'admin','today is important day','2018-11-02 04:18:37.449279','','2018-11-02 04:18:37.449424','',''),(10,'admin','there is a cricket match today','2018-11-02 04:24:05.318869','','2018-11-02 04:24:05.319117','',''),(11,'admin','today there is a cricket match at 3.00 p.m','2018-11-02 05:07:06.226354','','2018-11-02 05:07:06.226514','',''),(12,'admin','hi\r\n','2018-11-16 06:29:25.621389','','2018-11-16 06:29:25.621427','',''),(13,'manoj','hai','2018-11-16 16:44:18.514470','','2018-11-16 16:44:18.514613','',''),(14,'manoj','good bye','2018-11-16 16:55:05.085509','','2018-11-16 16:55:05.085653','',''),(15,'manoj','hello','2018-11-16 16:57:47.132195','','2018-11-16 16:57:47.132291','',''),(16,'manoj','fdfs','2018-11-16 17:02:09.386883','','2018-11-16 17:02:09.387041','',''),(17,'charan','fdgdf==-poijhgf','2018-11-16 17:26:04.145610','','2018-11-16 17:26:04.145819','',''),(18,'charan','hi','2018-11-16 18:50:51.282861','','2018-11-16 18:50:51.283051','',''),(19,'charan','hi','2018-11-16 18:55:11.509465','','2018-11-16 18:55:11.509585','',''),(20,'charan','hello','2018-11-17 04:32:10.283277','','2018-11-17 04:32:10.283451','','');
/*!40000 ALTER TABLE `smsystem_announcement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `smsystem_coach`
--

DROP TABLE IF EXISTS `smsystem_coach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `smsystem_coach` (
  `coach_id` int(11) NOT NULL AUTO_INCREMENT,
  `coach_password` varchar(50) NOT NULL,
  `coach_name` varchar(50) NOT NULL,
  `coach_type` varchar(50) NOT NULL,
  `experience` int(11) NOT NULL,
  `contact` varchar(20) NOT NULL,
  `created_by` varchar(50) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `modified_by` varchar(50) NOT NULL,
  `modified_at` varchar(50) NOT NULL,
  `sport_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`coach_id`),
  KEY `smsystem_coach_sport_id_82c3771a_fk_smsystem_sport_sport_id` (`sport_id`),
  CONSTRAINT `smsystem_coach_sport_id_82c3771a_fk_smsystem_sport_sport_id` FOREIGN KEY (`sport_id`) REFERENCES `smsystem_sport` (`sport_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `smsystem_coach`
--

LOCK TABLES `smsystem_coach` WRITE;
/*!40000 ALTER TABLE `smsystem_coach` DISABLE KEYS */;
INSERT INTO `smsystem_coach` VALUES (1,'charangv','charan','bating coach',3,'7995323275','','2018-11-01 18:31:02.734448','','',1),(2,'iiitscoach','manoj','defefence',5,'9347236290','','2018-11-02 00:59:34.857085','','',2);
/*!40000 ALTER TABLE `smsystem_coach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `smsystem_complaint`
--

DROP TABLE IF EXISTS `smsystem_complaint`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `smsystem_complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `about` varchar(500) NOT NULL,
  `status` int(11) NOT NULL,
  `datetime` datetime(6) NOT NULL,
  `created_by` varchar(50) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `modified_by` varchar(50) NOT NULL,
  `modified_at` varchar(50) NOT NULL,
  `student_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`),
  KEY `smsystem_complaint_student_id_33aba958_fk_smsystem_` (`student_id`),
  CONSTRAINT `smsystem_complaint_student_id_33aba958_fk_smsystem_` FOREIGN KEY (`student_id`) REFERENCES `smsystem_student` (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `smsystem_complaint`
--

LOCK TABLES `smsystem_complaint` WRITE;
/*!40000 ALTER TABLE `smsystem_complaint` DISABLE KEYS */;
INSERT INTO `smsystem_complaint` VALUES (3,'match schedules should be made more efficiently ',0,'2018-11-01 19:03:31.510394','venkata','2018-11-01 19:03:31.510481','','','20160020127'),(4,'please add koko game ',0,'2018-11-02 01:59:45.052479','Pranav','2018-11-02 01:59:45.052544','','','20160020140'),(5,'this is evaluation',0,'2018-11-02 04:41:32.203696','Pranav','2018-11-02 04:41:32.203823','','','20160020140'),(6,'hai',0,'2018-11-16 16:09:06.974048','venkata','2018-11-16 16:09:06.974216','','','20160020127'),(7,'sasasas',0,'2018-11-16 19:56:39.169208','','2018-11-16 19:56:39.198222','','',NULL);
/*!40000 ALTER TABLE `smsystem_complaint` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `smsystem_performance`
--

DROP TABLE IF EXISTS `smsystem_performance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `smsystem_performance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role` varchar(50) NOT NULL,
  `performance_score` int(11) NOT NULL,
  `datetime` datetime(6) NOT NULL,
  `created_by` varchar(50) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `modified_by` varchar(50) NOT NULL,
  `modified_at` varchar(50) NOT NULL,
  `sport_id` int(11) DEFAULT NULL,
  `student_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `smsystem_performance_sport_id_f12d849e_fk_smsystem_` (`sport_id`),
  KEY `smsystem_performance_student_id_7ce5a7a7_fk_smsystem_` (`student_id`),
  CONSTRAINT `smsystem_performance_sport_id_f12d849e_fk_smsystem_` FOREIGN KEY (`sport_id`) REFERENCES `smsystem_sport` (`sport_id`),
  CONSTRAINT `smsystem_performance_student_id_7ce5a7a7_fk_smsystem_` FOREIGN KEY (`student_id`) REFERENCES `smsystem_student` (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `smsystem_performance`
--

LOCK TABLES `smsystem_performance` WRITE;
/*!40000 ALTER TABLE `smsystem_performance` DISABLE KEYS */;
INSERT INTO `smsystem_performance` VALUES (1,'batsman',8,'2018-11-01 19:13:29.061696','','2018-11-01 19:13:29.062031','','',1,'20160020127'),(2,'wicket keeper',7,'2018-11-01 19:16:43.018097','','2018-11-01 19:16:43.018282','','',1,'20160020127'),(3,'batsman',6,'2018-11-01 19:27:49.117608','charan','2018-11-01 19:27:49.117810','','',1,'20160010145');
/*!40000 ALTER TABLE `smsystem_performance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `smsystem_player`
--

DROP TABLE IF EXISTS `smsystem_player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `smsystem_player` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sport_id` int(11) DEFAULT NULL,
  `student_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `smsystem_player_sport_id_cc0547b6_fk_smsystem_sport_sport_id` (`sport_id`),
  KEY `smsystem_player_student_id_18f54547_fk_smsystem_` (`student_id`),
  CONSTRAINT `smsystem_player_sport_id_cc0547b6_fk_smsystem_sport_sport_id` FOREIGN KEY (`sport_id`) REFERENCES `smsystem_sport` (`sport_id`),
  CONSTRAINT `smsystem_player_student_id_18f54547_fk_smsystem_` FOREIGN KEY (`student_id`) REFERENCES `smsystem_student` (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `smsystem_player`
--

LOCK TABLES `smsystem_player` WRITE;
/*!40000 ALTER TABLE `smsystem_player` DISABLE KEYS */;
INSERT INTO `smsystem_player` VALUES (1,1,'20160020140'),(2,2,'20160020140');
/*!40000 ALTER TABLE `smsystem_player` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `smsystem_schedule`
--

DROP TABLE IF EXISTS `smsystem_schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `smsystem_schedule` (
  `schedule_id` int(11) NOT NULL AUTO_INCREMENT,
  `venue` varchar(50) NOT NULL,
  `result` varchar(50) DEFAULT NULL,
  `opponent_1` varchar(50) NOT NULL,
  `opponent_2` varchar(50) NOT NULL,
  `datetime` datetime(6) NOT NULL,
  `created_by` varchar(50) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `modified_by` varchar(50) NOT NULL,
  `modified_at` varchar(50) NOT NULL,
  `sport_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`schedule_id`),
  KEY `smsystem_schedule_sport_id_80ff3ff1_fk_smsystem_sport_sport_id` (`sport_id`),
  CONSTRAINT `smsystem_schedule_sport_id_80ff3ff1_fk_smsystem_sport_sport_id` FOREIGN KEY (`sport_id`) REFERENCES `smsystem_sport` (`sport_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `smsystem_schedule`
--

LOCK TABLES `smsystem_schedule` WRITE;
/*!40000 ALTER TABLE `smsystem_schedule` DISABLE KEYS */;
INSERT INTO `smsystem_schedule` VALUES (1,'iiitsground','ug1 won','ug1','ug2','2018-11-10 02:30:00.000000','','2018-11-01 20:39:26.090411','','',1),(2,'iiitsground','ug4 has won','ug1','ug4','2018-11-10 06:30:00.000000','','2018-11-02 01:00:14.350924','','',2),(3,'iiitsground','none','ug3','ug1','2018-11-21 14:40:00.000000','','2018-11-02 01:10:47.429954','','',2),(4,'iiitsground',NULL,'ug3','ug4','2018-12-01 04:30:00.000000','','2018-11-02 01:35:02.222214','','',2),(5,'iiitsground',NULL,'ug1','ug4','2018-11-11 04:00:00.000000','','2018-11-02 02:05:22.827014','','',1),(6,'iiitsground','ug1 won','ug3','ug1','2018-12-01 04:30:00.000000','','2018-11-16 18:58:13.939145','','',1);
/*!40000 ALTER TABLE `smsystem_schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `smsystem_sport`
--

DROP TABLE IF EXISTS `smsystem_sport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `smsystem_sport` (
  `sport_id` int(11) NOT NULL AUTO_INCREMENT,
  `sport_name` varchar(50) NOT NULL,
  `equipment` varchar(50) NOT NULL,
  `category` varchar(50) NOT NULL,
  `no_of_players` int(11) NOT NULL,
  `no_of_coaches` int(11) NOT NULL,
  `created_by` varchar(50) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `modified_by` varchar(50) NOT NULL,
  `modified_at` varchar(50) NOT NULL,
  PRIMARY KEY (`sport_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `smsystem_sport`
--

LOCK TABLES `smsystem_sport` WRITE;
/*!40000 ALTER TABLE `smsystem_sport` DISABLE KEYS */;
INSERT INTO `smsystem_sport` VALUES (1,'cricket','bat,ball,wickets,helmet,pads','outdoor',0,1,'','2018-11-01 18:30:29.570294','',''),(2,'basket ball','basket balls','outdoor',0,1,'','2018-11-02 00:58:55.313144','',''),(3,'kabadi','kneepads','outdoor',0,0,'','2018-11-02 01:54:03.857307','','');
/*!40000 ALTER TABLE `smsystem_sport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `smsystem_student`
--

DROP TABLE IF EXISTS `smsystem_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `smsystem_student` (
  `student_id` varchar(255) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `middle_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `current_year` varchar(3) NOT NULL,
  `email` varchar(254) NOT NULL,
  `created_by` varchar(50) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `modified_by` varchar(50) NOT NULL,
  `modified_at` varchar(50) NOT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `smsystem_student`
--

LOCK TABLES `smsystem_student` WRITE;
/*!40000 ALTER TABLE `smsystem_student` DISABLE KEYS */;
INSERT INTO `smsystem_student` VALUES ('20160010093','SRI','HARSHAVARDHAN','S','M','3','sriharshavardhan.s16@iiits.in','','2018-11-02 03:36:13.597358','',''),('20160010145','Sandeep',' ','Potla','M','3','sandeep.p16@iiits.in','','2018-11-01 18:44:05.369280','',''),('20160020127','venkata','charan','gowthukatla','M','3','venkatacharan.g16@iiits.in','','2018-11-01 18:27:25.159331','',''),('20160020140','Pranav','','Meejuri','M','3','pranav.m16@iiits.in','','2018-11-02 01:56:18.983651','',''),('20160020154','Abhishek','','Thripurana','M','3','abhishek.t16@iiits.in','','2018-11-02 03:34:42.950930','','');
/*!40000 ALTER TABLE `smsystem_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `smsystem_tournament`
--

DROP TABLE IF EXISTS `smsystem_tournament`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `smsystem_tournament` (
  `tournament_id` int(11) NOT NULL AUTO_INCREMENT,
  `tournament_name` varchar(50) NOT NULL,
  `start_date` datetime(6) NOT NULL,
  `end_date` datetime(6) NOT NULL,
  `level` varchar(50) NOT NULL,
  `created_by` varchar(50) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `modified_by` varchar(50) NOT NULL,
  `modified_at` varchar(50) NOT NULL,
  `sport_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`tournament_id`),
  KEY `smsystem_tournament_sport_id_21fa7965_fk_smsystem_sport_sport_id` (`sport_id`),
  CONSTRAINT `smsystem_tournament_sport_id_21fa7965_fk_smsystem_sport_sport_id` FOREIGN KEY (`sport_id`) REFERENCES `smsystem_sport` (`sport_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `smsystem_tournament`
--

LOCK TABLES `smsystem_tournament` WRITE;
/*!40000 ALTER TABLE `smsystem_tournament` DISABLE KEYS */;
/*!40000 ALTER TABLE `smsystem_tournament` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-17 10:23:19
