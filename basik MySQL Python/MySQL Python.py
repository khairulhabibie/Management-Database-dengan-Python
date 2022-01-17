from mysql.connector import connect

# 01 - make a connection to the database
db = connect(
    host = "localhost",
    user = "root",
    password = "sayaBelajar"
)
print(db)

# 02 - make a database
cursor_db = db.cursor() 
cursor_db.execute("DROP DATABASE IF EXISTS school")
cursor_db.execute("CREATE DATABASE IF NOT EXISTS school")
cursor_db.close()
db.close()
    # make a new connection
db = connect(
  host="localhost",
  user="root",
  password="sayaBelajar",
  database="school"
)

# 03 - create a table attribute
cursor_db = db.cursor() 
cursor_db.execute(
    '''CREATE Table students(
        id_siswa int primary key auto_increment,
        nama VARCHAR(50) not null,
        id_kelas int not null,
        tahun_masuk int not null
    )'''
)

# 04 - insert data to table
    # side 1
query = '''
INSERT INTO students (nama, id_kelas, tahun_masuk)
VALUES
    ('shiroe', 21, 2012),
    ('akatsuki', 21, 2012),
    ('naotsugu', 21, 2012),
    ('minori', 13, 2013),
    ('touya', 13, 2013),
    ('kanami', 31, 2011)
'''
cursor_db.execute(query)
db.commit()

    # side
input_list = [

    ('shiroe', 21, 2012),
    ('akatsuki', 21, 2012),
    ('naotsugu', 21, 2012),
    ('minori', 13, 2013),
    ('touya', 13, 2013),
    ('kanami', 31, 2011)

]

for data in input_list:

    query = '''

    INSERT INTO students (nama, id_kelas, tahun_masuk)

    VALUES (%s, %s, %s)

    '''

    cursor_db.execute(query, data)

db.commit()

'''
    # close cusor and database
cursor_db.close()
db.close()
'''

# 05 - show data in database
query = '''select * from students'''
cursor_db.execute(query)
data = cursor_db.fetchall()

    # using loop
for row in data:
    print(row)

    # close database
cursor_db.close()
db.close()
