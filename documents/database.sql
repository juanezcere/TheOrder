CREATE DATABASE IF NOT EXISTS TheOrder;
USE TheOrder;

DELIMITER //
CREATE FUNCTION generate_id()
RETURNS VARCHAR(32)
BEGIN
  DECLARE id VARCHAR(32);
  SELECT REPLACE(UUID(), '-', '') INTO id;
  RETURN id;
END; //
DELIMITER ;

CREATE TABLE IF NOT EXISTS `trucks` (
  `truck_id` VARCHAR(32) PRIMARY KEY,
  `truck_name` VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS `foods` (
  `food_id` VARCHAR(32) PRIMARY KEY,
  `food_name` VARCHAR(255) NOT NULL,
  `food_value` FLOAT DEFAULT 0.0,
  `truck_id` VARCHAR(32) NOT NULL,
  CONSTRAINT `foods_trucks_truck_id_foreign` FOREIGN KEY (`truck_id`) REFERENCES `trucks` (`truck_id`)
);

CREATE TABLE IF NOT EXISTS `orders` (
  `order_id` VARCHAR(32) PRIMARY KEY,
  `food_id` VARCHAR(32) NOT NULL,
  `customer` VARCHAR(255) NOT NULL,
  `order_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `where_eat` BOOLEAN DEFAULT FALSE,
  `status` TINYINT UNSIGNED DEFAULT 0,
  `food_quantity` TINYINT UNSIGNED DEFAULT 1,
  `observations` VARCHAR(255) DEFAULT '',
  CONSTRAINT `foods_orders_food_id_foreign` FOREIGN KEY (`food_id`) REFERENCES `foods` (`food_id`)
);

-- To create new trucks
INSERT INTO TheOrder.`trucks` (`truck_id`, `truck_name`)
SELECT generate_id(), 'La hamburgueseria' UNION ALL
SELECT generate_id(), 'Super Papas';

-- To create new foods
INSERT INTO TheOrder.`foods` (`food_id`, `food_name`, `food_value`, `truck_id`)
SELECT generate_id(), 'Hamburguesa', 5, truck_id FROM `trucks` WHERE `truck_name` = 'La hamburgueseria' UNION ALL
SELECT generate_id(), 'Salchipapas', 3, truck_id FROM `trucks` WHERE `truck_name` = 'Super Papas' UNION ALL
SELECT generate_id(), 'Salchipapas Grande', 4.5, truck_id FROM `trucks` WHERE `truck_name` = 'Super Papas' UNION ALL
SELECT generate_id(), 'Gaseosa', 1, truck_id FROM `trucks` WHERE `truck_name` = 'La hamburgueseria' UNION ALL
SELECT generate_id(), 'Tacos', 10, truck_id FROM `trucks` WHERE `truck_name` = 'La hamburgueseria';
