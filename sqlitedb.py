import sqlite3

connection = sqlite3.connect("avg_grades.db")
cursor = connection.cursor()
print("Connected to database")


def create_tables():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS STUDENT_INFO ("
        "STUDENT_NO INT NOT NULL PRIMARY KEY,"
        "STUDENT_NAME VARCHAR(255) NOT NULL, AVERAGE INT)"
    )
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS STUDENT_GRADES ("
        "STUDENT_NO INT NOT NULL, LESSON TEXT NOT NULL,"
        "COEFFICIENT INT NOT NULL,"
        "GRADE INT NOT NULL, TIME INT NOT NULL,"
        "FOREIGN KEY (STUDENT_NO) REFERENCES STUDENT_INFO(STUDENT_NO))"
    )
    # cursor.execute(
    #     "CREATE TABLE IF NOT EXISTS STUDENT_AVERAGE ("
    #     "STUDENT_NO INT NOT NULL, AVERAGE INT,"
    #     "FOREIGN KEY (STUDENT_NO) REFERENCES STUDENT_INFO(STUDENT_NO))"
    # )


create_tables()


def close():
    cursor.close()
    connection.close()
