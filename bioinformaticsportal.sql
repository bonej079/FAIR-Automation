-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 21, 2019 at 01:42 PM
-- Server version: 10.1.34-MariaDB
-- PHP Version: 7.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bioinformaticsportal`
--

-- --------------------------------------------------------

--
-- Table structure for table `account_emailaddress`
--

DROP DATABASE IF EXISTS BioinformaticsPortal;
DROP USER IF EXISTS 'portal_admin'@'localhost' ;
FLUSH PRIVILEGES;

CREATE DATABASE BioinformaticsPortal;
CREATE USER 'portal_admin'@'%' IDENTIFIED BY 'test-password';
GRANT ALL PRIVILEGES ON BioinformaticsPortal.* TO 'portal_admin'@'%';
FLUSH PRIVILEGES;
ALTER DATABASE `BioinformaticsPortal` CHARACTER SET utf8;

USE `BioinformaticsPortal` ;

CREATE TABLE `account_emailaddress` (
  `id` int(11) NOT NULL,
  `email` varchar(254) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `primary` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `account_emailaddress`
--

INSERT INTO `account_emailaddress` (`id`, `email`, `verified`, `primary`, `user_id`) VALUES
(2, 'bioinformaticsresourceportal@gmail.com', 1, 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `account_emailconfirmation`
--

CREATE TABLE `account_emailconfirmation` (
  `id` int(11) NOT NULL,
  `created` datetime(6) NOT NULL,
  `sent` datetime(6) DEFAULT NULL,
  `key` varchar(64) NOT NULL,
  `email_address_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add site', 6, 'add_site'),
