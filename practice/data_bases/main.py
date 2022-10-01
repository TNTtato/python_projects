import sqlite3
import getpass

def main():
  create_user(4, 'olaride', 'lostatos')

def main2():
  username = input('Username: ')
  password = getpass.getpass('Password: ')
  if verify_credentials(username, password):
    print('Access granted')
  else:
    print('Access denied')

def verify_credentials(username, password):
  conn = sqlite3.connect('appdata.db')
  cur = conn.cursor()

  query = f'SELECT id FROM users WHERE username="{username}" AND password="{password}"'
  print('Executing query:', query)
  rows = cur.execute(query)
  data = rows.fetchone()
  print('Data is:', data)
  
  cur.close()

  conn.close()

  return data

def create_user(id, username, password):
  conn = sqlite3.connect('appdata.db')
  cur = conn.cursor()

  query = f'INSERT INTO users(id, username, password) VALUES({id}, "{username}", "{password}")'
  print('Executing query:', query)
  rows = cur.execute(query)
  print('Data is:', rows)
  conn.commit()
  cur.close()

  conn.close()

if __name__ == '__main__':
  main()

