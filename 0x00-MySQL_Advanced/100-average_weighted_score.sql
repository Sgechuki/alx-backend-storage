-- creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE v_total_weight INT;

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
END //

DELIMITER ;
