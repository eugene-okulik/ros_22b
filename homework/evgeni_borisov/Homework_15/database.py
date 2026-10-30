import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor()
#  Создание студента
query_create_student = cursor.execute("INSERT INTO  students (name, second_name, group_id) VALUES (%s, %s, %s)",
                                      ('Yuri',  'Bogdanov', None))
student_id = cursor.lastrowid


# Создание нескольких книг, взятых студентом
query_create_books = cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s), (%s, %s)",
                                    ('War and Peace', student_id, 'History of humanity', student_id))


#  Создание группы
query_create_group = cursor.execute("INSERT INTO `groups` (title, start_date, end_date) "
                                    "VALUES (%s, %s, %s)", ('Automation of testing', '2026-10-01', '2026-12-01'))
group_id = cursor.lastrowid


# Определение студента в группу
query_update_student = cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (group_id, student_id))

#  Создание нескольких учебных предметов
subjects = ['Manual Testing 2026', 'Auto Testing 2026']
subjects_ids = []
for subject in subjects:
    cursor.execute("INSERT INTO subjects (title) VALUES (%s)", (subject,))
    subjects_ids.append(cursor.lastrowid)

subjects_id_dict = dict(zip(subjects, subjects_ids))
subjects_id_list = list(subjects_id_dict.values())
# print(subjects_id_list) для себя


# Создание двух занятий для каждого предмета
'''узнал, что в цикл можно словарь...'''
lessons = ['lesson_55', 'lesson_77', 'lesson_88', 'lessons_98']
subjects_id_for_lessons = [sub_id for sub_id in subjects_ids for _ in range(2)]
lessons_dict = dict(zip(lessons, subjects_id_for_lessons))
# print(lessons_dict) для себя
lessons_id = []
for lesson, subject_id in lessons_dict.items():
    cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", (lesson, subject_id))
    lessons_id.append(cursor.lastrowid)

# Оценки студенту для всех созданных вами занятий
''' наткнулся на дубликаты ключей в массиве и приуныл..но не надолго))'''
marks = ['4', '3', '4', '5']
lessons_marks = list(zip(marks, lessons_id))
# print(lessons_marks) для себя
for value_mark, lesson_id in lessons_marks:
    cursor.execute("INSERT INTO marks (value, lesson_id, student_id) "
                   "VALUES (%s, %s, %s)", (value_mark, lesson_id, student_id))


#  Все оценки студента
all_marks = cursor.execute(
    "SELECT value FROM marks m inner join students s on s.id = m.student_id WHERE s.id = %s", (student_id,))

marks_student = cursor.fetchall()
marks_list = [i for (i,) in marks_student]
print(*marks_list)

# Все книги, которые находятся у студента
all_books_student = cursor.execute("SELECT title FROM books b inner join students s on s.id = b.taken_by_student_id "
                                   "WHERE s.id = %s", (student_id,))

books_student = cursor.fetchall()
print(*[b for (b,) in books_student], sep=', ')

#  Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
all_info_student = cursor.execute("SELECT s.id, s.name, s.second_name, b.title AS book_title, g.title AS group_title, "
                                  "sub.title AS subject_title, l.title AS lesson_title, m.value AS mark_value "
                                  "FROM students s "
                                  "LEFT JOIN `groups` g ON g.id = s.group_id "
                                  "LEFT JOIN books b ON b.taken_by_student_id = s.id "
                                  "LEFT JOIN marks m ON m.student_id = s.id "
                                  "LEFT JOIN lessons l ON l.id = m.lesson_id "
                                  "LEFT JOIN subjects sub ON sub.id = l.subject_id "
                                  "WHERE s.id = %s", (student_id,))
all_info = cursor.fetchall()
for string in all_info:
    print(string)

db.commit()

db.close()