(22, 'Can change site', 6, 'change_site'),
(23, 'Can delete site', 6, 'delete_site'),
(24, 'Can view site', 6, 'view_site'),
(25, 'Can add email address', 7, 'add_emailaddress'),
(26, 'Can change email address', 7, 'change_emailaddress'),
(27, 'Can delete email address', 7, 'delete_emailaddress'),
(28, 'Can view email address', 7, 'view_emailaddress'),
(29, 'Can add email confirmation', 8, 'add_emailconfirmation'),
(30, 'Can change email confirmation', 8, 'change_emailconfirmation'),
(31, 'Can delete email confirmation', 8, 'delete_emailconfirmation'),
(32, 'Can view email confirmation', 8, 'view_emailconfirmation'),
(33, 'Can add social account', 9, 'add_socialaccount'),
(34, 'Can change social account', 9, 'change_socialaccount'),
(35, 'Can delete social account', 9, 'delete_socialaccount'),
(36, 'Can view social account', 9, 'view_socialaccount'),
(37, 'Can add social application', 10, 'add_socialapp'),
(38, 'Can change social application', 10, 'change_socialapp'),
(39, 'Can delete social application', 10, 'delete_socialapp'),
(40, 'Can view social application', 10, 'view_socialapp'),
(41, 'Can add social application token', 11, 'add_socialtoken'),
(42, 'Can change social application token', 11, 'change_socialtoken'),
(43, 'Can delete social application token', 11, 'delete_socialtoken'),
(44, 'Can view social application token', 11, 'view_socialtoken'),
(45, 'Can add user', 12, 'add_portaluser'),
(46, 'Can change user', 12, 'change_portaluser'),
(47, 'Can delete user', 12, 'delete_portaluser'),
(48, 'Can view user', 12, 'view_portaluser'),
(49, 'Can add tool', 13, 'add_tool'),
(50, 'Can change tool', 13, 'change_tool'),
(51, 'Can delete tool', 13, 'delete_tool'),
(52, 'Can view tool', 13, 'view_tool'),
(53, 'Can add fair score', 14, 'add_fairscore'),
(54, 'Can change fair score', 14, 'change_fairscore'),
(55, 'Can delete fair score', 14, 'delete_fairscore'),
(56, 'Can view fair score', 14, 'view_fairscore'),
(57, 'Can add reusability', 15, 'add_reusability'),
(58, 'Can change reusability', 15, 'change_reusability'),
(59, 'Can delete reusability', 15, 'delete_reusability'),
(60, 'Can view reusability', 15, 'view_reusability'),
(61, 'Can add interoperability', 16, 'add_interoperability'),
(62, 'Can change interoperability', 16, 'change_interoperability'),
(63, 'Can delete interoperability', 16, 'delete_interoperability'),
(64, 'Can view interoperability', 16, 'view_interoperability'),
(65, 'Can add findability', 17, 'add_findability'),
(66, 'Can change findability', 17, 'change_findability'),
(67, 'Can delete findability', 17, 'delete_findability'),
(68, 'Can view findability', 17, 'view_findability'),
(69, 'Can add accessibility', 18, 'add_accessibility'),
(70, 'Can change accessibility', 18, 'change_accessibility'),
(71, 'Can delete accessibility', 18, 'delete_accessibility'),
(72, 'Can view accessibility', 18, 'view_accessibility'),
(73, 'Can add pipeline tools', 19, 'add_pipelinetools'),
(74, 'Can change pipeline tools', 19, 'change_pipelinetools'),
(75, 'Can delete pipeline tools', 19, 'delete_pipelinetools'),
(76, 'Can view pipeline tools', 19, 'view_pipelinetools'),
(77, 'Can add pipeline', 20, 'add_pipeline'),
(78, 'Can change pipeline', 20, 'change_pipeline'),
(79, 'Can delete pipeline', 20, 'delete_pipeline'),
(80, 'Can view pipeline', 20, 'view_pipeline'),
(81, 'Can add private tool', 21, 'add_privatetool'),
(82, 'Can change private tool', 21, 'change_privatetool'),
(83, 'Can delete private tool', 21, 'delete_privatetool'),
(84, 'Can view private tool', 21, 'view_privatetool');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'account', 'emailaddress'),
(8, 'account', 'emailconfirmation'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(18, 'portal', 'accessibility'),
(14, 'portal', 'fairscore'),
(17, 'portal', 'findability'),
(16, 'portal', 'interoperability'),
(20, 'portal', 'pipeline'),
(19, 'portal', 'pipelinetools'),
(21, 'portal', 'privatetool'),
(15, 'portal', 'reusability'),
(13, 'portal', 'tool'),
(5, 'sessions', 'session'),
(6, 'sites', 'site'),
(9, 'socialaccount', 'socialaccount'),
(10, 'socialaccount', 'socialapp'),
(11, 'socialaccount', 'socialtoken'),
(12, 'users', 'portaluser');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-03-10 18:33:19.283175'),
(2, 'contenttypes', '0002_remove_content_type_name', '2019-03-10 18:33:20.049721'),
(3, 'auth', '0001_initial', '2019-03-10 18:33:22.991143'),
(4, 'auth', '0002_alter_permission_name_max_length', '2019-03-10 18:33:23.790362'),
(5, 'auth', '0003_alter_user_email_max_length', '2019-03-10 18:33:23.826297'),
(6, 'auth', '0004_alter_user_username_opts', '2019-03-10 18:33:23.866159'),
(7, 'auth', '0005_alter_user_last_login_null', '2019-03-10 18:33:23.901067'),
(8, 'auth', '0006_require_contenttypes_0002', '2019-03-10 18:33:23.932049'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2019-03-10 18:33:23.963897'),
(10, 'auth', '0008_alter_user_username_max_length', '2019-03-10 18:33:24.003262'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2019-03-10 18:33:24.039166'),
(12, 'users', '0001_initial', '2019-03-10 18:33:28.247736'),
(13, 'account', '0001_initial', '2019-03-10 18:33:30.371210'),
(14, 'account', '0002_email_max_length', '2019-03-10 18:33:31.122349'),
(15, 'admin', '0001_initial', '2019-03-10 18:33:32.783841'),
(16, 'admin', '0002_logentry_remove_auto_add', '2019-03-10 18:33:32.879586'),
(17, 'admin', '0003_logentry_add_action_flag_choices', '2019-03-10 18:33:32.980522'),
(18, 'sessions', '0001_initial', '2019-03-10 18:33:33.293415'),
(19, 'sites', '0001_initial', '2019-03-10 18:33:33.574168'),
(20, 'sites', '0002_alter_domain_unique', '2019-03-10 18:33:33.732030'),
(21, 'socialaccount', '0001_initial', '2019-03-10 18:33:40.193257'),
(22, 'socialaccount', '0002_token_max_lengths', '2019-03-10 18:33:41.824012'),
(23, 'socialaccount', '0003_extra_data_default_dict', '2019-03-10 18:33:41.884879'),
(24, 'portal', '0001_initial', '2019-03-11 02:56:03.136419'),
(25, 'portal', '0002_auto_20190314_1343', '2019-03-14 12:43:59.197424'),
(26, 'portal', '0003_fairscore', '2019-03-14 13:03:52.113811'),
(27, 'portal', '0004_auto_20190314_1410', '2019-03-14 13:10:24.205440'),
(28, 'portal', '0005_fairscore_reusability', '2019-03-14 13:12:39.413828'),
(29, 'portal', '0006_auto_20190321_0036', '2019-03-20 23:36:11.565265'),
(30, 'portal', '0007_reusability_ontused', '2019-03-20 23:50:56.008343'),
(31, 'portal', '0008_pipeline_pipelinetools', '2019-03-24 20:46:01.089845'),
(32, 'portal', '0009_auto_20190324_2323', '2019-03-24 22:23:36.062456'),
(33, 'portal', '0010_auto_20190324_2326', '2019-03-24 22:26:39.642662'),
(34, 'portal', '0011_auto_20190327_1553', '2019-03-27 14:53:10.885771'),
(35, 'portal', '0012_auto_20190327_1705', '2019-03-27 16:05:13.890807'),
(36, 'portal', '0013_tool_privatedesc', '2019-03-27 16:06:33.384041'),
(37, 'portal', '0014_remove_pipelinetools_branchstart', '2019-03-29 13:51:42.842667'),
(38, 'portal', '0015_auto_20190509_1701', '2019-05-09 15:01:40.522585');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('5v9b7d0p885yrbt7qon1ypap391bpdpp', 'OTZmMjc3MThiZjhjODRlNWUzMzdjNGJhMjJiY2RmMzdjOGZkOTU0YTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODdkZmJjNTM3NjNiODZlNDAzMDI2NDFlMmZhY2MyZTA1YjM2YTRjNCIsIl9zZXNzaW9uX2V4cGlyeSI6MH0=', '2019-05-24 13:54:03.670396'),
('6nwqbzatkiwo887pfj3qtr4w178uullz', 'OTZmMjc3MThiZjhjODRlNWUzMzdjNGJhMjJiY2RmMzdjOGZkOTU0YTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODdkZmJjNTM3NjNiODZlNDAzMDI2NDFlMmZhY2MyZTA1YjM2YTRjNCIsIl9zZXNzaW9uX2V4cGlyeSI6MH0=', '2019-04-13 14:15:56.885781'),
('7em0xcdmmdk454hlly016i831bb985ff', 'OTZmMjc3MThiZjhjODRlNWUzMzdjNGJhMjJiY2RmMzdjOGZkOTU0YTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODdkZmJjNTM3NjNiODZlNDAzMDI2NDFlMmZhY2MyZTA1YjM2YTRjNCIsIl9zZXNzaW9uX2V4cGlyeSI6MH0=', '2019-04-10 15:54:46.402672'),
('90facr0567diwgdssfc72w28v2eehw78', 'MDEzMTVmZTk2OTI1ZDczZWM0ODllNDNhOTgwNWZmNDQ0MzcxMjhmZDp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODdkZmJjNTM3NjNiODZlNDAzMDI2NDFlMmZhY2MyZTA1YjM2YTRjNCIsIl9zZXNzaW9uX2V4cGlyeSI6MTIwOTYwMH0=', '2019-06-04 11:39:17.449932'),
('bu03hbcwjhpnpzkvrf0r7hwr8pxce2oe', 'OTZmMjc3MThiZjhjODRlNWUzMzdjNGJhMjJiY2RmMzdjOGZkOTU0YTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODdkZmJjNTM3NjNiODZlNDAzMDI2NDFlMmZhY2MyZTA1YjM2YTRjNCIsIl9zZXNzaW9uX2V4cGlyeSI6MH0=', '2019-04-15 10:42:51.494940'),
('ifnt53r270dgvnugao8wsitid3mvqjmy', 'Mzc3YTA5ZjUyNzQ4ODdhMjA2ZTJmZWI4YzExNTQxY2UwZDhiYTY2OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0OGZjZDgyMzRkMmRmZDRlZmE4MGFjZDQ3MGVkMTcyMGM4OTllM2RmIn0=', '2019-03-24 18:39:35.441632'),
('sonos23r9k0i04n078nypa5teqizal9d', 'OTZmMjc3MThiZjhjODRlNWUzMzdjNGJhMjJiY2RmMzdjOGZkOTU0YTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODdkZmJjNTM3NjNiODZlNDAzMDI2NDFlMmZhY2MyZTA1YjM2YTRjNCIsIl9zZXNzaW9uX2V4cGlyeSI6MH0=', '2019-04-12 13:46:30.135939'),
('x4w5o79zwrimbmik9bwwnqb6so768bag', 'OTZmMjc3MThiZjhjODRlNWUzMzdjNGJhMjJiY2RmMzdjOGZkOTU0YTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODdkZmJjNTM3NjNiODZlNDAzMDI2NDFlMmZhY2MyZTA1YjM2YTRjNCIsIl9zZXNzaW9uX2V4cGlyeSI6MH0=', '2019-04-07 21:29:54.976638');

-- --------------------------------------------------------

--
-- Table structure for table `django_site`
--

CREATE TABLE `django_site` (
  `id` int(11) NOT NULL,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

-- --------------------------------------------------------

--
-- Table structure for table `portal_accessibility`
--

CREATE TABLE `portal_accessibility` (
  `id` int(11) NOT NULL,
  `api` double NOT NULL,
  `tool_id` int(11) NOT NULL,
  `commandLine` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `portal_accessibility`
--

INSERT INTO `portal_accessibility` (`id`, `api`, `tool_id`, `commandLine`) VALUES
(1, 5, 1, 5),
(2, 0, 2, 5),
(3, 5, 3, 5),
(4, 5, 5, 5),
(5, 5, 6, 0),
(6, 0, 7, 0),
(7, 5, 8, 5),
(8, 0, 9, 5),
(9, 0, 10, 5),
(10, 0, 12, 0),
(11, 0, 13, 5),
(12, 0, 14, 5),
(13, 0, 15, 0),
(14, 0, 16, 5),
(15, 0, 17, 5),
(16, 5, 18, 5),
(17, 0, 19, 5),
(18, 0, 20, 5),
(19, 0, 21, 5),
(20, 0, 22, 5),
(21, 5, 23, 5),
(22, 5, 24, 5);

-- --------------------------------------------------------

--
-- Table structure for table `portal_fairscore`
--

CREATE TABLE `portal_fairscore` (
  `id` int(11) NOT NULL,
  `findability` double NOT NULL,
  `accessibility` double NOT NULL,
  `interoperability` double NOT NULL,
  `tool_id` int(11) NOT NULL,
  `reusability` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `portal_fairscore`
--

INSERT INTO `portal_fairscore` (`id`, `findability`, `accessibility`, `interoperability`, `tool_id`, `reusability`) VALUES
(1, 90, 100, 50, 1, 50),
(2, 100, 50, 100, 2, 100),
(3, 90, 100, 100, 3, 100),
(4, 0, 0, 0, 4, 0),
(5, 100, 100, 50, 5, 75),
(6, 100, 100, 50, 6, 100),
(7, 100, 0, 50, 7, 75),
(8, 100, 100, 100, 8, 75),
(9, 100, 50, 100, 9, 75),
(10, 90, 50, 0, 10, 50),
(11, 90, 50, 83.33, 11, 100),
(12, 90, 0, 0, 12, 25),
(13, 100, 50, 66.67, 13, 87.5),
(14, 100, 50, 50, 14, 87.5),
(15, 90, 0, 0, 15, 50),
(16, 100, 50, 66.67, 16, 87.5),
(17, 100, 50, 100, 17, 100),
(18, 65, 100, 33.33, 18, 12.5),
(19, 90, 50, 100, 19, 75),
(20, 100, 50, 100, 20, 100),
(21, 100, 50, 100, 21, 100),
(22, 100, 50, 100, 22, 87.5),
(23, 100, 100, 100, 23, 100),
(24, 90, 100, 66.67, 24, 37.5);

-- --------------------------------------------------------

--
-- Table structure for table `portal_findability`
--

CREATE TABLE `portal_findability` (
  `id` int(11) NOT NULL,
  `free_down` double NOT NULL,
  `doi` double NOT NULL,
  `description` double NOT NULL,
  `versions` double NOT NULL,
  `tool_id` int(11) NOT NULL,
  `descText` longtext NOT NULL,
  `doiLink` varchar(200) NOT NULL,
  `downlink` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `portal_findability`
--

INSERT INTO `portal_findability` (`id`, `free_down`, `doi`, `description`, `versions`, `tool_id`, `descText`, `doiLink`, `downlink`) VALUES
(1, 8, 5, 5, 0, 1, 'The Basic Local Alignment Search Tool (BLAST) finds regions of local similarity between sequences. The program compares nucleotide or protein sequences to sequence databases and calculates the statistical significance of matches. BLAST can be used to infer functional and evolutionary relationships between sequences as well as help identify members of gene families. ', 'https://doi.org/10.1002/cpet.8 ', 'https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download'),
(2, 8, 5, 5, 2, 2, 'Compares a protein sequence to another protein sequence or to a protein database, or a DNA sequence to another DNA sequence or a DNA library. ', 'https://doi.org/10.1073/pnas.85.8.2444', 'https://fasta.bioch.virginia.edu/fasta_www2/fasta_down.shtml'),
(3, 8, 5, 5, 0, 3, 'Clustal Omega is the latest addition to the Clustal family. It offers a significant increase in scalability over previous versions, allowing hundreds of thousands of sequences to be aligned in only a few hours. It will also make use of multiple processors, where present. In addition, the quality of alignments is superior to previous versions, as measured by a range of popular benchmarks. ', 'https://doi.org/10.1002/pro.3290', 'http://www.clustal.org/omega/clustal-omega-1.2.4.tar.gz'),
(4, 8, 5, 5, 2, 5, 'Hammock is a software tool to cluster peptide sequences on the basis of shared sequence motifs. It can process very large datasets of up to a million unique sequences. The main motivation are data from phage display experiments sequenced using NGS, but no limits are put on the origin of input data - Hammock will cluster any set of peptide sequences.', 'https://dx.doi.org/10.1093/bioinformatics/btv522', 'https://github.com/krejciadam/hammock'),
(5, 8, 5, 5, 2, 6, 'PyroHMMvar deploys a hidden Markov model to model homopolymer sequencing errors, and then re-align short reads against HMM. PyroHMMvar then merges the hidden state paths to a weighted alignment graph, which combined with a Bayesian method to improve the accuracy of short indels/SNPs calling.', 'https://doi.org/10.1093/nar/gkt372', 'https://github.com/homopolymer/PyroTools/'),
(6, 8, 5, 5, 2, 7, 'CytoSPADE is a high-performance implementation of an interface for the Spanning-tree Progression Analysis of Density-normalized Events algorithm for tree-based analysis and visualization of this high-dimensional cytometry data.', '10.1093/bioinformatics/bts425', 'https://github.com/nolanlab/cytospade'),
(7, 8, 5, 5, 2, 8, 'A free, user-friendly tool implementing an efficient moment expansion approximation with parametric closures that integrates well with the IPython interactive environment. This package enables the analysis of complex stochastic systems without any constraints on the number of species and moments studied and the type of rate laws in the system. In addition to the approximation method this package provides numerous tools to help non-expert users in stochastic analysis.', '10.1093/bioinformatics/btw229', 'https://github.com/theosysbio/means'),
(8, 8, 5, 5, 2, 9, 'A flexible toolkit for exploring datasets generated by nanopore sequencing devices from MinION for the purposes of quality control and downstream analysis. Poretools operates directly on the native FAST5 (a variant of the HDF5 standard) file format produced by ONT and provides a wealth of format conversion utilities and data exploration and visualization tools.', 'https://doi.org/10.1093/bioinformatics/btu555', 'https://github.com/arq5x/poretools'),
(9, 8, 5, 5, 0, 10, 'For the analysis of miRNAs targeting genes and pathways several tools exist. We previously presented a dictionary on single miRNAs and their putative target pathways. Since that time, the number of miRNAs has tripled and the knowledge on miRNAs and targets, especially experimentally validated ones, has grown substantially. This, along with changes in pathway resources such as KEGG, leads to an improved understanding of miRNAs targeting pathways.\r\n\r\nHere, we introduce the miRNA Pathway Dictionary Database (miRPathDB), freely accessible at https://mpd.bioinf.uni-sb.de/. With the database we aim to augment available target pathway web-servers by providing researches easy access to the information which pathways are regulated by a miRNA, which miRNAs target a pathway and how specific the regulations are. The database contains a large number of miRNAs (2,599 human miRNAs), different miRNA target sets (14,773 experimentally validated target genes as well as 19281 predicted targets genes) and a broad selection of functional biochemical categories (280 KEGG-, 296 WikiPathways-, 310 BioCarta-, 617 SMPDB-, 221 PID-, 1,300 Reactome pathways, 6,169 biological processes, 1,550 molecular functions, and 758 cellular components from Gene Ontology, and 806 cytogenetic bands, totaling 12,875 categories). In addition to H. sapiens, also M. musculus data are stored and can be compared to human target pathways. ', 'https://doi.org/10.1093/nar/gkw926', 'https://mpd.bioinf.uni-sb.de/download.html'),
(10, 8, 5, 5, 0, 11, 'A package used for efficient unraveling of the inherent dynamic properties of pathways. MicroRNA-mediated subpathway topologies are extracted and evaluated by exploiting the temporal transition and the fold change activity of the linked genes/microRNAs.', '10.18129/B9.bioc.CHRONOS', 'https://bioconductor.org/packages/release/bioc/html/CHRONOS.html'),
(11, 8, 5, 5, 0, 12, 'PhosphoPICK is a method for predicting kinase substrates using an integrated system of cellular context and protein sequence information, and is currently able to make predictions for 107 human kinases, 24 mouse kinases and 26 yeast kinases.', 'https://doi.org/10.1093/bioinformatics/btx072', 'http://bioinf.scmb.uq.edu.au/phosphopick/download'),
(12, 8, 5, 5, 2, 13, 'Breakpointer is a fast tool for locating sequence breakpoints from the alignment of single end reads (SE) produced by next generation sequencing (NGS). It adopts a heuristic method in searching for local mapping signatures created by insertion/deletions (indels) or more complex structural variants(SVs). With current NGS single-end sequencing data, the output regions by Breakpoint mainly contain the approximate breakpoints of indels and a limited number of large SVs. Notably, Breakpointer can uncover breakpoints of insertions which are longer than the read length. Breakpointer also can find breakpoints of many variants located in repetitive regions. The regions can be used not only as a extra support for SV predictions by other tools (such as by split-read method), but also can serve as a database for searching variants which might be missed by other tools. Breakpointer is a command line tool that runs under linux system.', 'https://doi.org/10.1093/bioinformatics/bts064', 'https://github.com/ruping/Breakpointer'),
(13, 8, 5, 5, 2, 14, 'HMMER is used for searching sequence databases for sequence homologs, and for making sequence alignments. It implements methods using probabilistic models called profile hidden Markov models (profile HMMs). ', 'https://doi.org/10.1093/nar/gkr367', 'http://hmmer.org/download.html'),
(14, 8, 5, 5, 0, 15, 'A combined transmembrane topology and signal peptide predictor\r\n', 'https://doi.org/10.1016/j.jmb.2004.03.016', 'http://phobius.sbc.su.se/data.html'),
(15, 8, 5, 5, 2, 16, 'InterPro is a database which integrates together predictive information about proteins\' function from a number of partner resources, giving an overview of the families that a protein belongs to and the domains and sites it contains.\r\n\r\nUsers who have novel nucleotide or protein sequences that they wish to functionally characterise can use the software package InterProScan to run the scanning algorithms from the InterPro database in an integrated way. Sequences are submitted in FASTA format. Matches are then calculated against all of the required member database\'s signatures and the results are then output in a variety of formats.', 'https://doi.org/10.1093/bioinformatics/btu031', 'https://github.com/ebi-pf-team/interproscan'),
(16, 8, 5, 5, 2, 17, 'MUSCLE is one of the best-performing multiple alignment programs according to published benchmark tests, with accuracy and speed that are consistently better than CLUSTALW. MUSCLE can align hundreds of sequences in seconds. Most users learn everything they need to know about MUSCLE in a few minutes—only a handful of command-line options are needed to perform common alignment tasks.', '10.1093/nar/gkh340', 'https://www.drive5.com/muscle/downloads.htm'),
(17, 8, 0, 5, 0, 18, 'Sequencher empowers the benchtop scientist by bringing the latest peer-reviewed NGS algorithms out of the command line and into an intuitive point and click interface.  Whether performing reference-guided alignments, de novo assembly, variant calling, or SNP analyses, Sequencher has the tools you need to get results.  Sequencher has integrated the comprehensive Cufflinks suite for in-depth transcript analysis and differential gene expression of your RNA-Seq data.  Sequencher can easily generate unique visualizations of your RNA-Seq data with custom plots and charts giving you publication-ready graphics in seconds.', 'No DOI found.', 'http://www.genecodes.com/free-download'),
(18, 8, 5, 5, 0, 19, 'MAFFT is a multiple sequence alignment program for unix-like operating systems.  It offers a range of multiple alignment methods, L-INS-i (accurate; for alignment of <?200 sequences), FFT-NS-2 (fast; for alignment of <?30,000 sequences), etc. ', 'https://doi.org/10.1093/nar/gkf436', 'https://mafft.cbrc.jp/alignment/software/'),
(19, 8, 5, 5, 2, 20, 'jModelTest is a tool to carry out statistical selection of best-fit models of nucleotide substitution. It implements five different model selection strategies: hierarchical and dynamical likelihood ratio tests (hLRT and dLRT), Akaike and Bayesian information criteria (AIC and BIC), and a decision theory method (DT). It also provides estimates of model selection uncertainty, parameter importances and model-averaged parameter estimates, including model-averaged tree topologies. jModelTest 2 includes High Performance Computing (HPC) capabilities and additional features like new strategies for tree optimization, model-averaged phylogenetic trees (both topology and branch lenght), heuristic filtering and automatic logging of user activity.', '10.1038/nmeth.2109', 'https://github.com/ddarriba/jmodeltest2'),
(20, 8, 5, 5, 2, 21, 'Standard tool for Maximum-likelihood based phylogenetic inference. ', 'https://doi.org/10.1093/bioinformatics/btu033', 'https://github.com/stamatak/standard-RAxML'),
(21, 8, 5, 5, 2, 22, 'MrBayes is a program for Bayesian inference and model choice across a wide range of phylogenetic and evolutionary models. MrBayes uses Markov chain Monte Carlo (MCMC) methods to estimate the posterior distribution of model parameters.', 'https://doi.org/10.1093/bioinformatics/17.8.754', 'http://nbisweden.github.io/MrBayes/download.html'),
(22, 8, 5, 5, 2, 23, 'BEAST is a cross-platform program for Bayesian analysis of molecular sequences using MCMC. It is entirely orientated towards rooted, time-measured phylogenies inferred using strict or relaxed molecular clock models. It can be used as a method of reconstructing phylogenies but is also a framework for testing evolutionary hypotheses without conditioning on a single tree topology. BEAST uses MCMC to average over tree space, so that each tree is weighted proportional to its posterior probability.', 'https://doi.org/10.1093/ve/vey016', 'http://beast.community/#downloading-beast'),
(23, 8, 5, 5, 0, 24, 'DnaSP, DNA Sequence Polymorphism, is a software package for the analysis of DNA polymorphisms using data from a single locus (a multiple sequence aligned -MSA data), or from several loci (a Multiple-MSA data, such as formats generated by some assembler RAD-seq software). DnaSP can estimate several measures of DNA sequence variation within and between populations in noncoding, synonymous or nonsynonymous sites, or in various sorts of codon positions), as well as linkage disequilibrium, recombination, gene flow and gene conversion parameters. ', '10.1093/molbev/msx248', 'http://www.ub.edu/dnasp/downloadTv6.html');

-- --------------------------------------------------------

--
-- Table structure for table `portal_interoperability`
--

CREATE TABLE `portal_interoperability` (
  `id` int(11) NOT NULL,
  `compatibility` double NOT NULL,
  `tool_id` int(11) NOT NULL,
  `macComp` tinyint(1) NOT NULL,
  `unixComp` tinyint(1) NOT NULL,
  `winComp` tinyint(1) NOT NULL,
  `sourceCode` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `portal_interoperability`
--

INSERT INTO `portal_interoperability` (`id`, `compatibility`, `tool_id`, `macComp`, `unixComp`, `winComp`, `sourceCode`) VALUES
(1, 0, 1, 0, 0, 0, 5),
(2, 5, 2, 1, 1, 1, 5),
(3, 5, 3, 1, 1, 1, 5),
(4, 0, 5, 0, 0, 0, 5),
(5, 0, 6, 0, 0, 0, 5),
(6, 0, 7, 0, 0, 0, 5),
(7, 5, 8, 1, 1, 1, 5),
(8, 0, 10, 0, 0, 0, 0),
(9, 3.33, 11, 1, 0, 1, 5),
(10, 0, 12, 0, 0, 0, 0),
(11, 1.67, 13, 0, 1, 0, 5),
(12, 0, 14, 0, 0, 0, 5),
(13, 0, 15, 0, 0, 0, 0),
(14, 1.67, 16, 0, 1, 0, 5),
(15, 5, 17, 1, 1, 1, 5),
(16, 3.33, 18, 1, 0, 1, 0),
(17, 5, 19, 1, 1, 1, 5),
(18, 5, 20, 1, 1, 1, 5),
(19, 5, 21, 1, 1, 1, 5),
(20, 5, 22, 1, 1, 1, 5),
(21, 5, 23, 1, 1, 1, 5),
(22, 1.67, 24, 0, 0, 1, 5),
(23, 5, 9, 1, 1, 1, 5);

-- --------------------------------------------------------

--
-- Table structure for table `portal_pipeline`
--

CREATE TABLE `portal_pipeline` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `owner_id` int(11) DEFAULT NULL,
  `accessibility` double DEFAULT NULL,
  `findability` double DEFAULT NULL,
  `interoperability` double DEFAULT NULL,
  `reusability` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `portal_pipeline`
--

INSERT INTO `portal_pipeline` (`id`, `name`, `owner_id`, `accessibility`, `findability`, `interoperability`, `reusability`) VALUES
(5, 'Conflicting Evolutionary Patterns Due to Mitochondrial Introgression and Multilocus Phylogeography of the Patagonian Freshwater Crab Aegla neuquensis', 2, 68.75, 93.12, 87.5, 76.56);

-- --------------------------------------------------------

--
-- Table structure for table `portal_pipelinetools`
--

CREATE TABLE `portal_pipelinetools` (
  `id` int(11) NOT NULL,
  `pipeline_id` int(11) NOT NULL,
  `tool_id` int(11) NOT NULL,
  `branch` int(11) NOT NULL,
  `position` int(11) DEFAULT NULL,
  `toolAfter_id` int(11) DEFAULT NULL,
  `toolBefore_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `portal_pipelinetools`
--

INSERT INTO `portal_pipelinetools` (`id`, `pipeline_id`, `tool_id`, `branch`, `position`, `toolAfter_id`, `toolBefore_id`) VALUES
(16, 5, 17, 0, NULL, NULL, NULL),
(17, 5, 18, 0, NULL, NULL, NULL),
(18, 5, 19, 0, NULL, NULL, NULL),
(19, 5, 20, 0, NULL, NULL, NULL),
(20, 5, 21, 0, NULL, NULL, NULL),
(21, 5, 22, 0, NULL, NULL, NULL),
(22, 5, 23, 0, NULL, NULL, NULL),
(23, 5, 24, 0, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `portal_reusability`
--

CREATE TABLE `portal_reusability` (
  `id` int(11) NOT NULL,
  `public_repo` double NOT NULL,
  `ontology` double NOT NULL,
  `documentation` double NOT NULL,
  `contact` double NOT NULL,
  `citation` double NOT NULL,
  `tool_id` int(11) NOT NULL,
  `repositoryLink` varchar(200) NOT NULL,
  `ontUsed` varchar(200) NOT NULL,
  `usesOnt` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `portal_reusability`
--

INSERT INTO `portal_reusability` (`id`, `public_repo`, `ontology`, `documentation`, `contact`, `citation`, `tool_id`, `repositoryLink`, `ontUsed`, `usesOnt`) VALUES
(1, 0, 0, 5, 2.5, 2.5, 1, 'No public repository found.', '', 0),
(2, 10, 0, 5, 2.5, 2.5, 2, 'https://github.com/wrpearson/fasta36', '', 0),
(3, 10, 0, 5, 2.5, 2.5, 3, 'https://github.com/etetoolkit/ext_apps/tree/master/src/clustal-omega-1.2.1', '', 0),
(4, 10, 0, 5, 0, 0, 5, 'https://github.com/krejciadam/hammock', '', 0),
(5, 10, 0, 5, 2.5, 2.5, 6, 'https://github.com/homopolymer/PyroTools/', '', 0),
(6, 10, 0, 5, 0, 0, 7, 'https://github.com/nolanlab/cytospade', '', 0),
(7, 10, 0, 5, 0, 0, 8, 'https://github.com/theosysbio/means', '', 0),
(8, 10, 0, 5, 0, 0, 9, 'https://github.com/arq5x/poretools', '', 0),
(9, 0, 0, 5, 2.5, 2.5, 10, 'No public repository found.', '', 0),
(10, 10, 0, 5, 2.5, 2.5, 11, 'https://bioconductor.org/packages/release/bioc/html/CHRONOS.html', '', 0),
(11, 0, 0, 0, 2.5, 2.5, 12, 'No repository found.', '', 0),
(12, 10, 0, 5, 2.5, 0, 13, 'https://github.com/ruping/Breakpointer', '', 0),
(13, 10, 0, 5, 2.5, 0, 14, 'https://github.com/EddyRivasLab/hmmer', '', 0),
(14, 0, 0, 5, 2.5, 2.5, 15, 'No repository found.', '', 0),
(15, 10, 0, 5, 2.5, 0, 16, 'https://github.com/ebi-pf-team/interproscan', '', 0),
(16, 10, 0, 5, 2.5, 2.5, 17, 'https://github.com/cran/muscle', '', 0),
(17, 0, 0, 0, 2.5, 0, 18, 'No repository found.', '', 0),
(18, 10, 0, 0, 2.5, 2.5, 19, 'https://github.com/nesi/applications', '', 0),
(19, 10, 0, 5, 2.5, 2.5, 20, 'https://github.com/ddarriba/jmodeltest2', '', 0),
(20, 10, 0, 5, 2.5, 2.5, 21, 'https://github.com/stamatak/standard-RAxML', '', 0),
(21, 10, 0, 5, 0, 2.5, 22, 'https://github.com/NBISweden/MrBayes', '', 0),
(22, 10, 0, 5, 2.5, 2.5, 23, 'https://github.com/beast-dev/beast-mcmc', '', 0),
(23, 0, 0, 5, 2.5, 0, 24, 'No repository found.', '', 0);

-- --------------------------------------------------------

--
-- Table structure for table `portal_tool`
--

CREATE TABLE `portal_tool` (
  `id` int(11) NOT NULL,
  `tool_name` varchar(200) NOT NULL,
  `isPrivate` tinyint(1) NOT NULL,
  `owner_id` int(11) DEFAULT NULL,
  `privateDesc` longtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `portal_tool`
--

INSERT INTO `portal_tool` (`id`, `tool_name`, `isPrivate`, `owner_id`, `privateDesc`) VALUES
(1, 'BLAST', 0, NULL, NULL),
(2, 'FASTA', 0, NULL, NULL),
(3, 'Clustal Omega', 0, NULL, NULL),
(4, 'Private Tool 1', 1, 2, 'This is a private tool added by the user.'),
(5, 'HAMMOCK', 0, NULL, NULL),
(6, 'PyroHMMvar', 0, NULL, NULL),
(7, 'CytoSPADE', 0, NULL, NULL),
(8, 'MEANS', 0, NULL, NULL),
(9, 'poretools', 0, NULL, NULL),
(10, 'miRPathDB', 0, NULL, NULL),
(11, 'CHRONOS', 0, NULL, NULL),
(12, 'PhosphoPICK', 0, NULL, NULL),
(13, 'Breakpointer', 0, NULL, NULL),
(14, 'HMMER', 0, NULL, NULL),
(15, 'Phobius', 0, NULL, NULL),
(16, 'InterProScan', 0, NULL, NULL),
(17, 'MUSCLE', 0, NULL, NULL),
(18, 'Sequencher', 0, NULL, NULL),
(19, 'MAFFT', 0, NULL, NULL),
(20, 'jModelTest', 0, NULL, NULL),
(21, 'RAxML', 0, NULL, NULL),
(22, 'MrBayes', 0, NULL, NULL),
(23, 'BEAST', 0, NULL, NULL),
(24, 'DnaSP', 0, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `socialaccount_socialaccount`
--

CREATE TABLE `socialaccount_socialaccount` (
  `id` int(11) NOT NULL,
  `provider` varchar(30) NOT NULL,
  `uid` varchar(191) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `extra_data` longtext NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `socialaccount_socialapp`
--

CREATE TABLE `socialaccount_socialapp` (
  `id` int(11) NOT NULL,
  `provider` varchar(30) NOT NULL,
  `name` varchar(40) NOT NULL,
  `client_id` varchar(191) NOT NULL,
  `secret` varchar(191) NOT NULL,
  `key` varchar(191) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `socialaccount_socialapp_sites`
--

CREATE TABLE `socialaccount_socialapp_sites` (
  `id` int(11) NOT NULL,
  `socialapp_id` int(11) NOT NULL,
  `site_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `socialaccount_socialtoken`
--

CREATE TABLE `socialaccount_socialtoken` (
  `id` int(11) NOT NULL,
  `token` longtext NOT NULL,
  `token_secret` longtext NOT NULL,
  `expires_at` datetime(6) DEFAULT NULL,
  `account_id` int(11) NOT NULL,
  `app_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `users_portaluser`
--

CREATE TABLE `users_portaluser` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users_portaluser`
--

INSERT INTO `users_portaluser` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(2, 'pbkdf2_sha256$120000$dwVoMOqegZsZ$HrkMOiw8Be2CJ2jg+pNQdSpHEaGQ+X+/HglU4k1TAwc=', '2019-05-21 11:39:17.416023', 1, 'User', '', '', 'bioinformaticsresourceportal@gmail.com', 0, 1, '2019-03-24 21:12:53.650715');

-- --------------------------------------------------------

--
-- Table structure for table `users_portaluser_groups`
--

CREATE TABLE `users_portaluser_groups` (
  `id` int(11) NOT NULL,
  `portaluser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `users_portaluser_user_permissions`
--

CREATE TABLE `users_portaluser_user_permissions` (
  `id` int(11) NOT NULL,
  `portaluser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account_emailaddress`
--
ALTER TABLE `account_emailaddress`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `account_emailaddress_user_id_2c513194_fk_users_portaluser_id` (`user_id`);

--
-- Indexes for table `account_emailconfirmation`
--
ALTER TABLE `account_emailconfirmation`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `key` (`key`),
  ADD KEY `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` (`email_address_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_users_portaluser_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `django_site`
--
ALTER TABLE `django_site`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`);

--
-- Indexes for table `portal_accessibility`
--
ALTER TABLE `portal_accessibility`
  ADD PRIMARY KEY (`id`),
  ADD KEY `portal_accessibility_tool_id_b809d201_fk_portal_tool_id` (`tool_id`);

--
-- Indexes for table `portal_fairscore`
--
ALTER TABLE `portal_fairscore`
  ADD PRIMARY KEY (`id`),
  ADD KEY `portal_fairscore_tool_id_37b735b8_fk_portal_tool_id` (`tool_id`);

--
-- Indexes for table `portal_findability`
--
ALTER TABLE `portal_findability`
  ADD PRIMARY KEY (`id`),
  ADD KEY `portal_findability_tool_id_3d16427e_fk_portal_tool_id` (`tool_id`);

--
-- Indexes for table `portal_interoperability`
--
ALTER TABLE `portal_interoperability`
  ADD PRIMARY KEY (`id`),
  ADD KEY `portal_interoperability_tool_id_e1b7b2a4_fk_portal_tool_id` (`tool_id`);

--
-- Indexes for table `portal_pipeline`
--
ALTER TABLE `portal_pipeline`
  ADD PRIMARY KEY (`id`),
  ADD KEY `portal_pipeline_owner_id_835053c3_fk_users_portaluser_id` (`owner_id`);

--
-- Indexes for table `portal_pipelinetools`
--
ALTER TABLE `portal_pipelinetools`
  ADD PRIMARY KEY (`id`),
  ADD KEY `portal_pipelinetools_pipeline_id_e8322466_fk_portal_pipeline_id` (`pipeline_id`),
  ADD KEY `portal_pipelinetools_tool_id_049134a4_fk_portal_tool_id` (`tool_id`),
  ADD KEY `portal_pipelinetools_toolAfter_id_a9dc7564_fk_portal_tool_id` (`toolAfter_id`),
  ADD KEY `portal_pipelinetools_toolBefore_id_8a1d4438_fk_portal_tool_id` (`toolBefore_id`);

--
-- Indexes for table `portal_reusability`
--
ALTER TABLE `portal_reusability`
  ADD PRIMARY KEY (`id`),
  ADD KEY `portal_reusability_tool_id_3726fdc0_fk_portal_tool_id` (`tool_id`);

--
-- Indexes for table `portal_tool`
--
ALTER TABLE `portal_tool`
  ADD PRIMARY KEY (`id`),
  ADD KEY `portal_tool_owner_id_1c5917cd_fk_users_portaluser_id` (`owner_id`);

--
-- Indexes for table `socialaccount_socialaccount`
--
ALTER TABLE `socialaccount_socialaccount`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `socialaccount_socialaccount_provider_uid_fc810c6e_uniq` (`provider`,`uid`),
  ADD KEY `socialaccount_social_user_id_8146e70c_fk_users_por` (`user_id`);

--
-- Indexes for table `socialaccount_socialapp`
--
ALTER TABLE `socialaccount_socialapp`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `socialaccount_socialapp_sites`
--
ALTER TABLE `socialaccount_socialapp_sites`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `socialaccount_socialapp_sites_socialapp_id_site_id_71a9a768_uniq` (`socialapp_id`,`site_id`),
  ADD KEY `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id` (`site_id`);

--
-- Indexes for table `socialaccount_socialtoken`
--
ALTER TABLE `socialaccount_socialtoken`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq` (`app_id`,`account_id`),
  ADD KEY `socialaccount_social_account_id_951f210e_fk_socialacc` (`account_id`);

--
-- Indexes for table `users_portaluser`
--
ALTER TABLE `users_portaluser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `users_portaluser_groups`
--
ALTER TABLE `users_portaluser_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_portaluser_groups_portaluser_id_group_id_51948a21_uniq` (`portaluser_id`,`group_id`),
  ADD KEY `users_portaluser_groups_group_id_ff94670e_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `users_portaluser_user_permissions`
--
ALTER TABLE `users_portaluser_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_portaluser_user_pe_portaluser_id_permission_7502d71b_uniq` (`portaluser_id`,`permission_id`),
  ADD KEY `users_portaluser_use_permission_id_2e08e205_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account_emailaddress`
--
ALTER TABLE `account_emailaddress`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `account_emailconfirmation`
--
ALTER TABLE `account_emailconfirmation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=85;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `django_site`
--
ALTER TABLE `django_site`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `portal_accessibility`
--
ALTER TABLE `portal_accessibility`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `portal_fairscore`
--
ALTER TABLE `portal_fairscore`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `portal_findability`
--
ALTER TABLE `portal_findability`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `portal_interoperability`
--
ALTER TABLE `portal_interoperability`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `portal_pipeline`
--
ALTER TABLE `portal_pipeline`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `portal_pipelinetools`
--
ALTER TABLE `portal_pipelinetools`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `portal_reusability`
--
ALTER TABLE `portal_reusability`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `portal_tool`
--
ALTER TABLE `portal_tool`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `socialaccount_socialaccount`
--
ALTER TABLE `socialaccount_socialaccount`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `socialaccount_socialapp`
--
ALTER TABLE `socialaccount_socialapp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `socialaccount_socialapp_sites`
--
ALTER TABLE `socialaccount_socialapp_sites`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `socialaccount_socialtoken`
--
ALTER TABLE `socialaccount_socialtoken`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users_portaluser`
--
ALTER TABLE `users_portaluser`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `users_portaluser_groups`
--
ALTER TABLE `users_portaluser_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users_portaluser_user_permissions`
--
ALTER TABLE `users_portaluser_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `account_emailaddress`
--
ALTER TABLE `account_emailaddress`
  ADD CONSTRAINT `account_emailaddress_user_id_2c513194_fk_users_portaluser_id` FOREIGN KEY (`user_id`) REFERENCES `users_portaluser` (`id`);

--
-- Constraints for table `account_emailconfirmation`
--
ALTER TABLE `account_emailconfirmation`
  ADD CONSTRAINT `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` FOREIGN KEY (`email_address_id`) REFERENCES `account_emailaddress` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_portaluser_id` FOREIGN KEY (`user_id`) REFERENCES `users_portaluser` (`id`);

--
-- Constraints for table `portal_accessibility`
--
ALTER TABLE `portal_accessibility`
  ADD CONSTRAINT `portal_accessibility_tool_id_b809d201_fk_portal_tool_id` FOREIGN KEY (`tool_id`) REFERENCES `portal_tool` (`id`);

--
-- Constraints for table `portal_fairscore`
--
ALTER TABLE `portal_fairscore`
  ADD CONSTRAINT `portal_fairscore_tool_id_37b735b8_fk_portal_tool_id` FOREIGN KEY (`tool_id`) REFERENCES `portal_tool` (`id`);

--
-- Constraints for table `portal_findability`
--
ALTER TABLE `portal_findability`
  ADD CONSTRAINT `portal_findability_tool_id_3d16427e_fk_portal_tool_id` FOREIGN KEY (`tool_id`) REFERENCES `portal_tool` (`id`);

--
-- Constraints for table `portal_interoperability`
--
ALTER TABLE `portal_interoperability`
  ADD CONSTRAINT `portal_interoperability_tool_id_e1b7b2a4_fk_portal_tool_id` FOREIGN KEY (`tool_id`) REFERENCES `portal_tool` (`id`);

--
-- Constraints for table `portal_pipeline`
--
ALTER TABLE `portal_pipeline`
  ADD CONSTRAINT `portal_pipeline_owner_id_835053c3_fk_users_portaluser_id` FOREIGN KEY (`owner_id`) REFERENCES `users_portaluser` (`id`);

--
-- Constraints for table `portal_pipelinetools`
--
ALTER TABLE `portal_pipelinetools`
  ADD CONSTRAINT `portal_pipelinetools_pipeline_id_e8322466_fk_portal_pipeline_id` FOREIGN KEY (`pipeline_id`) REFERENCES `portal_pipeline` (`id`),
  ADD CONSTRAINT `portal_pipelinetools_toolAfter_id_a9dc7564_fk_portal_tool_id` FOREIGN KEY (`toolAfter_id`) REFERENCES `portal_tool` (`id`),
  ADD CONSTRAINT `portal_pipelinetools_toolBefore_id_8a1d4438_fk_portal_tool_id` FOREIGN KEY (`toolBefore_id`) REFERENCES `portal_tool` (`id`),
  ADD CONSTRAINT `portal_pipelinetools_tool_id_049134a4_fk_portal_tool_id` FOREIGN KEY (`tool_id`) REFERENCES `portal_tool` (`id`);

--
-- Constraints for table `portal_reusability`
--
ALTER TABLE `portal_reusability`
  ADD CONSTRAINT `portal_reusability_tool_id_3726fdc0_fk_portal_tool_id` FOREIGN KEY (`tool_id`) REFERENCES `portal_tool` (`id`);

--
-- Constraints for table `portal_tool`
--
ALTER TABLE `portal_tool`
  ADD CONSTRAINT `portal_tool_owner_id_1c5917cd_fk_users_portaluser_id` FOREIGN KEY (`owner_id`) REFERENCES `users_portaluser` (`id`);

--
-- Constraints for table `socialaccount_socialaccount`
--
ALTER TABLE `socialaccount_socialaccount`
  ADD CONSTRAINT `socialaccount_social_user_id_8146e70c_fk_users_por` FOREIGN KEY (`user_id`) REFERENCES `users_portaluser` (`id`);

--
-- Constraints for table `socialaccount_socialapp_sites`
--
ALTER TABLE `socialaccount_socialapp_sites`
  ADD CONSTRAINT `socialaccount_social_socialapp_id_97fb6e7d_fk_socialacc` FOREIGN KEY (`socialapp_id`) REFERENCES `socialaccount_socialapp` (`id`),
  ADD CONSTRAINT `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`);

--
-- Constraints for table `socialaccount_socialtoken`
--
ALTER TABLE `socialaccount_socialtoken`
  ADD CONSTRAINT `socialaccount_social_account_id_951f210e_fk_socialacc` FOREIGN KEY (`account_id`) REFERENCES `socialaccount_socialaccount` (`id`),
  ADD CONSTRAINT `socialaccount_social_app_id_636a42d7_fk_socialacc` FOREIGN KEY (`app_id`) REFERENCES `socialaccount_socialapp` (`id`);

--
-- Constraints for table `users_portaluser_groups`
--
ALTER TABLE `users_portaluser_groups`
  ADD CONSTRAINT `users_portaluser_gro_portaluser_id_5dfca044_fk_users_por` FOREIGN KEY (`portaluser_id`) REFERENCES `users_portaluser` (`id`),
  ADD CONSTRAINT `users_portaluser_groups_group_id_ff94670e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `users_portaluser_user_permissions`
--
ALTER TABLE `users_portaluser_user_permissions`
  ADD CONSTRAINT `users_portaluser_use_permission_id_2e08e205_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `users_portaluser_use_portaluser_id_fa164e2d_fk_users_por` FOREIGN KEY (`portaluser_id`) REFERENCES `users_portaluser` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
