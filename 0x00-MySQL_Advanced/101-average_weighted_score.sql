-- stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE v_total_weight INT;
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

	SELECT SUM(pro.weight) INTO v_total_weight
        FROM corrections cor
        INNER JOIN projects pro ON pro.id = cor.project_id
        WHERE cor.user_id = user_id;

	UPDATE users
	SET average_score = (SELECT SUM((cor.score * pro.weight) / v_total_weight)
			FROM corrections cor
			INNER JOIN projects pro ON pro.id = cor.project_id
			WHERE cor.user_id = user_id)
	WHERE id = user_id;

	END LOOP;
	CLOSE cur;
END //

DELIMITER ;
