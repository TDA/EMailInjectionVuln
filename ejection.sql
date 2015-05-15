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

--
-- Dumping data for table `email_forms`
--

INSERT INTO `email_forms` (`id`, `form_id`) VALUES
(4, 5),
(6, 6),
(7, 7);

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
-- Dumping data for table `form`
--

INSERT INTO `form` (`id`, `url`, `attributes`, `request_id`, `xpath`, `method`, `action`, `absolute_action`, `params`) VALUES
(1, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 24, 'None', 'post', 'add_model.php', 'saipcadd_model.php', '[1, 2, 3]'),
(2, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 25, 'None', 'post', 'add_model.php', 'saipcadd_model.php', '[4, 5, 6]'),
(3, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 26, 'None', 'post', 'add_model.php', 'saipcadd_model.php', '[7, 8, 9]'),
(6, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 29, 'None', 'post', 'add_model.php', 'saipcadd_model.php', '[16, 17, 18]'),
(7, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 30, '<form action="add_model.php" data-hi="hi" method="post">\n<label for="uname">Name <br>\r\n	(please enter your name in the box below)\r\n	</br></label>\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n<label for="pass">PIN <br>\r\n	(please create a four (4) digit numeric PIN in the box below) <br>\r\n 	(please remember and don''t forget your PIN)\r\n	</br></br></label>\n<input id="pass" name="pass" pattern="d{4}" placeholder="Password" required="" type="password">\n<!--<input type="" value="nothing" name="" />-->\n<input class="button green" type="submit" value="Signup">\n</input></input></input></form>', 'post', 'add_model.php', 'saipcadd_model.php', '[19, 20, 21]'),
(8, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 31, '<form action="add_model.php" data-hi="hi" method="post">\n<label for="uname">Name <br>\r\n	(please enter your name in the box below)\r\n	</br></label>\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n<label for="pass">PIN <br>\r\n	(please create a four (4) digit numeric PIN in the box below) <br>\r\n 	(please remember and don''t forget your PIN)\r\n	</br></br></label>\n<input id="pass" name="pass" pattern="d{4}" placeholder="Password" required="" type="password">\n<!--<input type="" value="nothing" name="" />-->\n<input class="button green" type="submit" value="Signup">\n</input></input></input></form>', 'post', 'add_model.php', 'saipcadd_model.php', '[22, 23, 24]'),
(9, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 32, '<form action="add_model.php" data-hi="hi" method="post">\n<label for="uname">Name <br>\r\n	(please enter your name in the box below)\r\n	</br></label>\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n<label for="pass">PIN <br>\r\n	(please create a four (4) digit numeric PIN in the box below) <br>\r\n 	(please remember and don''t forget your PIN)\r\n	</br></br></label>\n<input id="pass" name="pass" pattern="d{4}" placeholder="Password" required="" type="password">\n<!--<input type="" value="nothing" name="" />-->\n<input class="button green" type="submit" value="Signup">\n</input></input></input></form>', 'post', 'add_model.php', 'saipcadd_model.php', '[25, 26, 27]'),
(10, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 34, '<form action="add_model.php" data-hi="hi" method="post">\n<label for="uname">Name <br>\r\n	(please enter your name in the box below)\r\n	</br></label>\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n<label for="pass">PIN <br>\r\n	(please create a four (4) digit numeric PIN in the box below) <br>\r\n 	(please remember and don''t forget your PIN)\r\n	</br></br></label>\n<input id="pass" name="pass" pattern="d{4}" placeholder="Password" required="" type="password">\n<!--<input type="" value="nothing" name="" />-->\n<input class="button green" type="submit" value="Signup">\n</input></input></input></form>', 'post', 'add_model.php', 'saipcadd_model.php', '[32, 33, 34]'),
(11, 'http://localhost/VV/vv.htm', '[{"name": "f2", "onsubmit": "do()"}]', 35, '<form action="spc.vv" name="f2" onsubmit="do()">\n<label for="uname">Name\r\n	</label>\n<input id="uname2" name="uname2" placeholder="Enter Name here" required="" type="text">\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n</input></input></form>', '', 'spc.vv', 'saipcspc.vv', '[35, 36]'),
(12, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 36, '<form action="add_model.php" data-hi="hi" method="post">\n<label for="uname">Name <br>\r\n	(please enter your name in the box below)\r\n	</br></label>\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n<label for="pass">PIN <br>\r\n	(please create a four (4) digit numeric PIN in the box below) <br>\r\n 	(please remember and don''t forget your PIN)\r\n	</br></br></label>\n<input id="pass" name="pass" pattern="d{4}" placeholder="Password" required="" type="password">\n<!--<input type="" value="nothing" name="" />-->\n<input class="button green" type="submit" value="Signup">\n</input></input></input></form>', 'post', 'add_model.php', 'saipcadd_model.php', '[40, 41, 42]'),
(13, 'http://localhost/VV/vv.htm', '[{"name": "f2", "onsubmit": "do()"}]', 37, '<form action="spc.vv" name="f2" onsubmit="do()">\n<label for="uname">Name\r\n	</label>\n<input id="uname2" name="uname2" placeholder="Enter Name here" required="" type="text">\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n</input></input></form>', '', 'spc.vv', 'saipcspc.vv', '[43, 44]'),
(14, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 38, '<form action="add_model.php" data-hi="hi" method="post">\n<label for="uname">Name <br>\r\n	(please enter your name in the box below)\r\n	</br></label>\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n<label for="pass">PIN <br>\r\n	(please create a four (4) digit numeric PIN in the box below) <br>\r\n 	(please remember and don''t forget your PIN)\r\n	</br></br></label>\n<input id="pass" name="pass" pattern="d{4}" placeholder="Password" required="" type="password">\n<!--<input type="" value="nothing" name="" />-->\n<input class="button green" type="submit" value="Signup">\n</input></input></input></form>', 'post', 'add_model.php', 'iamsaipc/add_model.php', '[45, 46, 47]'),
(15, 'http://localhost/VV/vv.htm', '[{"name": "f2", "onsubmit": "do()"}]', 39, '<form action="spc.vv" name="f2" onsubmit="do()">\n<label for="uname">Name\r\n	</label>\n<input id="uname2" name="uname2" placeholder="Enter Name here" required="" type="text">\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n</input></input></form>', '', 'spc.vv', 'iamsaipc/spc.vv', '[48, 49]'),
(16, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 40, '<form action="add_model.php" data-hi="hi" method="post">\n<label for="uname">Name <br>\r\n	(please enter your name in the box below)\r\n	</br></label>\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n<label for="pass">PIN <br>\r\n	(please create a four (4) digit numeric PIN in the box below) <br>\r\n 	(please remember and don''t forget your PIN)\r\n	</br></br></label>\n<input id="pass" name="pass" pattern="d{4}" placeholder="Password" required="" type="password">\n<!--<input type="" value="nothing" name="" />-->\n<input class="button green" type="submit" value="Signup">\n</input></input></input></form>', 'post', 'add_model.php', 'iamsaipc/add_model.php', '[50, 51, 52]'),
(17, 'http://localhost/VV/vv.htm', '[{"onsubmit": "do()", "name": "f2"}]', 41, '<form action="spc.vv" name="f2" onsubmit="do()">\n<label for="uname">Name\r\n	</label>\n<input id="uname2" name="uname2" placeholder="Enter Name here" required="" type="text">\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n</input></input></form>', '', 'spc.vv', 'iamsaipc/spc.vv', '[53, 54]'),
(18, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 42, '<form action="add_model.php" data-hi="hi" method="post">\n<label for="uname">Name <br>\r\n	(please enter your name in the box below)\r\n	</br></label>\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n<label for="pass">PIN <br>\r\n	(please create a four (4) digit numeric PIN in the box below) <br>\r\n 	(please remember and don''t forget your PIN)\r\n	</br></br></label>\n<input id="pass" name="pass" pattern="d{4}" placeholder="Password" required="" type="password">\n<!--<input type="" value="nothing" name="" />-->\n<input class="button green" type="submit" value="Signup">\n</input></input></input></form>', 'post', 'add_model.php', 'iamsaipc/add_model.php', '[55, 56, 57]'),
(19, 'http://localhost/VV/vv.htm', '[{"name": "f2", "onsubmit": "do()"}]', 43, '<form action="spc.vv" name="f2" onsubmit="do()">\n<label for="uname">Name\r\n	</label>\n<input id="uname2" name="uname2" placeholder="Enter Name here" required="" type="text">\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n</input></input></form>', 'GET', 'spc.vv', 'iamsaipc/spc.vv', '[58, 59]'),
(20, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 44, '<form action="add_model.php" data-hi="hi" method="post">\n<label for="uname">Name <br>\r\n	(please enter your name in the box below)\r\n	</br></label>\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n<label for="pass">PIN <br>\r\n	(please create a four (4) digit numeric PIN in the box below) <br>\r\n 	(please remember and don''t forget your PIN)\r\n	</br></br></label>\n<input id="pass" name="pass" pattern="d{4}" placeholder="Password" required="" type="password">\n<!--<input type="" value="nothing" name="" />-->\n<input class="button green" type="submit" value="Signup">\n</input></input></input></form>', 'post', 'add_model.php', 'iamsaipc/add_model.php', '[60, 61, 62]'),
(21, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 45, '<form action="add_model.php" data-hi="hi" method="post">\n<label for="uname">Name <br>\r\n	(please enter your name in the box below)\r\n	</br></label>\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n<label for="pass">PIN <br>\r\n	(please create a four (4) digit numeric PIN in the box below) <br>\r\n 	(please remember and don''t forget your PIN)\r\n	</br></br></label>\n<input id="pass" name="pass" pattern="d{4}" placeholder="Password" required="" type="password">\n<!--<input type="" value="nothing" name="" />-->\n<input class="button green" type="submit" value="Signup">\n</input></input></input></form>', 'post', 'add_model.php', 'iamsaipc/add_model.php', '[63, 64, 65]'),
(22, 'http://localhost/VV/vv.htm', '[{"onsubmit": "do()", "name": "f2"}]', 46, '<form name="f2" onsubmit="do()">\n<label for="uname">Name\r\n	</label>\n<input id="uname2" name="uname2" placeholder="Enter Name here" required="" type="text">\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n</input></input></form>', 'GET', 'http://localhost/VV/vv.htm', 'iamsaipc/http://localhost/VV/vv.htm', '[66, 67]'),
(23, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 47, '<form action="add_model.php" data-hi="hi" method="post">\n<label for="uname">Name <br>\r\n	(please enter your name in the box below)\r\n	</br></label>\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n<label for="pass">PIN <br>\r\n	(please create a four (4) digit numeric PIN in the box below) <br>\r\n 	(please remember and don''t forget your PIN)\r\n	</br></br></label>\n<input id="pass" name="pass" pattern="d{4}" placeholder="Password" required="" type="password">\n<!--<input type="" value="nothing" name="" />-->\n<input class="button green" type="submit" value="Signup">\n</input></input></input></form>', 'post', 'add_model.php', 'iamsaipc/add_model.php', '[68, 69, 70]'),
(24, 'http://localhost/VV/vv.htm', '[{"name": "f2", "onsubmit": "do()"}]', 48, '<form name="f2" onsubmit="do()">\n<label for="uname">Name\r\n	</label>\n<input id="uname2" name="uname2" placeholder="Enter Name here" required="" type="text">\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n</input></input></form>', 'GET', '/VV/vv.htm', 'iamsaipc//VV/vv.htm', '[71, 72]'),
(25, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 49, '<form action="add_model.php" data-hi="hi" method="post">\n<label for="uname">Name <br>\r\n	(please enter your name in the box below)\r\n	</br></label>\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n<label for="pass">PIN <br>\r\n	(please create a four (4) digit numeric PIN in the box below) <br>\r\n 	(please remember and don''t forget your PIN)\r\n	</br></br></label>\n<input id="pass" name="pass" pattern="d{4}" placeholder="Password" required="" type="password">\n<!--<input type="" value="nothing" name="" />-->\n<input class="button green" type="submit" value="Signup">\n</input></input></input></form>', 'post', 'add_model.php', 'iamsaipc/add_model.php', '[73, 74, 75]'),
(26, 'http://localhost/VV/vv.htm', '[{"name": "f2", "onsubmit": "do()"}]', 50, '<form name="f2" onsubmit="do()">\n<label for="uname">Name\r\n	</label>\n<input id="uname2" name="uname2" placeholder="Enter Name here" required="" type="text">\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n</input></input></form>', 'GET', '', 'iamsaipc/', '[76, 77]'),
(27, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 51, '<form action="add_model.php" data-hi="hi" method="post">\n<label for="uname">Name <br>\r\n	(please enter your name in the box below)\r\n	</br></label>\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n<label for="pass">PIN <br>\r\n	(please create a four (4) digit numeric PIN in the box below) <br>\r\n 	(please remember and don''t forget your PIN)\r\n	</br></br></label>\n<input id="pass" name="pass" pattern="d{4}" placeholder="Password" required="" type="password">\n<!--<input type="" value="nothing" name="" />-->\n<input class="button green" type="submit" value="Signup">\n</input></input></input></form>', 'post', 'add_model.php', 'iamsaipc/add_model.php', '[78, 79, 80]'),
(28, 'http://localhost/VV/vv.htm', '[{"name": "f2", "onsubmit": "do()"}]', 52, '<form name="f2" onsubmit="do()">\n<label for="uname">Name\r\n	</label>\n<input id="uname2" name="uname2" placeholder="Enter Name here" required="" type="text">\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n</input></input></form>', 'GET', '', 'iamsaipc/', '[81, 82]'),
(29, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 53, '<form action="add_model.php" data-hi="hi" method="post">\n<label for="uname">Name <br>\r\n	(please enter your name in the box below)\r\n	</br></label>\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n<label for="pass">PIN <br>\r\n	(please create a four (4) digit numeric PIN in the box below) <br>\r\n 	(please remember and don''t forget your PIN)\r\n	</br></br></label>\n<input id="pass" name="pass" pattern="d{4}" placeholder="Password" required="" type="password">\n<!--<input type="" value="nothing" name="" />-->\n<input class="button green" type="submit" value="Signup">\n</input></input></input></form>', 'post', 'add_model.php', 'iamsaipc/add_model.php', '[83, 84, 85]'),
(30, 'http://localhost/VV/vv.htm', '[{"onsubmit": "do()", "name": "f2"}]', 54, '<form name="f2" onsubmit="do()">\n<label for="uname">Name\r\n	</label>\n<input id="uname2" name="uname2" placeholder="Enter Name here" required="" type="text">\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="email">\n</input></input></form>', 'GET', '', 'iamsaipc/', '[86, 87]'),
(31, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 55, '<form action="add_model.php" data-hi="hi" method="post">\n<label for="uname">Name <br>\r\n	(please enter your name in the box below)\r\n	</br></label>\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n<label for="pass">PIN <br>\r\n	(please create a four (4) digit numeric PIN in the box below) <br>\r\n 	(please remember and don''t forget your PIN)\r\n	</br></br></label>\n<input id="pass" name="pass" pattern="d{4}" placeholder="Password" required="" type="password">\n<!--<input type="" value="nothing" name="" />-->\n<input class="button green" type="submit" value="Signup">\n</input></input></input></form>', 'post', 'add_model.php', 'iamsaipc/add_model.php', '[88, 89, 90]'),
(32, 'http://localhost/VV/vv.htm', '[{"onsubmit": "do()", "name": "f2"}]', 56, '<form name="f2" onsubmit="do()">\n<label for="uname">Name\r\n	</label>\n<input id="uname2" name="uname2" placeholder="Enter Name here" required="" type="text">\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="email">\n</input></input></form>', 'GET', '', 'iamsaipc/', '[91, 92]'),
(33, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 57, '<form action="add_model.php" data-hi="hi" method="post">\n<label for="uname">Name <br>\r\n	(please enter your name in the box below)\r\n	</br></label>\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n<label for="pass">PIN <br>\r\n	(please create a four (4) digit numeric PIN in the box below) <br>\r\n 	(please remember and don''t forget your PIN)\r\n	</br></br></label>\n<input id="pass" name="pass" pattern="d{4}" placeholder="Password" required="" type="password">\n<!--<input type="" value="nothing" name="" />-->\n<input class="button green" type="submit" value="Signup">\n</input></input></input></form>', 'post', 'add_model.php', 'iamsaipc/add_model.php', '[93, 94, 95]'),
(34, 'http://localhost/VV/vv.htm', '[{"onsubmit": "do()", "name": "f2"}]', 58, '<form name="f2" onsubmit="do()">\n<label for="uname">Name\r\n	</label>\n<input id="uname2" name="uname2" placeholder="Enter Name here" required="" type="text">\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="email">\n</input></input></form>', 'GET', '', 'iamsaipc/', '[96, 97]'),
(35, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 59, '<form action="add_model.php" data-hi="hi" method="post">\n<label for="uname">Name <br>\r\n	(please enter your name in the box below)\r\n	</br></label>\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n<label for="pass">PIN <br>\r\n	(please create a four (4) digit numeric PIN in the box below) <br>\r\n 	(please remember and don''t forget your PIN)\r\n	</br></br></label>\n<input id="pass" name="pass" pattern="d{4}" placeholder="Password" required="" type="password">\n<!--<input type="" value="nothing" name="" />-->\n<input class="button green" type="submit" value="Signup">\n</input></input></input></form>', 'post', 'add_model.php', 'iamsaipc/add_model.php', '[98, 99, 100]'),
(36, 'http://localhost/VV/vv.htm', '[{"onsubmit": "do()", "name": "f2"}]', 60, '<form name="f2" onsubmit="do()">\n<label for="uname">Name\r\n	</label>\n<input id="uname2" name="uname2" placeholder="Enter Name here" required="" type="text">\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="email">\n</input></input></form>', 'GET', '', 'iamsaipc/', '[101, 102]'),
(37, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 61, '<form action="add_model.php" data-hi="hi" method="post">\n<label for="uname">Name <br>\r\n	(please enter your name in the box below)\r\n	</br></label>\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n<label for="pass">PIN <br>\r\n	(please create a four (4) digit numeric PIN in the box below) <br>\r\n 	(please remember and don''t forget your PIN)\r\n	</br></br></label>\n<input id="pass" name="pass" pattern="d{4}" placeholder="Password" required="" type="password">\n<!--<input type="" value="nothing" name="" />-->\n<input class="button green" type="submit" value="Signup">\n</input></input></input></form>', 'post', 'add_model.php', 'iamsaipc/add_model.php', '[103, 104, 105]'),
(38, 'http://localhost/VV/vv.htm', '[{"onsubmit": "do()", "name": "f2"}]', 62, '<form name="f2" onsubmit="do()">\n<label for="uname">Name\r\n	</label>\n<input id="uname2" name="uname2" placeholder="Enter Name here" required="" type="text">\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="email">\n</input></input></form>', 'GET', '', 'iamsaipc/', '[106, 107]'),
(39, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 63, '<form action="add_model.php" data-hi="hi" method="post">\n<label for="uname">Name <br>\r\n	(please enter your name in the box below)\r\n	</br></label>\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n<label for="pass">PIN <br>\r\n	(please create a four (4) digit numeric PIN in the box below) <br>\r\n 	(please remember and don''t forget your PIN)\r\n	</br></br></label>\n<input id="pass" name="pass" pattern="d{4}" placeholder="Password" required="" type="password">\n<!--<input type="" value="nothing" name="" />-->\n<input class="button green" type="submit" value="Signup">\n</input></input></input></form>', 'post', 'add_model.php', 'iamsaipc/add_model.php', '[108, 109, 110]'),
(40, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 64, '<form action="add_model.php" data-hi="hi" method="post">\n<label for="uname">Name <br>\r\n	(please enter your name in the box below)\r\n	</br></label>\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n<label for="pass">PIN <br>\r\n	(please create a four (4) digit numeric PIN in the box below) <br>\r\n 	(please remember and don''t forget your PIN)\r\n	</br></br></label>\n<input id="pass" name="pass" pattern="d{4}" placeholder="Password" required="" type="password">\n<!--<input type="" value="nothing" name="" />-->\n<input class="button green" type="submit" value="Signup">\n</input></input></input></form>', 'post', 'add_model.php', 'iamsaipc/add_model.php', '[111, 112, 113]'),
(41, 'http://localhost/VV/vv.htm', '[{"onsubmit": "do()", "name": "f2"}]', 65, '<form name="f2" onsubmit="do()">\n<label for="uname">Name\r\n	</label>\n<input id="uname2" name="uname2" placeholder="Enter Name here" required="" type="text">\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="email">\n</input></input></form>', 'GET', '', 'iamsaipc/', '[114, 115]'),
(42, 'http://localhost/VV/vv.htm', '[{"name": "f2", "onsubmit": "do()"}]', 66, '<form name="f2" onsubmit="do()">\n<label for="uname">Name\r\n	</label>\n<input id="uname2" name="uname2" placeholder="Enter Name here" required="" type="text">\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="email">\n</input></input></form>', 'GET', '', 'iamsaipc/', '[116, 117]'),
(43, 'http://localhost/VV/vv.htm', '[{"data-hi": "hi"}]', 67, '<form action="add_model.php" data-hi="hi" method="post">\n<label for="uname">Name <br>\r\n	(please enter your name in the box below)\r\n	</br></label>\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="text">\n<label for="pass">PIN <br>\r\n	(please create a four (4) digit numeric PIN in the box below) <br>\r\n 	(please remember and don''t forget your PIN)\r\n	</br></br></label>\n<input id="pass" name="pass" pattern="d{4}" placeholder="Password" required="" type="password">\n<!--<input type="" value="nothing" name="" />-->\n<input class="button green" type="submit" value="Signup">\n</input></input></input></form>', 'post', 'add_model.php', 'iamsaipc/add_model.php', '[118, 119, 120]'),
(44, 'http://localhost/VV/vv.htm', '[{"name": "f2", "onsubmit": "do()"}]', 68, '<form name="f2" onsubmit="do()">\n<label for="uname">Name\r\n	</label>\n<input id="uname2" name="uname2" placeholder="Enter Name here" required="" type="text">\n<input id="uname" name="uname" placeholder="Enter Name here" required="" type="email">\n</input></input></form>', 'GET', '', 'iamsaipc/', '[121, 122]');

