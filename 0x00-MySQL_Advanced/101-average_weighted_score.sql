-- stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE user_id INT;
	DECLARE done INT DEFAULT 0;
	DECLARE cur CURSOR FOR SELECT id FROM users;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
	
	OPEN cur;
	user_loop: LOOP
	FETCH cur INTO user_id;
	IF done = 1 THEN
		LEAVE user_loop;
	END IF;

	CALL ComputeAverageWeightedScoreForUser(user_id);

	END LOOP;
	CLOSE cur;
END //

DELIMITER ;
