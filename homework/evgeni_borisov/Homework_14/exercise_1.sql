-- Создание студента
INSERT INTO  students (name, second_name, group_id) VALUES ('Evegi', 'Borisov', NULL)

-- Создание нескольких книг, взятых студентом
INSERT INTO books (title, taken_by_student_id)
VALUES ('Philosophy', 23456), ('The History of Humanity', 23456), ('Do Androids Dream of Electric Sheep?', 23456)

-- Создание группы
INSERT INTO `groups` (title, start_date, end_date) VALUES ('Automation of testing', '2026-10-01', '2026-12-30')

-- Определение студента в группу
UPDATE students SET group_id = 25162
WHERE second_name = 'Borisov'

-- Создание несколько учебных предметов
INSERT INTO subjects (title) VALUES ('Manual Testing 2026'), ('Auto Testing 2026')

-- Создание двух занятий для каждого предмета
INSERT INTO lessons (title, subject_id)
VALUES ('lesson_55', 23775), ('lesson_77', 23775), ('lesson_88', 23776), ('lessons_98', 23776)

-- Оценки студенту для всех созданных вами занятий
INSERT INTO marks (value, lesson_id, student_id)
VALUES ('4', 77376, 23456), ('3', 77377, 23456), ('5', 77378, 23456), ('4', 77379, 23456)

-- Все оценки студента (сделал по фамилии)
SELECT value FROM marks m
inner join students s on s.id = m.student_id
WHERE s.second_name = 'Borisov'

-- Все книги, которые находятся у студента
SELECT title FROM books b
inner join students s on s.id = b.taken_by_student_id
WHERE s.second_name = 'Borisov'

-- Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
SELECT s.id, s.name, s.second_name,
	   b.title AS book_title,
	   g.title AS group_title,
	   sub.title AS subject_title,
	   l.title AS lesson_title,
       m.value AS mark_value
FROM students s
LEFT JOIN `groups` g ON g.id = s.group_id
LEFT JOIN books b ON b.taken_by_student_id = s.id
LEFT JOIN marks m ON m.student_id = s.id
LEFT JOIN lessons l ON l.id = m.lesson_id
LEFT JOIN subjects sub ON sub.id = l.subject_id
WHERE s.second_name = 'Borisov';
