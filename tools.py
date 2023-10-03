import sqlitedb as db

from datetime import datetime

now = datetime.now()
creation = now.strftime("%d/%m/%Y %H:%M:%S")


def crud_student(_splitted_data):
    insert_query_student = ("INSERT INTO STUDENT_INFO (STUDENT_NO, STUDENT_NAME) "
                            "VALUES (?, ?)")
    db.cursor.execute(insert_query_student, (_splitted_data[1], _splitted_data[2]))

    db.connection.commit()


def crud_grades(_splitted_data):
    # try:
        insert_query_grades = ("INSERT INTO STUDENT_GRADES (STUDENT_NO, LESSON, COEFFICIENT,"
                               " GRADE, TIME) VALUES (?, ?, ?, ?, ?)")
        db.cursor.execute(insert_query_grades, (_splitted_data[1], _splitted_data[3],
                                                len(_splitted_data[4]), _splitted_data[5], creation))

        average_query = "SELECT SUM(GRADE * COEFFICIENT) / SUM(COEFFICIENT) FROM STUDENT_GRADES WHERE STUDENT_NO = ?"
        db.cursor.execute(average_query, (_splitted_data[1],))

        average = db.cursor.fetchone()[0]
        print(average)
        update_average_query = "UPDATE STUDENT_INFO SET AVERAGE = ? WHERE STUDENT_NO = ?"
        db.cursor.execute(update_average_query, (average, _splitted_data[1]))

    # except:
    #     insert_average = "INSERT INTO STUDENT_AVERAGE (STUDENT_NO, AVERAGE) VALUES (?, ?)"
    #     db.cursor.execute(insert_average, (_splitted_data[1], _splitted_data[5] ))
        db.connection.commit()


def print_info(student_no):

    db.cursor.execute("SELECT STUDENT_NO FROM STUDENT_INFO WHERE STUDENT_NO = ?", (student_no,))
    check = db.cursor.fetchone()

    if check:

        db.cursor.execute(
            "SELECT i.STUDENT_NO, i.STUDENT_NAME, i.AVERAGE, g.LESSON, g.COEFFICIENT, g.GRADE, g.TIME "
            "FROM STUDENT_INFO AS i "
            "JOIN STUDENT_GRADES AS g ON i.STUDENT_NO = g.STUDENT_NO "
            "WHERE i.STUDENT_NO = ?",
            (student_no,)
        )

        data = db.cursor.fetchall()
        for row in data:
            print("Student No:", row[0])
            print("Student Name:", row[1])
            print("Average:", row[2])

    else:
        print(f"Student with Student No {student_no} does not exist in the STUDENT_GRADES table")

    db.connection.commit()
def print_grades(student_no):

    db.cursor.execute(
        "SELECT i.STUDENT_NO, i.STUDENT_NAME, i.AVERAGE, g.LESSON, g.COEFFICIENT, g.GRADE, g.TIME "
        "FROM STUDENT_INFO AS i "
        "JOIN STUDENT_GRADES AS g ON i.STUDENT_NO = g.STUDENT_NO "
        "WHERE i.STUDENT_NO = ?",
        (student_no,)
    )

    data = db.cursor.fetchall()
    for row in data:
        print("Grades:")
        print("Student No:", row[0])
        print("Lesson:", row[3])
        print("Coefficient:", row[4])
        print("Grade:", row[5])
        print("Time:", row[6])

    db.connection.commit()

