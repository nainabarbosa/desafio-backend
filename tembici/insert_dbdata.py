import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn
 
def create_category(conn, category):
    """
    Create a new category
    :param conn:
    :param category:
    :return:
    """
    sql = '''INSERT INTO viagem_category (classificacao) VALUES(?);'''
    cur = conn.cursor()
    cur.execute(sql, category)
    return cur.lastrowid

def create_trip(conn, trip):
    """
    Create a new category
    :param conn:
    :param category:
    :return:
    """
    sql = '''INSERT INTO viagem_trip (data_inicio, data_fim, classificacao_id, nota) VALUES(?, ?, ?, ?);'''
    cur = conn.cursor()
    cur.execute(sql, trip)
    return cur.lastrowid
 
def main():
    database = r"/home/janaina/projects/tembici/db.sqlite3"
 
    # create a database connection
    conn = create_connection(database)
    with conn:

        # category
        category_1 = ('Trabalho',)
        category_2 = ('Atividade física',)
        category_3 = ('Lazer',)
        category_4 = ('Deslocamento',)

        # trip
        trip_1 = ('2020-02-20T12:10:00Z', '2020-02-20T12:20:00Z', 1, 3)
        trip_2 = ('2020-02-21T12:10:00Z', '2020-02-20T12:15:00Z', 4, None)

        create_category(conn, category_1)
        create_category(conn, category_2)
        create_category(conn, category_3)
        create_category(conn, category_4)

        create_trip(conn, trip_1)
        create_trip(conn, trip_2)

if __name__ == '__main__':
    # main()
    database = r"/home/janaina/projects/tembici/db.sqlite3"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM viagem_trip")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)