from uuid import uuid4
import sqlite3

def Conn():
    return sqlite3.connect('banco.db')

def create_table():
    conn = Conn()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Produtos(
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            quantidade TEXT,
            valor TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert(name, quantidade, valor):
    conn = Conn()
    cursor = conn.cursor()
    id = str(uuid4())
    cursor.execute('''
        INSERT INTO Produtos(id, name, quantidade, valor)
        VALUES (?, ?, ?, ?)
    ''', (id, name, quantidade, valor))
    conn.commit()
    conn.close()
    return select(id)

def select_all():
    conn = Conn()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Produtos
    ''')
    data = cursor.fetchall()
    conn.close()
    return data

def select(id = ''):
    conn = Conn()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Produtos WHERE id = ? or name = ?
    ''', (id, id))
    data = cursor.fetchone()
    conn.close()
    return data

def update(name, quantidade, valor, id = ''):
    conn = Conn()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Produtos SET name = ?, quantidade = ?, valor = ? WHERE id = ?
    ''', (name, quantidade, valor, id))
    conn.commit()
    conn.close()

def delete(id = ''):
    conn = Conn()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM Produtos WHERE id = ? or name = ?
    ''', (id, id))
    conn.commit()
    conn.close()