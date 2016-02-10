-- phpMyAdmin SQL Dump
-- version 3.4.5
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 15, 2015 at 05:46 AM
-- Server version: 5.5.16
-- PHP Version: 5.3.8

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `ejection`
--

-- --------------------------------------------------------

--
-- Table structure for table `email_forms`
--

CREATE TABLE IF NOT EXISTS `email_forms` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `form_id` int(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `form_id` (`form_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

-- --------------------------------------------------------

--
-- Table structure for table `form`
--

CREATE TABLE IF NOT EXISTS `form` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `url` varchar(250) NOT NULL,
  `attributes` varchar(250) NOT NULL,
  `request_id` int(10) NOT NULL,
  `xpath` varchar(1024) NOT NULL,
  `method` varchar(5) NOT NULL,
  `action` varchar(250) NOT NULL,
  `absolute_action` varchar(250) NOT NULL,
  `params` varchar(250) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `request_id` (`request_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=45 ;

--
-- Table structure for table `params`
--

CREATE TABLE IF NOT EXISTS `params` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `element_type` varchar(20) NOT NULL,
  `type` varchar(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `value` varchar(50) NOT NULL,
  `form_id` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=123 ;

--
-- Table structure for table `requests`
--

CREATE TABLE IF NOT EXISTS `requests` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `headers` varchar(1024) NOT NULL,
  `url` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=69 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