-- --------------------------------------------------------

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
-- Dumping data for table `params`
--

INSERT INTO `params` (`id`, `element_type`, `type`, `name`, `value`, `form_id`) VALUES
(19, 'input', 'password', 'pass', '', 7),
(20, 'input', 'text', 'uname', '', 7),
(21, 'input', 'submit', '', 'Signup', 7),
(22, 'input', 'password', 'pass', '', 8),
(23, 'input', 'text', 'uname', '', 8),
(24, 'input', 'submit', '', 'Signup', 8),
(25, 'input', 'text', 'uname', '', 9),
(26, 'input', 'password', 'pass', '', 9),
(27, 'input', 'submit', '', 'Signup', 9),
(32, 'input', 'submit', '', 'Signup', 10),
(33, 'input', 'text', 'uname', '', 10),
(34, 'input', 'password', 'pass', '', 10),
(35, 'input', 'text', 'uname2', '', 11),
(36, 'input', 'text', 'uname', '', 11),
(40, 'input', 'text', 'uname', '', 12),
(41, 'input', 'password', 'pass', '', 12),
(42, 'input', 'submit', '', 'Signup', 12),
(43, 'input', 'text', 'uname2', '', 13),
(44, 'input', 'text', 'uname', '', 13),
(45, 'input', 'password', 'pass', '', 14),
(46, 'input', 'text', 'uname', '', 14),
(47, 'input', 'submit', '', 'Signup', 14),
(48, 'input', 'text', 'uname', '', 15),
(49, 'input', 'text', 'uname2', '', 15),
(50, 'input', 'password', 'pass', '', 16),
(51, 'input', 'submit', '', 'Signup', 16),
(52, 'input', 'text', 'uname', '', 16),
(53, 'input', 'text', 'uname2', '', 17),
(54, 'input', 'text', 'uname', '', 17),
(55, 'input', 'text', 'uname', '', 18),
(56, 'input', 'submit', '', 'Signup', 18),
(57, 'input', 'password', 'pass', '', 18),
(58, 'input', 'text', 'uname2', '', 19),
(59, 'input', 'text', 'uname', '', 19),
(60, 'input', 'text', 'uname', '', 20),
(61, 'input', 'submit', '', 'Signup', 20),
(62, 'input', 'password', 'pass', '', 20),
(63, 'input', 'text', 'uname', '', 21),
(64, 'input', 'password', 'pass', '', 21),
(65, 'input', 'submit', '', 'Signup', 21),
(66, 'input', 'text', 'uname', '', 22),
(67, 'input', 'text', 'uname2', '', 22),
(68, 'input', 'password', 'pass', '', 23),
(69, 'input', 'submit', '', 'Signup', 23),
(70, 'input', 'text', 'uname', '', 23),
(71, 'input', 'text', 'uname2', '', 24),
(72, 'input', 'text', 'uname', '', 24),
(73, 'input', 'text', 'uname', '', 25),
(74, 'input', 'password', 'pass', '', 25),
(75, 'input', 'submit', '', 'Signup', 25),
(76, 'input', 'text', 'uname', '', 26),
(77, 'input', 'text', 'uname2', '', 26),
(78, 'input', 'text', 'uname', '', 27),
(79, 'input', 'submit', '', 'Signup', 27),
(80, 'input', 'password', 'pass', '', 27),
(81, 'input', 'text', 'uname2', '', 28),
(82, 'input', 'text', 'uname', '', 28),
(83, 'input', 'text', 'uname', '', 29),
(84, 'input', 'password', 'pass', '', 29),
(85, 'input', 'submit', '', 'Signup', 29),
(86, 'input', 'text', 'uname2', '', 30),
(87, 'input', 'email', 'uname', '', 30),
(88, 'input', 'submit', '', 'Signup', 31),
(89, 'input', 'text', 'uname', '', 31),
(90, 'input', 'password', 'pass', '', 31),
(91, 'input', 'text', 'uname2', '', 32),
(92, 'input', 'email', 'uname', '', 32),
(93, 'input', 'password', 'pass', '', 33),
(94, 'input', 'text', 'uname', '', 33),
(95, 'input', 'submit', '', 'Signup', 33),
(96, 'input', 'text', 'uname2', '', 34),
(97, 'input', 'email', 'uname', '', 34),
(98, 'input', 'submit', '', 'Signup', 35),
(99, 'input', 'text', 'uname', '', 35),
(100, 'input', 'password', 'pass', '', 35),
(101, 'input', 'text', 'uname2', '', 36),
(102, 'input', 'email', 'uname', '', 36),
(103, 'input', 'password', 'pass', '', 37),
(104, 'input', 'text', 'uname', '', 37),
(105, 'input', 'submit', '', 'Signup', 37),
(106, 'input', 'text', 'uname2', '', 38),
(107, 'input', 'email', 'uname', '', 38),
(108, 'input', 'password', 'pass', '', 39),
(109, 'input', 'text', 'uname', '', 39),
(110, 'input', 'submit', '', 'Signup', 39),
(111, 'input', 'text', 'uname', '', 40),
(112, 'input', 'password', 'pass', '', 40),
(113, 'input', 'submit', '', 'Signup', 40),
(114, 'input', 'text', 'uname2', '', 41),
(115, 'input', 'email', 'uname', '', 41),
(116, 'input', 'text', 'uname2', '', 42),
(117, 'input', 'email', 'uname', '', 42),
(118, 'input', 'text', 'uname', '', 43),
(119, 'input', 'submit', '', 'Signup', 43),
(120, 'input', 'password', 'pass', '', 43),
(121, 'input', 'text', 'uname2', '', 44),
(122, 'input', 'email', 'uname', '', 44);

