/*
 Navicat Premium Data Transfer

 Source Server         : lsy
 Source Server Type    : MySQL
 Source Server Version : 80015
 Source Host           : localhost:3306
 Source Schema         : logistics

 Target Server Type    : MySQL
 Target Server Version : 80015
 File Encoding         : 65001

 Date: 04/12/2020 21:44:00
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 85 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add evaluate', 7, 'add_evaluate');
INSERT INTO `auth_permission` VALUES (26, 'Can change evaluate', 7, 'change_evaluate');
INSERT INTO `auth_permission` VALUES (27, 'Can delete evaluate', 7, 'delete_evaluate');
INSERT INTO `auth_permission` VALUES (28, 'Can view evaluate', 7, 'view_evaluate');
INSERT INTO `auth_permission` VALUES (29, 'Can add evaluate info', 8, 'add_evaluateinfo');
INSERT INTO `auth_permission` VALUES (30, 'Can change evaluate info', 8, 'change_evaluateinfo');
INSERT INTO `auth_permission` VALUES (31, 'Can delete evaluate info', 8, 'delete_evaluateinfo');
INSERT INTO `auth_permission` VALUES (32, 'Can view evaluate info', 8, 'view_evaluateinfo');
INSERT INTO `auth_permission` VALUES (33, 'Can add fm evaluate', 7, 'add_fmevaluate');
INSERT INTO `auth_permission` VALUES (34, 'Can change fm evaluate', 7, 'change_fmevaluate');
INSERT INTO `auth_permission` VALUES (35, 'Can delete fm evaluate', 7, 'delete_fmevaluate');
INSERT INTO `auth_permission` VALUES (36, 'Can view fm evaluate', 7, 'view_fmevaluate');
INSERT INTO `auth_permission` VALUES (37, 'Can add fm evaluate info', 8, 'add_fmevaluateinfo');
INSERT INTO `auth_permission` VALUES (38, 'Can change fm evaluate info', 8, 'change_fmevaluateinfo');
INSERT INTO `auth_permission` VALUES (39, 'Can delete fm evaluate info', 8, 'delete_fmevaluateinfo');
INSERT INTO `auth_permission` VALUES (40, 'Can view fm evaluate info', 8, 'view_fmevaluateinfo');
INSERT INTO `auth_permission` VALUES (41, 'Can add om back order', 9, 'add_ombackorder');
INSERT INTO `auth_permission` VALUES (42, 'Can change om back order', 9, 'change_ombackorder');
INSERT INTO `auth_permission` VALUES (43, 'Can delete om back order', 9, 'delete_ombackorder');
INSERT INTO `auth_permission` VALUES (44, 'Can view om back order', 9, 'view_ombackorder');
INSERT INTO `auth_permission` VALUES (45, 'Can add om bl', 10, 'add_ombl');
INSERT INTO `auth_permission` VALUES (46, 'Can change om bl', 10, 'change_ombl');
INSERT INTO `auth_permission` VALUES (47, 'Can delete om bl', 10, 'delete_ombl');
INSERT INTO `auth_permission` VALUES (48, 'Can view om bl', 10, 'view_ombl');
INSERT INTO `auth_permission` VALUES (49, 'Can add om concract', 11, 'add_omconcract');
INSERT INTO `auth_permission` VALUES (50, 'Can change om concract', 11, 'change_omconcract');
INSERT INTO `auth_permission` VALUES (51, 'Can delete om concract', 11, 'delete_omconcract');
INSERT INTO `auth_permission` VALUES (52, 'Can view om concract', 11, 'view_omconcract');
INSERT INTO `auth_permission` VALUES (53, 'Can add om detail', 12, 'add_omdetail');
INSERT INTO `auth_permission` VALUES (54, 'Can change om detail', 12, 'change_omdetail');
INSERT INTO `auth_permission` VALUES (55, 'Can delete om detail', 12, 'delete_omdetail');
INSERT INTO `auth_permission` VALUES (56, 'Can view om detail', 12, 'view_omdetail');
INSERT INTO `auth_permission` VALUES (57, 'Can add om detail warehouse', 13, 'add_omdetailwarehouse');
INSERT INTO `auth_permission` VALUES (58, 'Can change om detail warehouse', 13, 'change_omdetailwarehouse');
INSERT INTO `auth_permission` VALUES (59, 'Can delete om detail warehouse', 13, 'delete_omdetailwarehouse');
INSERT INTO `auth_permission` VALUES (60, 'Can view om detail warehouse', 13, 'view_omdetailwarehouse');
INSERT INTO `auth_permission` VALUES (61, 'Can add om order', 14, 'add_omorder');
INSERT INTO `auth_permission` VALUES (62, 'Can change om order', 14, 'change_omorder');
INSERT INTO `auth_permission` VALUES (63, 'Can delete om order', 14, 'delete_omorder');
INSERT INTO `auth_permission` VALUES (64, 'Can view om order', 14, 'view_omorder');
INSERT INTO `auth_permission` VALUES (65, 'Can add code', 15, 'add_code');
INSERT INTO `auth_permission` VALUES (66, 'Can change code', 15, 'change_code');
INSERT INTO `auth_permission` VALUES (67, 'Can delete code', 15, 'delete_code');
INSERT INTO `auth_permission` VALUES (68, 'Can view code', 15, 'view_code');
INSERT INTO `auth_permission` VALUES (69, 'Can add role_menu', 16, 'add_role_menu');
INSERT INTO `auth_permission` VALUES (70, 'Can change role_menu', 16, 'change_role_menu');
INSERT INTO `auth_permission` VALUES (71, 'Can delete role_menu', 16, 'delete_role_menu');
INSERT INTO `auth_permission` VALUES (72, 'Can view role_menu', 16, 'view_role_menu');
INSERT INTO `auth_permission` VALUES (73, 'Can add user_profile', 17, 'add_user_profile');
INSERT INTO `auth_permission` VALUES (74, 'Can change user_profile', 17, 'change_user_profile');
INSERT INTO `auth_permission` VALUES (75, 'Can delete user_profile', 17, 'delete_user_profile');
INSERT INTO `auth_permission` VALUES (76, 'Can view user_profile', 17, 'view_user_profile');
INSERT INTO `auth_permission` VALUES (77, 'Can add role', 18, 'add_role');
INSERT INTO `auth_permission` VALUES (78, 'Can change role', 18, 'change_role');
INSERT INTO `auth_permission` VALUES (79, 'Can delete role', 18, 'delete_role');
INSERT INTO `auth_permission` VALUES (80, 'Can view role', 18, 'view_role');
INSERT INTO `auth_permission` VALUES (81, 'Can add menu', 19, 'add_menu');
INSERT INTO `auth_permission` VALUES (82, 'Can change menu', 19, 'change_menu');
INSERT INTO `auth_permission` VALUES (83, 'Can delete menu', 19, 'delete_menu');
INSERT INTO `auth_permission` VALUES (84, 'Can view menu', 19, 'view_menu');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES (1, 'pbkdf2_sha256$216000$snrQoavSzlhK$N3rpIL9yJb6Gzg9GDDfPAyFuGEVrCYhSGJSkybcJvAk=', '2020-12-04 21:32:42.793285', 1, 'lsy', '', '', '1291012840@qq.com', 1, 1, '2020-12-04 13:44:33.234619');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (7, 'fm', 'fmevaluate');
INSERT INTO `django_content_type` VALUES (8, 'fm', 'fmevaluateinfo');
INSERT INTO `django_content_type` VALUES (9, 'om', 'ombackorder');
INSERT INTO `django_content_type` VALUES (10, 'om', 'ombl');
INSERT INTO `django_content_type` VALUES (11, 'om', 'omconcract');
INSERT INTO `django_content_type` VALUES (12, 'om', 'omdetail');
INSERT INTO `django_content_type` VALUES (13, 'om', 'omdetailwarehouse');
INSERT INTO `django_content_type` VALUES (14, 'om', 'omorder');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (15, 'sm', 'code');
INSERT INTO `django_content_type` VALUES (19, 'sm', 'menu');
INSERT INTO `django_content_type` VALUES (18, 'sm', 'role');
INSERT INTO `django_content_type` VALUES (16, 'sm', 'role_menu');
INSERT INTO `django_content_type` VALUES (17, 'sm', 'user_profile');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 31 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2020-11-21 17:37:51.690776');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2020-11-21 17:37:51.954015');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2020-11-21 17:37:52.791776');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2020-11-21 17:37:52.998964');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2020-11-21 17:37:53.008973');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2020-11-21 17:37:53.158108');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2020-11-21 17:37:53.274214');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0003_alter_user_email_max_length', '2020-11-21 17:37:53.380311');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0004_alter_user_username_opts', '2020-11-21 17:37:53.392322');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0005_alter_user_last_login_null', '2020-11-21 17:37:53.484405');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0006_require_contenttypes_0002', '2020-11-21 17:37:53.491412');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2020-11-21 17:37:53.501421');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0008_alter_user_username_max_length', '2020-11-21 17:37:53.611521');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2020-11-21 17:37:53.717617');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0010_alter_group_name_max_length', '2020-11-21 17:37:53.821711');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0011_update_proxy_permissions', '2020-11-21 17:37:53.832722');
INSERT INTO `django_migrations` VALUES (17, 'auth', '0012_alter_user_first_name_max_length', '2020-11-21 17:37:53.943823');
INSERT INTO `django_migrations` VALUES (18, 'rm', '0001_initial', '2020-11-21 17:37:53.985861');
INSERT INTO `django_migrations` VALUES (19, 'rm', '0002_delete_t_rm_user', '2020-11-21 17:37:54.012885');
INSERT INTO `django_migrations` VALUES (20, 'sessions', '0001_initial', '2020-11-21 17:37:54.053922');
INSERT INTO `django_migrations` VALUES (21, 'fm', '0001_initial', '2020-11-21 17:44:04.160049');
INSERT INTO `django_migrations` VALUES (22, 'fm', '0002_auto_20201121_1757', '2020-11-21 17:58:03.348243');
INSERT INTO `django_migrations` VALUES (23, 'fm', '0003_auto_20201122_2150', '2020-11-22 21:51:07.254591');
INSERT INTO `django_migrations` VALUES (24, 'fm', '0004_auto_20201123_2046', '2020-11-23 20:46:19.044488');
INSERT INTO `django_migrations` VALUES (28, 'om', '0001_initial', '2020-11-24 10:04:59.506736');
INSERT INTO `django_migrations` VALUES (29, 'fm', '0005_auto_20201124_1709', '2020-11-24 17:09:28.629153');
INSERT INTO `django_migrations` VALUES (30, 'sm', '0001_initial', '2020-12-04 13:14:18.764895');
INSERT INTO `django_migrations` VALUES (31, 'sm', '0002_menu_icon', '2020-12-04 13:31:22.105482');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('2jlu5i306raofywwlx4b2291e4urknb0', '.eJx1kdtuwjAMht8l11VpnKZNuJzEJXsBQChHDmtTqSWT0LR3n7OFAYOprWvX_2fXzgeJ24Mlc0JJgW5QvcOgm87f4Th0KVzHViuKtq6adeQ1F7_ZK9x3lMxXK0KrFKUHAeM1Wmf9bQlS0IK8DsGRTZH0cNU7y5JStg96stmkHnDp8dOlyhwHsY4NsEduNvWzOLlxqYLaXTrmnpkW0gJaaOEpncb8Q7NbmlmDS2GcP6V7F-IdDfnP4XFiztAX2rf_1fM93ot31UV1cotwGs95LQzXgs5WxdN-m8a9nsvNN63MmwspYY8q7IbSDFjjoMskKXN2KpeDdd1L1t4V2KtpjzRnjfcGrGZc-lZRoJX2jklRM8PAcA8KKtNq0TAF1krh8S2k8RwvaWry-QUf47b7:1kl9jC:x4LvHdY_2KsCw5eexTZ3dL-wATXU-P9sYL_0k-0G6HU', '2020-12-04 20:28:22.790025');
INSERT INTO `django_session` VALUES ('5uhr5meovg6af9tekaadsz9l857rxi9y', '.eJxVjE0OgjAQhe_StSG0pdCydO8JxJDpn6AFEkoXxnh3W0XRTDLzvXlv5o5C22tUI4x2EUcYTBTO315ynlySTagk4NiLvGwCKxj_utvx4DCqj6cE5AP0DS2EpWuDN_MW_9lJUFczJkNfYDxPmZrGZe5lliLZ6vrsMGnj9mv270EHvovXjJbWKqIlZcJWgAnOpTVU8IIqShSzBEiuKslLCkRrwW2cXCjLYglVoMcTjPtUiQ:1kl4ey:GFV8yb7-y3qGpfttcOUI-zrTk8nMCrqPdksoJgw5wgk', '2020-12-04 15:03:40.714746');
INSERT INTO `django_session` VALUES ('60nn1rpn9z6shmqinu1ndgow7bkqy7ik', '.eJxtkM1ugzAMx98lZ0SJQyDpcffuBUqF8lm6QZCgOVTV3n1OS1e2VVFs_2P_LDtXEtuTJVtCSYZhUIND0c-Xm5zGPskm1lpRtGVRNZGXXPxkn_DQU7Ld7wktkkoXAeM1Wmf9ugXJaEbex-DI4ZA4eHB3slhYDqKJFbD6H7uZh02c3bRTQR2xS3anYUULaQEt1PCSTqP_odmaZtbgoozzl_TgQnzQtw0YboBBq-K5a9Nkz29ZvWllPl1ICfuhwnHMzRjO00nnqSRfsnO-G63r35baXw06NXdIc1Z5b8BqxqWvFQVaaO-YFCUzDAz3oKAwtRYVU2CtFB69kMZzPNKU5OsbfhSTcw:1kl5zv:fmjZWnPOJrNJVde0rA5601Jt6gocp64hunpwmUNZC68', '2020-12-04 16:29:23.541255');
INSERT INTO `django_session` VALUES ('6tka2u5uidbcmv27lviqo7p1ggep8xxo', '.eJxtkM1ugzAMx98lZ0SJQyDpcffuBUqF8lm6QZCgOVTV3n1OS1e2VVFs_2P_LDtXEtuTJVtCSYZhUIND0c-Xm5zGPskm1lpRtGVRNZGXXPxkn_DQU7Ld7wktkkoXAeM1Wmf9ugXJaEbex-DI4ZA4eHB3slhYDqKJFbD6H7uZh02c3bRTQR2xS3anYUULaQEt1PCSTqP_odmaZtbgoozzl_TgQnzQtw0YboBBq-K5a9Nkz29ZvWllPl1ICfuhwnHMzRjO00nnqSRfsnO-G63r35baXw06NXdIc1Z5b8BqxqWvFQVaaO-YFCUzDAz3oKAwtRYVU2CtFB69kMZzPNKU5OsbfhSTcw:1kl64R:ksbPUAlxKcVs69dYmfWSLK4BYPi30MJv2jmaTsaB6us', '2020-12-04 16:34:03.053481');
INSERT INTO `django_session` VALUES ('bx2scg737mysfp03f88ss9twmg1xf9ua', '.eJxVjE0OgjAQhe_StSG0pdCydO8JxJDpn6AFEkoXxnh3W0XRTDLzvXlv5o5C22tUI4x2EUcYTBTO315ynlySTagk4NiLvGwCKxj_utvx4DCqj6cE5AP0DS2EpWuDN_MW_9lJUFczJkNfYDxPmZrGZe5lliLZ6vrsMGnj9mv270EHvovXjJbWKqIlZcJWgAnOpTVU8IIqShSzBEiuKslLCkRrwW2cXCjLYglVoMcTjPtUiQ:1kl4OS:izVIuvbFG2_sTnVFC4qpFgEWWxJYDgBP3Z5a2wrRI6Q', '2020-12-04 14:46:36.565767');
INSERT INTO `django_session` VALUES ('bzmk8f4ckoq3jg39yyoc87b2lwwbh43d', '.eJyNldtu2zAMht_F10Fqizr2ckAvuxdoi0DWoWmXOEASDyiGvftIW7aV2u6KJIpkffxFiSL9p2h3b764L6pig93GHgMODpePbng-HWj43KraVtjyUj63ggs9zk7Gx0NV3D89FVVJI_qhgYs1tsHHXKLYVJvi56kJxcuGeDbxwQORRs34xMLI8hhwXpYStQV47ItA0xPLR1bXlhElxJquGFmhmCZP6pj7k7NyYrnVpB5QXTIjqO9MzqplXUn-SrA3ujo_h9h5TZQKol8jZ83ISqFK0pKhUxS0zzCcwwvFhQ1x6SNTpjUE-SMZzM_67nK8ay_h_Ggb-zpEKcUpWWvjcc-aKbZoTVfjkzXk1uDdSjzI-hia9pM1z6wFODbsezmaKZ7DalFKarVc52XO1w4ZHuQXvMp46TkxtsS7birusR9luOV1fvLB8a5VFF2w1Gq-thZLUWPzDBEA5G1Ua2cZj_h9-G0Prb2Gh-Z6_hjSKIlCv2HPyJVgyrVUghR8yA70K54nfZ6uGtC1rAXxvNRd6255lvHfSNekL-b8YsqKpJ_46EvaNZjVFE_6Mp0P590q8zI28izjp1Kwxqukr-b-L5YGlfTV_IKu8JDxPHq8lEZKs87zXD9PmOVSlfzXfUJ2_velZLlc6eS_nu13jYdcPy-zy-Uw-WP6_QaL8cJnmFrC8fI_RTIpsEwBkxlJwSh231DoyixgmcXOzrbX_Y7K5_RuzJ7V1v0KDU34d9u8nrbuhHn5Vm8J2abZy_bx5MPhR2JvBPb2skdrATJGx3wNwkRlK1aVdQxgNAcHzInILCudqjU6y7w3OuK_Ni4K_BjHi7__AJxSFrM:1klBNO:D-UBh0OuV3f0VCTaMyj0rZUJ_8pReBn837J_O4RwjgE', '2020-12-04 22:13:58.025663');
INSERT INTO `django_session` VALUES ('hdbplhmv1fll15prah2rwgrf779as2if', '.eJxVjLEOwyAQQ_-FuUIBQgIdu-cb0HHHlbQVkUIyVf33EilDKw-W_Gy_RYB9y2GvaQ0ziatQ4vKbRcBnKgegB5T7InEp2zpHeVTkSaucFkqv29n9O8hQc1tbMzCjpmis5xGUVl3kZLzrDRqNljXoDsfoBgOayDtu7jyybfLYi88X6q84PQ:1kl42H:IAvuMmE2M2Q3l-b8L5UOEjatm-TgNid4GrfzaPrW_tw', '2020-12-04 14:23:41.718723');
INSERT INTO `django_session` VALUES ('ihvy0uuesth2glzvo7g3iiq20m742vc0', '.eJx1kdtuwjAMht8l11VpnKZNuJzEJXsBQChHDmtTqSWT0LR3n7OFAYOprWvX_2fXzgeJ24Mlc0JJgW5QvcOgm87f4Th0KVzHViuKtq6adeQ1F7_ZK9x3lMxXK0KrFKUHAeM1Wmf9bQlS0IK8DsGRTZH0cNU7y5JStg96stmkHnDp8dOlyhwHsY4NsEduNvWzOLlxqYLaXTrmnpkW0gJaaOEpncb8Q7NbmlmDS2GcP6V7F-IdDfnP4XFiztAX2rf_1fM93ot31UV1cotwGs95LQzXgs5WxdN-m8a9nsvNN63MmwspYY8q7IbSDFjjoMskKXN2KpeDdd1L1t4V2KtpjzRnjfcGrGZc-lZRoJX2jklRM8PAcA8KKtNq0TAF1krh8S2k8RwvaWry-QUf47b7:1kl7Xn:RBmn4chO-sM941xhvVwj3RMj6dtruvvpMlf-S-DAClA', '2020-12-04 18:08:27.834185');
INSERT INTO `django_session` VALUES ('kmqn4ztvjinaw62u08hf9ef9gyjzo80r', '.eJxVjE0OgjAQhe_StSG0pdCydO8JxJDpn6AFEkoXxnh3W0XRTDLzvXlv5o5C22tUI4x2EUcYTBTO315ynlySTagk4NiLvGwCKxj_utvx4DCqj6cE5AP0DS2EpWuDN_MW_9lJUFczJkNfYDxPmZrGZe5lliLZ6vrsMGnj9mv270EHvovXjJbWKqIlZcJWgAnOpTVU8IIqShSzBEiuKslLCkRrwW2cXCjLYglVoMcTjPtUiQ:1kl5jD:NlV6W0CxVcyir7BIniucusjEiZ4UMyfrD-VPktop-RI', '2020-12-04 16:12:07.415947');
INSERT INTO `django_session` VALUES ('ngqsgzdg1tytu4eya5kbkbp0ojwnpav9', '.eJx1kdtuwjAMht8l11VpnKZNuJzEJXsBQChHDmtTqSWT0LR3n7OFAYOprWvX_2fXzgeJ24Mlc0JJgW5QvcOgm87f4Th0KVzHViuKtq6adeQ1F7_ZK9x3lMxXK0KrFKUHAeM1Wmf9bQlS0IK8DsGRTZH0cNU7y5JStg96stmkHnDp8dOlyhwHsY4NsEduNvWzOLlxqYLaXTrmnpkW0gJaaOEpncb8Q7NbmlmDS2GcP6V7F-IdDfnP4XFiztAX2rf_1fM93ot31UV1cotwGs95LQzXgs5WxdN-m8a9nsvNN63MmwspYY8q7IbSDFjjoMskKXN2KpeDdd1L1t4V2KtpjzRnjfcGrGZc-lZRoJX2jklRM8PAcA8KKtNq0TAF1krh8S2k8RwvaWry-QUf47b7:1kl7JR:seOsTczHJLPxlWbOK_uexTKmRqVAYjZrxTxEmtcWj3g', '2020-12-04 17:53:37.726643');
INSERT INTO `django_session` VALUES ('nib685ht6wmr9mb4rk0w0bhng8kj4mn3', '.eJx1kdtuwjAMht8l11VpnKZNuJzEJXsBQChHDmtTqSWT0LR3n7OFAYOprWvX_2fXzgeJ24Mlc0JJgW5QvcOgm87f4Th0KVzHViuKtq6adeQ1F7_ZK9x3lMxXK0KrFKUHAeM1Wmf9bQlS0IK8DsGRTZH0cNU7y5JStg96stmkHnDp8dOlyhwHsY4NsEduNvWzOLlxqYLaXTrmnpkW0gJaaOEpncb8Q7NbmlmDS2GcP6V7F-IdDfnP4XFiztAX2rf_1fM93ot31UV1cotwGs95LQzXgs5WxdN-m8a9nsvNN63MmwspYY8q7IbSDFjjoMskKXN2KpeDdd1L1t4V2KtpjzRnjfcGrGZc-lZRoJX2jklRM8PAcA8KKtNq0TAF1krh8S2k8RwvaWry-QUf47b7:1kl7CM:EyVLlwPlhITfbuBetvM6qUG14OZKocf4DOhXcIFodIM', '2020-12-04 17:46:18.026893');
INSERT INTO `django_session` VALUES ('o5ax86tscbc2sbqk6qwtzykn2iwzccw3', '.eJx1kdtuwjAMht8l11VpnKZNuJzEJXsBQChHDmtTqSWT0LR3n7OFAYOprWvX_2fXzgeJ24Mlc0JJgW5QvcOgm87f4Th0KVzHViuKtq6adeQ1F7_ZK9x3lMxXK0KrFKUHAeM1Wmf9bQlS0IK8DsGRTZH0cNU7y5JStg96stmkHnDp8dOlyhwHsY4NsEduNvWzOLlxqYLaXTrmnpkW0gJaaOEpncb8Q7NbmlmDS2GcP6V7F-IdDfnP4XFiztAX2rf_1fM93ot31UV1cotwGs95LQzXgs5WxdN-m8a9nsvNN63MmwspYY8q7IbSDFjjoMskKXN2KpeDdd1L1t4V2KtpjzRnjfcGrGZc-lZRoJX2jklRM8PAcA8KKtNq0TAF1krh8S2k8RwvaWry-QUf47b7:1klAh0:uJE-aWO-KemxKNatkLM660f0x54XCS1Lb817AOJQBsg', '2020-12-04 21:30:10.336178');
INSERT INTO `django_session` VALUES ('qci60vet20tzx1rk9w0owww19ju8d8kj', '.eJx1kdtuwjAMht8l11VpnKZNuJzEJXsBQChHDmtTqSWT0LR3n7OFAYOprWvX_2fXzgeJ24Mlc0JJgW5QvcOgm87f4Th0KVzHViuKtq6adeQ1F7_ZK9x3lMxXK0KrFKUHAeM1Wmf9bQlS0IK8DsGRTZH0cNU7y5JStg96stmkHnDp8dOlyhwHsY4NsEduNvWzOLlxqYLaXTrmnpkW0gJaaOEpncb8Q7NbmlmDS2GcP6V7F-IdDfnP4XFiztAX2rf_1fM93ot31UV1cotwGs95LQzXgs5WxdN-m8a9nsvNN63MmwspYY8q7IbSDFjjoMskKXN2KpeDdd1L1t4V2KtpjzRnjfcGrGZc-lZRoJX2jklRM8PAcA8KKtNq0TAF1krh8S2k8RwvaWry-QUf47b7:1kl7Dz:Ltyeb3NtAm_j290TH7n8o9zvDoJ5tQ3h5hCljTWHAaY', '2020-12-04 17:47:59.445652');
INSERT INTO `django_session` VALUES ('rbbqoovzinkr2wp41h4lbvklhb8phog4', '.eJx1kMtuwyAQRf-FteWYwdg4y-7TH4gji2cetbFkzCKq-u8dEqdxW0WIYS4z94jhk8TubMiWUJJh6uVgUfThepPT2CfZxlpJirEsqjbykouf6tM89JRs93tCi6TSRoN2CqM1bo0gGc3I--gtORySDx6-u7NYvBxEGytg9T_vJlzDbIdNDHbaSS-PSMruBFgRRGMAI9TwkpBG-ENgawIzGgdmnL8kDNbHB-E2DcNpMOlknE9deuHzi1Z3SuoP61PBXKQ_jrke_TydVZ5a8qUa8t1obP-29P4CnGQ4oZuzyjkNRjHeuFpSoIVyljWiZJqB5g4kFLpWomISjGmEw1M02nFcjS7J1zcXqJjC:1kl5ue:fiFao2zYTlcU5s8-QaeBhbe52z7U8ahQdNCpVrrsSJU', '2020-12-04 16:23:56.934584');
INSERT INTO `django_session` VALUES ('sgs872prmxlby0a2l5w9eb2as7at8c8e', '.eJxtkE1ugzAQhe_iNSJ4jMHOsvv0AiFC_g1JwUgQL6qqd--YkIZWkeXxPL_5Rh5_kdheLNkTSjJMgxocin7-XOQ09kk2sdaKYiyLqom85OLXfcJDT8n-eCS0SCptBIzXGJ312xbo0Yy8j8GR0ymB8ADvaLHCHEQTK2D1Fl7Y3Tzs4uymgwrqjF2yOw0bWkgLGKGGl3R6-z-abWlmDU7KOH9JDy7EB71MwHACTFoVb12bXvb8l82dVubDhWTYqwrnMTdjuE0XnaeSfHXn_DBa17-ttX8adGrukOas8t6A1YxLXysKtNDeMSlKZhgY7kFBYWotKqbAWik8nkIaz3FJU5LvH-mzk6Q:1kl6Mq:LSkUWWseS9cSSpfqfvGnJKNb5Ha5KJOcS0Y8ofbZjMA', '2020-12-04 16:53:04.109038');
INSERT INTO `django_session` VALUES ('yx3rtb5rguvl4e4wue2bofmltn75iu41', '.eJxtkE1ugzAQhe_iNSJ4jMHOsvv0AiFC_g1JwUgQL6qqd--YkIZWkeXxPL_5Rh5_kdheLNkTSjJMgxocin7-XOQ09kk2sdaKYiyLqom85OLXfcJDT8n-eCS0SCptBIzXGJ312xbo0Yy8j8GR0ymB8ADvaLHCHEQTK2D1Fl7Y3Tzs4uymgwrqjF2yOw0bWkgLGKGGl3R6-z-abWlmDU7KOH9JDy7EB71MwHACTFoVb12bXvb8l82dVubDhWTYqwrnMTdjuE0XnaeSfHXn_DBa17-ttX8adGrukOas8t6A1YxLXysKtNDeMSlKZhgY7kFBYWotKqbAWik8nkIaz3FJU5LvH-mzk6Q:1kl6N8:V3U2CvrxSwkhYo7HSlW4v4IGYHiH-6n8Hflbnh-Ru20', '2020-12-04 16:53:22.238538');
INSERT INTO `django_session` VALUES ('z2jvcqi7brfiywus51x2ctf0hanz0f05', '.eJx1kdtuwjAMht8l11VpnKZNuJzEJXsBQChHDmtTqSWT0LR3n7OFAYOprWvX_2fXzgeJ24Mlc0JJgW5QvcOgm87f4Th0KVzHViuKtq6adeQ1F7_ZK9x3lMxXK0KrFKUHAeM1Wmf9bQlS0IK8DsGRTZH0cNU7y5JStg96stmkHnDp8dOlyhwHsY4NsEduNvWzOLlxqYLaXTrmnpkW0gJaaOEpncb8Q7NbmlmDS2GcP6V7F-IdDfnP4XFiztAX2rf_1fM93ot31UV1cotwGs95LQzXgs5WxdN-m8a9nsvNN63MmwspYY8q7IbSDFjjoMskKXN2KpeDdd1L1t4V2KtpjzRnjfcGrGZc-lZRoJX2jklRM8PAcA8KKtNq0TAF1krh8S2k8RwvaWry-QUf47b7:1klAsG:a9N4wd0zdFevY250qHFjECiygBtEXEFu3bsnJD75IxI', '2020-12-04 21:41:48.845963');

-- ----------------------------
-- Table structure for t_fm_evaluate
-- ----------------------------
DROP TABLE IF EXISTS `t_fm_evaluate`;
CREATE TABLE `t_fm_evaluate`  (
  `evaluate_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `apply_num` varchar(12) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `apply_date` date NOT NULL,
  `evaluate_type` int(11) NULL DEFAULT NULL,
  `actual_evaluate_amount` double NULL DEFAULT NULL,
  `payment_amount` double NULL DEFAULT NULL,
  `freight_amount` double NULL DEFAULT NULL,
  `fine_amount` double NULL DEFAULT NULL,
  `liquidated_damages_amount` double NULL DEFAULT NULL,
  `evaluate_explain` varchar(300) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `evaluate_people_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `evaluate_people` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `evaluate_finish_time` date NULL DEFAULT NULL,
  `evaluate_state` int(11) NULL DEFAULT NULL,
  `company_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` datetime(6) NULL DEFAULT NULL,
  `create_user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `del_flag` int(11) NULL DEFAULT NULL,
  `dept_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `update_time` datetime(6) NULL DEFAULT NULL,
  `update_user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`evaluate_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_fm_evaluate
-- ----------------------------
INSERT INTO `t_fm_evaluate` VALUES ('1', '1', '1001', '2020-12-03', 1, 2, 2, 2, 2, 2, '2', '2', '2', '2020-12-10', 2, '2', '2020-12-23 20:16:12.000000', '0101', 111, NULL, '2020-12-09 20:16:22.000000', '11');
INSERT INTO `t_fm_evaluate` VALUES ('2', '', '1002', '2020-12-01', 1, 234234, 234234, 234234, 234234, 2342342, '2342342342\r\n                                ', '1111', '李李', '2020-12-01', 0, '1', '2021-01-09 21:17:16.000000', '222', 222, '22', '2020-12-30 21:17:27.000000', '222');
INSERT INTO `t_fm_evaluate` VALUES ('3', '', '1003', '2020-12-01', 1, 1231231, 213123, 123123, 1231231, 123123, '123123\r\n                                ', '1111', '李李', '2020-12-01', 0, '1', '2020-12-01 21:33:04.000000', '1001', 2, '2', '2020-12-01 21:33:04.000000', '1001');
INSERT INTO `t_fm_evaluate` VALUES ('4', '', '1004', '2020-12-04', 1, 233232, 32323, 32233223, 23323232, 323223, '3232232332\r\n                                ', '1111', '李李', '2020-12-04', 0, '1', '2020-12-04 20:56:05.000000', '1001', 2, '2', '2020-12-04 20:56:05.000000', '1001');
INSERT INTO `t_fm_evaluate` VALUES ('5', '', '1005', '2020-12-04', 1, 888, 456, 778.88, 888, 888, '8888\r\n                                ', '1111', '李李', '2020-12-04', 0, '1', '2020-12-04 20:58:29.000000', '1001', 2, '2', '2020-12-04 20:58:29.000000', '1001');

-- ----------------------------
-- Table structure for t_fm_evaluateinfo
-- ----------------------------
DROP TABLE IF EXISTS `t_fm_evaluateinfo`;
CREATE TABLE `t_fm_evaluateinfo`  (
  `evaluate_info_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `evaluate_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `order_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `company_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` datetime(6) NULL DEFAULT NULL,
  `create_user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `del_flag` int(11) NULL DEFAULT NULL,
  `dept_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `update_time` datetime(6) NULL DEFAULT NULL,
  `update_user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`evaluate_info_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for t_om_back_order
-- ----------------------------
DROP TABLE IF EXISTS `t_om_back_order`;
CREATE TABLE `t_om_back_order`  (
  `back_order_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `order_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `signer` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `signer_time` datetime(6) NULL DEFAULT NULL,
  `signer_opinion` varchar(320) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `back_order_status` int(11) NULL DEFAULT NULL,
  `back_order_Image_path1` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `back_order_Image_path2` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `back_order_Image_path3` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `company_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `dept_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` datetime(6) NULL DEFAULT NULL,
  `update_user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `update_time` datetime(6) NULL DEFAULT NULL,
  `del_flag` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`back_order_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for t_om_bl
-- ----------------------------
DROP TABLE IF EXISTS `t_om_bl`;
CREATE TABLE `t_om_bl`  (
  `bl_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `order_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `bl_person` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `bl_time` datetime(6) NOT NULL,
  `bl_status` int(11) NOT NULL,
  `company_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `dept_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` datetime(6) NULL DEFAULT NULL,
  `update_user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `update_time` datetime(6) NULL DEFAULT NULL,
  `del_flag` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`bl_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for t_om_concract
-- ----------------------------
DROP TABLE IF EXISTS `t_om_concract`;
CREATE TABLE `t_om_concract`  (
  `contract_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `contract_num` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `contract_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sign_time` datetime(6) NOT NULL,
  `contract_start_time` datetime(6) NULL DEFAULT NULL,
  `contract_end_time` datetime(6) NULL DEFAULT NULL,
  `contract_addr` varchar(280) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_company_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_person_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_person_tel` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `second_company_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `second_person_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `second_person_tel` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `contract_attachment` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `company_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `dept_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` datetime(6) NULL DEFAULT NULL,
  `update_user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `update_time` datetime(6) NULL DEFAULT NULL,
  `del_flag` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`contract_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for t_om_detail
-- ----------------------------
DROP TABLE IF EXISTS `t_om_detail`;
CREATE TABLE `t_om_detail`  (
  `detail_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `order_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `goods_num` varchar(12) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `goods_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `goods_type` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `goods_weight` double NULL DEFAULT NULL,
  `goods_volume` double NULL DEFAULT NULL,
  `goods_quantity` int(11) NOT NULL,
  `goods_price` double NOT NULL,
  `goods_total_price` double NOT NULL,
  `company_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `dept_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` datetime(6) NULL DEFAULT NULL,
  `update_user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `update_time` datetime(6) NULL DEFAULT NULL,
  `del_flag` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`detail_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for t_om_detail_warehouse
-- ----------------------------
DROP TABLE IF EXISTS `t_om_detail_warehouse`;
CREATE TABLE `t_om_detail_warehouse`  (
  `warehouse_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `time` datetime(6) NOT NULL,
  `detail_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `warehouse_local` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `company_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `dept_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` datetime(6) NULL DEFAULT NULL,
  `update_user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `update_time` datetime(6) NULL DEFAULT NULL,
  `del_flag` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`warehouse_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for t_om_order
-- ----------------------------
DROP TABLE IF EXISTS `t_om_order`;
CREATE TABLE `t_om_order`  (
  `order_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `transporter_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `contract_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `transporter` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `transporter_tel` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `get_addr` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `receiver` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `receiver_tel` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `unload_addr` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `transporter_method` int(11) NOT NULL,
  `get_goods_time` datetime(6) NULL DEFAULT NULL,
  `car_start_time` datetime(6) NULL DEFAULT NULL,
  `arriveGoodsTime` datetime(6) NULL DEFAULT NULL,
  `transform` int(11) NULL DEFAULT NULL,
  `ordinary_ticket` int(11) NULL DEFAULT NULL,
  `special_ticket` int(11) NULL DEFAULT NULL,
  `taxpayer_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `taxpayer_num` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `taxpayer_addr` varchar(280) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `taxpayer_tel` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `taxpayer_bank` varchar(280) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `taxpayer_bannk_num` varchar(24) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `send_order` int(11) NULL DEFAULT NULL,
  `transport_order` int(11) NULL DEFAULT NULL,
  `back_order` int(11) NULL DEFAULT NULL,
  `order_amount` double NULL DEFAULT NULL,
  `evaluate_method` int(11) NULL DEFAULT NULL,
  `pay_method` int(11) NULL DEFAULT NULL,
  `pay_status` int(11) NULL DEFAULT NULL,
  `order_status` int(11) NULL DEFAULT NULL,
  `car_demand` varchar(280) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `goods_demand` varchar(280) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `other_demand` varchar(280) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `company_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `dept_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` datetime(6) NULL DEFAULT NULL,
  `update_user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `update_time` datetime(6) NULL DEFAULT NULL,
  `del_flag` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`order_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for t_sys_code
-- ----------------------------
DROP TABLE IF EXISTS `t_sys_code`;
CREATE TABLE `t_sys_code`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` int(11) NOT NULL,
  `value` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `order_number` int(11) NOT NULL,
  `comment` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for t_sys_menu
-- ----------------------------
DROP TABLE IF EXISTS `t_sys_menu`;
CREATE TABLE `t_sys_menu`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `parent_code` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `url` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `icon` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `level` int(11) NULL DEFAULT NULL,
  `is_Enabled_tsc` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `code`(`code`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_sys_menu
-- ----------------------------
INSERT INTO `t_sys_menu` VALUES (1, '物流菜单管理', '1', '0', NULL, '', 0, 0);
INSERT INTO `t_sys_menu` VALUES (2, '系统管理', '101', '1', 'None', '', 1, 1);
INSERT INTO `t_sys_menu` VALUES (3, '用户管理', '10101', '101', '/sm/userManage', 'ico/test.jpeg', 2, 1);
INSERT INTO `t_sys_menu` VALUES (4, '角色管理', '10102', '101', '/sm/roleManage', 'ico/test.jpeg', 2, 1);
INSERT INTO `t_sys_menu` VALUES (5, '菜单管理', '10103', '101', '/sm/menuManage', 'ico/test.jpeg', 2, 1);
INSERT INTO `t_sys_menu` VALUES (6, '结算管理', '102', '1', '', NULL, 1, 1);
INSERT INTO `t_sys_menu` VALUES (7, '结算申请单管理', '10201', '102', '/fm/fmEvaluateEntry', NULL, 2, 1);
INSERT INTO `t_sys_menu` VALUES (8, '信息发布', '103', '1', '', NULL, 1, 1);
INSERT INTO `t_sys_menu` VALUES (9, '货源发布', '10301', '103', '', NULL, 2, 1);
INSERT INTO `t_sys_menu` VALUES (10, '车源发布', '10302', '103', '', NULL, 2, 1);
INSERT INTO `t_sys_menu` VALUES (11, '订单管理', '104', '1', '', NULL, 1, 1);
INSERT INTO `t_sys_menu` VALUES (12, '电子合同', '10401', '104', '', NULL, 2, 1);
INSERT INTO `t_sys_menu` VALUES (13, '订单管理', '10402', '104', '', NULL, 2, 1);
INSERT INTO `t_sys_menu` VALUES (14, '在线结算', '105', '1', '', NULL, 1, 1);
INSERT INTO `t_sys_menu` VALUES (15, '订单结算', '10501', '105', '', NULL, 2, 1);
INSERT INTO `t_sys_menu` VALUES (16, '运费结算', '10502', '105', '', NULL, 2, 1);
INSERT INTO `t_sys_menu` VALUES (17, '咨询投诉', '106', '1', '', NULL, 1, 1);
INSERT INTO `t_sys_menu` VALUES (18, '资讯管理', '10601', '106', '', NULL, 2, 1);
INSERT INTO `t_sys_menu` VALUES (19, '投诉管理', '10602', '106', '', NULL, 2, 1);
INSERT INTO `t_sys_menu` VALUES (20, '在线监控', '107', '1', '', NULL, 1, 1);
INSERT INTO `t_sys_menu` VALUES (21, '订单监控', '10701', '107', '', NULL, 2, 1);
INSERT INTO `t_sys_menu` VALUES (22, '证书监控', '10702', '107', '', NULL, 2, 1);
INSERT INTO `t_sys_menu` VALUES (23, '保险监控', '10703', '107', '', NULL, 2, 1);
INSERT INTO `t_sys_menu` VALUES (24, '车辆监控', '10704', '107', '', NULL, 2, 1);
INSERT INTO `t_sys_menu` VALUES (25, '统计查询', '108', '1', '', NULL, 1, 1);
INSERT INTO `t_sys_menu` VALUES (26, '客户查询', '10801', '108', '', NULL, 2, 1);
INSERT INTO `t_sys_menu` VALUES (27, '订单查询', '10802', '108', '', NULL, 2, 1);
INSERT INTO `t_sys_menu` VALUES (28, '咨询查询', '10803', '108', '', NULL, 2, 1);
INSERT INTO `t_sys_menu` VALUES (29, '数据接口', '109', '1', '', NULL, 1, 1);
INSERT INTO `t_sys_menu` VALUES (30, '交通局数据接口', '10901', '109', '', NULL, 2, 1);
INSERT INTO `t_sys_menu` VALUES (31, '税务局数据接口', '10902', '109', '', NULL, 2, 1);
INSERT INTO `t_sys_menu` VALUES (37, '参数管理', '10104', '101', '', NULL, 2, 1);
INSERT INTO `t_sys_menu` VALUES (38, '车辆管理', '10105', '101', '', NULL, 2, 1);
INSERT INTO `t_sys_menu` VALUES (39, '证书管理', '10106', '101', '', NULL, 2, 1);
INSERT INTO `t_sys_menu` VALUES (40, '流程配置', '10107', '101', '', NULL, 2, 1);
INSERT INTO `t_sys_menu` VALUES (41, '组织机构管理', '10108', '101', '', NULL, 2, 1);

-- ----------------------------
-- Table structure for t_sys_role
-- ----------------------------
DROP TABLE IF EXISTS `t_sys_role`;
CREATE TABLE `t_sys_role`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `note` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_sys_role
-- ----------------------------
INSERT INTO `t_sys_role` VALUES (1, '管理员', 'None');
INSERT INTO `t_sys_role` VALUES (2, '托运人', '');

-- ----------------------------
-- Table structure for t_sys_role_menu
-- ----------------------------
DROP TABLE IF EXISTS `t_sys_role_menu`;
CREATE TABLE `t_sys_role_menu`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `system_menu_id` int(11) NOT NULL,
  `system_role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `t_sys_role_menu_system_menu_id_c3d5d2a9_fk_t_sys_menu_id`(`system_menu_id`) USING BTREE,
  INDEX `t_sys_role_menu_system_role_id_3cb60dd2_fk_t_sys_role_id`(`system_role_id`) USING BTREE,
  CONSTRAINT `t_sys_role_menu_system_menu_id_c3d5d2a9_fk_t_sys_menu_id` FOREIGN KEY (`system_menu_id`) REFERENCES `t_sys_menu` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `t_sys_role_menu_system_role_id_3cb60dd2_fk_t_sys_role_id` FOREIGN KEY (`system_role_id`) REFERENCES `t_sys_role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_sys_role_menu
-- ----------------------------
INSERT INTO `t_sys_role_menu` VALUES (8, 1, 1);
INSERT INTO `t_sys_role_menu` VALUES (9, 2, 1);
INSERT INTO `t_sys_role_menu` VALUES (10, 3, 1);
INSERT INTO `t_sys_role_menu` VALUES (11, 4, 1);
INSERT INTO `t_sys_role_menu` VALUES (12, 5, 1);
INSERT INTO `t_sys_role_menu` VALUES (13, 37, 1);
INSERT INTO `t_sys_role_menu` VALUES (14, 38, 1);
INSERT INTO `t_sys_role_menu` VALUES (15, 39, 1);
INSERT INTO `t_sys_role_menu` VALUES (16, 40, 1);
INSERT INTO `t_sys_role_menu` VALUES (17, 41, 1);
INSERT INTO `t_sys_role_menu` VALUES (18, 6, 1);
INSERT INTO `t_sys_role_menu` VALUES (19, 7, 1);
INSERT INTO `t_sys_role_menu` VALUES (20, 8, 1);
INSERT INTO `t_sys_role_menu` VALUES (21, 9, 1);
INSERT INTO `t_sys_role_menu` VALUES (22, 10, 1);
INSERT INTO `t_sys_role_menu` VALUES (23, 11, 1);
INSERT INTO `t_sys_role_menu` VALUES (24, 12, 1);
INSERT INTO `t_sys_role_menu` VALUES (25, 13, 1);
INSERT INTO `t_sys_role_menu` VALUES (26, 14, 1);
INSERT INTO `t_sys_role_menu` VALUES (27, 15, 1);
INSERT INTO `t_sys_role_menu` VALUES (28, 16, 1);
INSERT INTO `t_sys_role_menu` VALUES (29, 17, 1);
INSERT INTO `t_sys_role_menu` VALUES (30, 18, 1);
INSERT INTO `t_sys_role_menu` VALUES (31, 19, 1);
INSERT INTO `t_sys_role_menu` VALUES (32, 20, 1);
INSERT INTO `t_sys_role_menu` VALUES (33, 21, 1);
INSERT INTO `t_sys_role_menu` VALUES (34, 22, 1);
INSERT INTO `t_sys_role_menu` VALUES (35, 23, 1);
INSERT INTO `t_sys_role_menu` VALUES (36, 24, 1);
INSERT INTO `t_sys_role_menu` VALUES (37, 25, 1);
INSERT INTO `t_sys_role_menu` VALUES (38, 26, 1);
INSERT INTO `t_sys_role_menu` VALUES (39, 27, 1);
INSERT INTO `t_sys_role_menu` VALUES (40, 28, 1);
INSERT INTO `t_sys_role_menu` VALUES (41, 29, 1);
INSERT INTO `t_sys_role_menu` VALUES (42, 30, 1);
INSERT INTO `t_sys_role_menu` VALUES (43, 31, 1);

-- ----------------------------
-- Table structure for t_sys_user
-- ----------------------------
DROP TABLE IF EXISTS `t_sys_user`;
CREATE TABLE `t_sys_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `u_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `u_pwd` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `u_status_tsc` int(11) NOT NULL,
  `apply_date` datetime(6) NULL DEFAULT NULL,
  `approvel_date` datetime(6) NULL DEFAULT NULL,
  `chinese_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `identity_card` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `telephone_number` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `landline` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `wechanumber` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `email` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `appid` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `lastlogin_date` datetime(6) NULL DEFAULT NULL,
  `system_role_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_id`(`user_id`) USING BTREE,
  INDEX `t_sys_user_system_role_id_0fab41fa_fk_t_sys_role_id`(`system_role_id`) USING BTREE,
  CONSTRAINT `t_sys_user_system_role_id_0fab41fa_fk_t_sys_role_id` FOREIGN KEY (`system_role_id`) REFERENCES `t_sys_role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `t_sys_user_user_id_a5dc6041_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_sys_user
-- ----------------------------
INSERT INTO `t_sys_user` VALUES (1, 'lsy', '123456', 1, NULL, NULL, '管理员', 'None', '13066031040', NULL, '123456', '123456789@qq.com', NULL, '2020-12-04 21:32:42.776269', 1, 1);

SET FOREIGN_KEY_CHECKS = 1;
