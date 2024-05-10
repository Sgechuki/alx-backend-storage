-- creates a stored procedure AddBonus that adds a new correction for a student
DELIMITER //

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
	DECLARE v_name_exist INT;
	DECLARE v_project_id INT;

	SELECT COUNT(*) INTO v_name_exist
	FROM projects
	WHERE name = project_name;

	IF v_name_exist = 0 THEN
		INSERT INTO projects (name)
		VALUES (project_name);
	END IF;
	SELECT id INTO v_project_id
	FROM projects
	WHERE name = project_name;

	INSERT INTO corrections (user_id, project_id, score)
	VALUES (user_id, v_project_id, score);
END //
DELIMITER ;