-- --------------------------------------------------------

--
-- Table structure for table `requests`
--

CREATE TABLE IF NOT EXISTS `requests` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `headers` varchar(1024) NOT NULL,
  `url` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=69 ;

--
-- Dumping data for table `requests`
--

INSERT INTO `requests` (`id`, `headers`, `url`) VALUES
(4, 'None', 'http://localhost/VV/vv.htm'),
(5, 'None', 'http://localhost/VV/vv.htm'),
(6, 'None', 'http://localhost/VV/vv.htm'),
(7, 'None', 'http://localhost/VV/vv.htm'),
(8, 'None', 'http://localhost/VV/vv.htm'),
(9, 'None', 'http://localhost/VV/vv.htm'),
(10, 'None', 'http://localhost/VV/vv.htm'),
(11, 'None', 'http://localhost/VV/vv.htm'),
(12, 'None', 'http://localhost/VV/vv.htm'),
(13, 'None', 'http://localhost/VV/vv.htm'),
(14, 'None', 'http://localhost/VV/vv.htm'),
(15, 'None', 'http://localhost/VV/vv.htm'),
(16, 'None', 'http://localhost/VV/vv.htm'),
(17, 'None', 'http://localhost/VV/vv.htm'),
(18, 'None', 'http://localhost/VV/vv.htm'),
(19, 'None', 'http://localhost/VV/vv.htm'),
(20, 'None', 'http://localhost/VV/vv.htm'),
(21, 'None', 'http://localhost/VV/vv.htm'),
(22, 'None', 'http://localhost/VV/vv.htm'),
(23, 'None', 'http://localhost/VV/vv.htm'),
(24, 'None', 'http://localhost/VV/vv.htm'),
(25, 'None', 'http://localhost/VV/vv.htm'),
(26, 'None', 'http://localhost/VV/vv.htm'),
(29, 'None', 'http://localhost/VV/vv.htm'),
(30, 'None', 'http://localhost/VV/vv.htm'),
(31, 'None', 'http://localhost/VV/vv.htm'),
(32, 'None', 'http://localhost/VV/vv.htm'),
(34, 'None', 'http://localhost/VV/vv.htm'),
(35, 'None', 'http://localhost/VV/vv.htm'),
(36, '[["User-agent", "Mozilla/5.0"], ["Host", "localhost"], ["Referer", "localhost"]]', 'http://localhost/VV/vv.htm'),
(37, '[["User-agent", "Mozilla/5.0"], ["Host", "localhost"], ["Referer", "localhost"]]', 'http://localhost/VV/vv.htm'),
(38, '[["Host", "localhost"], ["User-agent", "Mozilla/5.0"], ["Referer", "localhost"]]', 'http://localhost/VV/vv.htm'),
(39, '[["Host", "localhost"], ["User-agent", "Mozilla/5.0"], ["Referer", "localhost"]]', 'http://localhost/VV/vv.htm'),
(40, '[["Host", "localhost"], ["Referer", "localhost"], ["User-agent", "Mozilla/5.0"]]', 'http://localhost/VV/vv.htm'),
(41, '[["Host", "localhost"], ["Referer", "localhost"], ["User-agent", "Mozilla/5.0"]]', 'http://localhost/VV/vv.htm'),
(42, '[["Referer", "localhost"], ["Host", "localhost"], ["User-agent", "Mozilla/5.0"]]', 'http://localhost/VV/vv.htm'),
(43, '[["Referer", "localhost"], ["Host", "localhost"], ["User-agent", "Mozilla/5.0"]]', 'http://localhost/VV/vv.htm'),
(44, '[["Referer", "localhost"], ["Host", "localhost"], ["User-agent", "Mozilla/5.0"]]', 'http://localhost/VV/vv.htm'),
(45, '[["User-agent", "Mozilla/5.0"], ["Referer", "localhost"], ["Host", "localhost"]]', 'http://localhost/VV/vv.htm'),
(46, '[["User-agent", "Mozilla/5.0"], ["Referer", "localhost"], ["Host", "localhost"]]', 'http://localhost/VV/vv.htm'),
(47, '[["Host", "localhost"], ["Referer", "localhost"], ["User-agent", "Mozilla/5.0"]]', 'http://localhost/VV/vv.htm'),
(48, '[["Host", "localhost"], ["Referer", "localhost"], ["User-agent", "Mozilla/5.0"]]', 'http://localhost/VV/vv.htm'),
(49, '[["User-agent", "Mozilla/5.0"], ["Referer", "localhost"], ["Host", "localhost"]]', 'http://localhost/VV/vv.htm'),
(50, '[["User-agent", "Mozilla/5.0"], ["Referer", "localhost"], ["Host", "localhost"]]', 'http://localhost/VV/vv.htm'),
(51, '[["Referer", "localhost"], ["User-agent", "Mozilla/5.0"], ["Host", "localhost"]]', 'http://localhost/VV/vv.htm'),
(52, '[["Referer", "localhost"], ["User-agent", "Mozilla/5.0"], ["Host", "localhost"]]', 'http://localhost/VV/vv.htm'),
(53, '[["Host", "localhost"], ["Referer", "localhost"], ["User-agent", "Mozilla/5.0"]]', 'http://localhost/VV/vv.htm'),
(54, '[["Host", "localhost"], ["Referer", "localhost"], ["User-agent", "Mozilla/5.0"]]', 'http://localhost/VV/vv.htm'),
(55, '[["Referer", "localhost"], ["Host", "localhost"], ["User-agent", "Mozilla/5.0"]]', 'http://localhost/VV/vv.htm'),
(56, '[["Referer", "localhost"], ["Host", "localhost"], ["User-agent", "Mozilla/5.0"]]', 'http://localhost/VV/vv.htm'),
(57, '[["User-agent", "Mozilla/5.0"], ["Referer", "localhost"], ["Host", "localhost"]]', 'http://localhost/VV/vv.htm'),
(58, '[["User-agent", "Mozilla/5.0"], ["Referer", "localhost"], ["Host", "localhost"]]', 'http://localhost/VV/vv.htm'),
(59, '[["Referer", "localhost"], ["User-agent", "Mozilla/5.0"], ["Host", "localhost"]]', 'http://localhost/VV/vv.htm'),
(60, '[["Referer", "localhost"], ["User-agent", "Mozilla/5.0"], ["Host", "localhost"]]', 'http://localhost/VV/vv.htm'),
(61, '[["User-agent", "Mozilla/5.0"], ["Host", "localhost"], ["Referer", "localhost"]]', 'http://localhost/VV/vv.htm'),
(62, '[["User-agent", "Mozilla/5.0"], ["Host", "localhost"], ["Referer", "localhost"]]', 'http://localhost/VV/vv.htm'),
(63, '[["User-agent", "Mozilla/5.0"], ["Referer", "localhost"], ["Host", "localhost"]]', 'http://localhost/VV/vv.htm'),
(64, '[["Host", "localhost"], ["Referer", "localhost"], ["User-agent", "Mozilla/5.0"]]', 'http://localhost/VV/vv.htm'),
(65, '[["User-agent", "Mozilla/5.0"], ["Referer", "localhost"], ["Host", "localhost"]]', 'http://localhost/VV/vv.htm'),
(66, '[["Host", "localhost"], ["Referer", "localhost"], ["User-agent", "Mozilla/5.0"]]', 'http://localhost/VV/vv.htm'),
(67, '[["Host", "localhost"], ["User-agent", "Mozilla/5.0"], ["Referer", "localhost"]]', 'http://localhost/VV/vv.htm'),
(68, '[["Host", "localhost"], ["User-agent", "Mozilla/5.0"], ["Referer", "localhost"]]', 'http://localhost/VV/vv.htm');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
