'''#Classe
class Disciplina:
    def __init__(self):
        self.codigo = 0
        self.nome = ""
        self.ch = 0
        self.professor = ""
        self.chr = 0.0

#Um objeto é uma instância de uma classe, sendo a instância o fato de obter os registros da classe no qual gera um cadastro/registro propriamente dito, ou seja, a classe é o molde e o objeto o que existe

#Objeto
d1 = Disciplina()
d1.codigo = 5
d1.nome = "Algoritmos"
d1.ch = 160
'''
#atividade bd disciplina
'cria banco de dados e tabela'
import mysql.connector


class Disciplina:
    def __init__(self):
        self.codigo = 0
        self.nome = ""
        self.ch = 0
        self.professor = ""
        self.chr = 0.0

def salvar(d):
    banco = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='algoritmos'
    )

    cursor = banco.cursor()
    
    sql = "INSERT INTO disciplina VALUES (%s, %s, %s, %s, %s)"
    valores = (None, d.nome, d.ch, d.professor, d.chr)

    cursor.execute(sql, valores)
    banco.commit()

    d.codigo = cursor.lastrowid

    cursor.close()
    banco.close()

def lerDados():
    banco = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='algoritmos'
    )

    cursor = banco.cursor()

    sql = "SELECT * from disciplina"

    cursor.execute(sql)

#converte os dados obtidos na tabela para um veetor e guarda na variável
    dados = cursor.fetchall()

    x = [Disciplina()] * cursor.rowcount

    i = 0
    for linha in dados:

        d = Disciplina()

        d.codigo = linha[0]
        d.nome = linha[1]
        d.ch = linha[2]
        d.professor = linha[3]
        d.chr = linha[4] 

        x[i] = d

        i += 1

    return x

disc = Disciplina()
disc.nome = input("Nome:")
disc.ch = int(input("CH:"))
disc.professor = input("Professor:")
disc.chr = (disc.ch * 50 / 60)

salvar(disc)

disciplinas = lerDados()

print("====Disciplinar====")
for i in range(0, len(disciplinas)):
    print("Código:", disciplinas[i].codigo)
    print("Nome:", disciplinas[i].nome)
    print("CH:", disciplinas[i].ch)
    print("Professor:", disciplinas[i].professor)
    print("CHR:", disciplinas[i].chr)

print("")

