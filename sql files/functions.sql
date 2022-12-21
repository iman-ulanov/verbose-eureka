CREATE OR REPLACE FUNCTION get_course_id_by_email(mail VARCHAR(30))
RETURNS BIGINT AS $$
	SELECT id
	FROM user_student
	WHERE user_student.email = mail
$$ LANGUAGE SQL

SELECT * FROM get_course_id_by_email('aapina@bk.ru')



