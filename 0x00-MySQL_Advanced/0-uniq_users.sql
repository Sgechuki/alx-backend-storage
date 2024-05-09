-- 0 We are all unique
-- creates a table users
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) UNIQUE,
	name VARCHAR(255),
	PRIMARY KEY (id)
	);

