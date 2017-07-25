import sqlite3
import ctypes
import time

conn = sqlite3.connect('CRUD.db', timeout = 10)
c = conn.cursor()

#Create
def criarTabela(sql):
    try:
        c.execute('%s' %sql)
        ctypes.windll.user32.MessageBoxW(None, "Tabela criada com sucesso!", "Parabéns!", 0)
    except sqlite3.Error as e:
        ctypes.windll.user32.MessageBoxW(None, "Erro: %s" % e, "Erro ao usar o criar tabela", 0)

#Insert
def inserir(sql):
    try:
        c.execute('%s' %sql)
        conn.commit()
        ctypes.windll.user32.MessageBoxW(None, "Dado(s) inserido(s) com sucesso!", "Parabéns!", 0)
    except sqlite3.Error as e:
        ctypes.windll.user32.MessageBoxW(None, "Erro: %s" % e, "Erro ao usar o INSERT", 0)

#Select
def select(sql):
    try:
        c.execute('%s' %sql)
        for linha in c.fetchall():
            print(linha)
    except sqlite3.Error as e:
        ctypes.windll.user32.MessageBoxW(None , "Erro: %s" %e, "Erro ao usar o SELECT", 0)

#Select
def update(sql):
    try:
        c.execute(sql)
        conn.commit()
        ctypes.windll.user32.MessageBoxW(None, "Tupla atualizada com sucesso!", "Parabéns!", 0)
    except sqlite3.Error as e:
        ctypes.windll.user32.MessageBoxW(None, "Erro: %s" % e, "Erro ao usar o UPDATE", 0)

#Delete
def remove(sql):
    try:
        c.execute(sql)
        conn.commit()
        ctypes.windll.user32.MessageBoxW(None, "Tupla removida com sucesso!", "Parabéns!", 0)
    except sqlite3.Error as e:
        ctypes.windll.user32.MessageBoxW(None , "Erro: %s" %e, "Erro ao usar o REMOVE", 0)