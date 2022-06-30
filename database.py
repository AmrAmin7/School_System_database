import sqlite3



def create_students_tables():
    conn = sqlite3.connect('School_database.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE Students(
        id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        first_name text,
        last_name text,
        grade integer,
        FOREIGN KEY (grade) REFERENCES Lessons (grade))""")

    conn.commit()
    conn.close()

def add_student(id,first_name,last_name,grade):
    conn = sqlite3.connect('School_database.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO Students VALUES (?,?, ?, ? )",(id,first_name,last_name,grade))
    
    conn.commit()
    conn.close()

def get_students():
    conn = sqlite3.connect('School_database.db')
    c = conn.cursor()
    c.execute("""SELECT id,first_name,last_name,grade,lecture,lesson_name FROM Lessons INNER JOIN Students USING (grade)""")
    items=c.fetchall()
    for item in items:
        print(item) 

    conn.commit()
    conn.close()
    
    
    
def get_students_by_grade(grade):
    conn = sqlite3.connect('School_database.db')
    c = conn.cursor()
    
    c.execute("SELECT * FROM Students WHERE grade = (?)", (grade,))
    students=c.fetchall()
    
    for student in students:
        print(student)
        
    conn.commit()
    conn.close()


def update_grade_students(grade,id):  
    conn = sqlite3.connect('School_database.db')
    c = conn.cursor()
 
    c.execute("UPDATE Students SET grade= (?) WHERE id= (?)",(grade,id))
    
    conn.commit()
    conn.close()
    
    
def delete_students(id):  
    conn = sqlite3.connect('School_database.db')
    c = conn.cursor()
    
    c.execute("DELETE FROM Students WHERE id = (?)", id)
    
    conn.commit()
    conn.close()

