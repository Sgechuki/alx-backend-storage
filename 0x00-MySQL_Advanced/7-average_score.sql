-- stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE v_avg_score DECIMAL;

	SELECT AVG(score) INTO v_avg_score
	FROM corrections cor
	WHERE cor.user_id = user_id;

	UPDATE users
	SET average_score = v_avg_score
	WHERE id = user_id;
END //
DELIMITER ;
