CREATE TABLE `user` (
  `id` BINARY(16) PRIMARY KEY NOT NULL,
  `first_name` varchar(256) NOT NULL,
  `second_name` varchar(256) NOT NULL,
  `password_hash` char(60) NOT NULL,
  `age` int,
  `biography` varchar(256),
  `city` varchar(256)
);
