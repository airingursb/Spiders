/*
 Navicat MySQL Data Transfer

 Source Server         : MySQL
 Source Server Version : 50163
 Source Host           : localhost
 Source Database       : python

 Target Server Version : 50163
 File Encoding         : utf-8

 Date: 02/22/2016 21:54:35 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `bilibili_user_info`
-- ----------------------------
DROP TABLE IF EXISTS `bilibili_user_info`;
CREATE TABLE `bilibili_user_info` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `mid` varchar(11) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `sex` varchar(11) DEFAULT NULL,
  `face` varchar(200) DEFAULT NULL,
  `coins` int(11) DEFAULT NULL,
  `regtime` varchar(45) DEFAULT NULL,
  `spacesta` int(11) DEFAULT NULL,
  `birthday` varchar(45) DEFAULT NULL,
  `place` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `article` int(11) DEFAULT NULL,
  `fans` int(11) DEFAULT NULL,
  `friend` int(11) DEFAULT NULL,
  `attention` int(11) DEFAULT NULL,
  `sign` varchar(300) DEFAULT NULL,
  `attentions` text,
  `level` int(11) DEFAULT NULL,
  `exp` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=24178780 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `video`
-- ----------------------------
DROP TABLE IF EXISTS `video`;
CREATE TABLE `video` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `av` int(11) DEFAULT NULL,
  `cid` int(11) DEFAULT NULL,
  `title` varchar(150) DEFAULT NULL,
  `tminfo` varchar(45) DEFAULT NULL,
  `time` varchar(45) DEFAULT NULL,
  `click` int(11) DEFAULT NULL,
  `danmu` int(11) DEFAULT NULL,
  `coins` int(11) DEFAULT NULL,
  `favourites` int(11) DEFAULT NULL,
  `duration` varchar(45) DEFAULT NULL,
  `mid` int(11) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `article` int(11) DEFAULT NULL,
  `fans` int(11) DEFAULT NULL,
  `tag1` varchar(45) DEFAULT NULL,
  `tag2` varchar(45) DEFAULT NULL,
  `tag3` varchar(45) DEFAULT NULL,
  `common` int(11) DEFAULT NULL,
  `honor_click` int(11) DEFAULT NULL,
  `honor_coins` int(11) DEFAULT NULL,
  `honor_favourites` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3813749 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
