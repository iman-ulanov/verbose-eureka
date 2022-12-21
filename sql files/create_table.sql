CREATE TABLE payments
(
	id SERIAL PRIMARY KEY,
	course_id INTEGER REFERENCES user_course (id),
	amount INTEGER,
	pay_date DATE
)


INSERT INTO payments
(course_id, amount, pay_date)
VALUES
(get_course_id_by_email('aman@mail.ru'), 15000, '2022-08-15'),
(get_course_id_by_email('aapina@bk.ru'), 55000, '2022-08-05'),
(get_course_id_by_email('spencer@microsoft.com'), 5000, '2022-08-25')


SELECT get_course_id_by_email('aman@mail.ru')

SELECT * FROM payments


SELECT * FROM user_student