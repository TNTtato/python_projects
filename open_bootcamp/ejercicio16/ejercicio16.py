from distutils.log import error
import sqlite3

def main():
  alumnos = {
    1: ['Gustavo', 'Penaranda'],
    2: ['Angie', 'Chaya'],
    3: ['Erika', 'Penaranda'],
    4: ['Olaride', 'Cabrea'],
    5: ['Milo', 'Cabrera'],
    6: ['Julieth', 'Castro'],
    7: ['Yamil', 'Chaya'],
    8: ['Rocky', 'Penaranda Chaya']
  }
  conn = create_conn('./open_bootcamp/ejercicio16/test.db')
  query_create_table = '''
  CREATE TABLE Alumnos(
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL
  );
  '''
  create_table(conn, query_create_table)
  for id, names in alumnos.items():
    query = f'INSERT INTO Alumnos VALUES({id}, "{names[0]}", "{names[1]}")'
    insert_reg(conn, query)
  
  alm = search(conn,'Gustavo')
  print('ID | name | last name', alm, sep='\n')

def create_conn(data_base):
  try:
    return sqlite3.connect(data_base)
  except sqlite3.Error:
    print('Se ha producido un error:', error)

def create_table(conn, query):
  cur = conn.cursor()
  cur.execute(query)
  conn.commit()

def insert_reg(conn, query):
  cur = conn.cursor()
  cur.execute(query)
  conn.commit()

def search(conn, name):
  query = f'SELECT * FROM Alumnos WHERE nombre="{name}"'
  cur = conn.cursor()
  cur.execute(query)
  rows = cur.fetchall()
  return rows[0]

if __name__ == '__main__':
  main()