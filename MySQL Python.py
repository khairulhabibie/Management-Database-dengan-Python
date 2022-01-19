from mysql.connector import connect

# 01 - membuat koneksi dengan database
db = connect(
    host = "localhost",
    user = "root",
    password = "sayaBelajar"
)
print(db)

# 02 - membuat database
cursor_db = db.cursor() 
cursor_db.execute("DROP DATABASE IF EXISTS school")
cursor_db.execute("CREATE DATABASE IF NOT EXISTS school")
cursor_db.close()
db.close()
    # membuat koneksi baru
db = connect(
  host="localhost",
  user="root",
  password="sayaBelajar",
  database="school"
)

# 03 - membuat atribut table
cursor_db = db.cursor() 
cursor_db.execute(
    '''CREATE Table students(
        id_siswa int primary key auto_increment,
        nama VARCHAR(50) not null,
        id_kelas int not null,
        tahun_masuk int not null
    )'''
)

# 04 - memasukkan data kedalam table
    # Cara 1
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

# cara 2
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
    # menutup database
cursor_db.close()
db.close()
'''

# 05 - melihat data di dalam table
query = '''select * from students'''
cursor_db.execute(query)
data = cursor_db.fetchall()

#Untuk menampilkan kita bisa menggunakan for loop,
for row in data:
    print(row)

# Menutup database
cursor_db.close()
db.close()