# --------importando sql lite, (para criar banco de dados) (PASSO 1)
import sqlite3 as lite

# Criando Banco de dados (PASSO 2)
con = lite.connect("lista.db")
# apos criacao da lista do banco de dados, tem que executar no comando ("python dbd.py"), ele ira criar um novo arquivo.


# criando tabela dentro do banco de dados (PASSO 3)
"""
with con:
    cur = con.cursor()  # cur=cursos

    cur.execute(
        "CREATE TABLE tarefa(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")
    # Rodar novamente no comando (python dbd.py) para criar tabela (PASSO 4)
"""


"""
    # ---- Alimentando o banco de dados (PASSO 5)
    with con:
        cur = con.cursor()

        query = "INSERT INTO tarefa(nome) VALUES(?)"  # (PASSO 8) add query

        cur.execute("INSERT INTO tarefa(nome) VALUES('assistir one piece')")
        cur.execute(
            "INSERT INTO tarefa(nome) VALUES('encontrar o mundial do palmeiras')")
        cur.execute("INSERT INTO tarefa(nome) VALUES('Estudar as 14 hrs')")
        cur.execute("INSERT INTO tarefa(nome) VALUES('jogar bola')")
    # Rodar novamente no comando (python dbd.py) alimentar a tabela (PASSO 6)
"""

"""
def inserir(i):  # (PASSO 7)add funcao
    # ---- Alimentando o banco de dados
    with con:
        cur = con.cursor()

        query = "INSERT INTO tarefa(nome) VALUES(?)"  # (PASSO 8) add query

        cur.execute("INSERT INTO tarefa(nome) VALUES('assistir one piece')")
        cur.execute(
            "INSERT INTO tarefa(nome) VALUES('encontrar o mundial do palmeiras')")
        cur.execute("INSERT INTO tarefa(nome) VALUES('Estudar as 14 hrs')")
        cur.execute("INSERT INTO tarefa(nome) VALUES('jogar bola')")
"""
# (PASSO 9)


def inserir(i):
    # ---- Alimentando o banco de dados
    with con:
        cur = con.cursor()
        query = "INSERT INTO tarefa(nome) VALUES(?)"
        cur.execute(query, i)


"""
# (PASSO 10)
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM tarefa")
    row=cur.fetchall()
    for r in row:
        print(r)
# Rodar novamente no comando (python dbd.py) para inserir na tabela
"""

# (PASSO 11)


def selecionar():
    lista_tarefa = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM tarefa")
        row = cur.fetchall()
        for r in row:
            lista_tarefa.append(r)
    return lista_tarefa


print(selecionar())

# (PASSO 11) CRIANDO FUNCAO PARA DELETAR
"""
with con:
    cur = con.cursor()
    cur.execute("DELETE FROM tarefa WHERE id=4")
# Rodar novamente no comando (python dbd.py) remover um item, verificando a funcionalidade
"""
# (PASSO 12) CONTINUACAO CRIANDO FUNCAO PARA DELETAR


def deletar(i):
    lista_tarefa = []
    with con:
        cur = con.cursor()
        query = "DELETE FROM tarefa WHERE id=?"
        cur.execute(query, i)

# (PASSO 13) CRIANDO FUNCAO PARA ATUALIZAR
# def deletar(i):
#    lista_tarefa=[]
with con:
    cur = con.cursor()
    cur.execute("UPDATE tarefa SET nome='Comer' WHERE id=3")
# Rodar novamente no comando (python dbd.py) atualizar item 3