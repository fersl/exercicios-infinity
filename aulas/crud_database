import mysql.connector
import pandas as pd

conexao = mysql.connector.connect(
    # servidor - usuário - senha - bancoDeDados
    host= 'localhost',
    user = 'root',
    password = '',      # password do banco de dados
    database = 'infinity'
)

cursor = conexao.cursor()   # responsável por realizar as alterações no banco


# CRUD create - INSERT
def inserirAluno():
    novo_aluno = input('Digite o nome do aluno: ')
    novo_curso = input('Digite o curso do aluno: ')

    comandoSQL = f'INSERT INTO aluno(nome_aluno, curso_aluno) VALUES ("{novo_aluno}", "{novo_curso}")'
    cursor.execute(comandoSQL)
    conexao.commit()
    print(f"Aluno {novo_aluno} inserido com sucesso.")

# CRUD READ - SELECT
def consultarTodos():
    comandoSQL = f'SELECT * FROM aluno'
    cursor.execute(comandoSQL)
    resultadoDaConsulta = cursor.fetchall()
    df = pd.DataFrame(resultadoDaConsulta)
    print(df)

def consultarPorID():
    id_aluno = input('Digite a id do aluno a ser pesquisado: ')
    comandoSQL = f"SELECT nome_aluno FROM aluno WHERE id_aluno='{id_aluno}' "
    cursor.execute(comandoSQL)
    resultadoDaConsulta = cursor.fetchall()
    print(resultadoDaConsulta)


# CRUD UPDATE - UPDATE
def alterarCursoDoAluno():
    nome_aluno = input('Digite o nome do aluno a ser alterado: ')
    novo_curso = input('Digite o novo curso do aluno: ')

    comandoSQL = f"UPDATE aluno " \
                 f"SET curso_aluno = '{novo_curso}'" \
                 f"WHERE nome_aluno = '{nome_aluno}' "

    cursor.execute(comandoSQL)
    conexao.commit()
    print(f"Aluno {nome_aluno} alterado com sucesso.")


# CRUD DELETE - DELETE
def deletarAluno():
    nome_aluno = input("Digite o nome do aluno a ser deletado: ")

    comandoSQL = f"DELETE FROM aluno WHERE nome_aluno = '{nome_aluno}' "
    cursor.execute(comandoSQL)
    conexao.commit()
    print(f"Aluno {nome_aluno} deletado com sucesso.")

def printarMenu():
    print(f"{'MENU':-^50}")
    print(f"(1) INSERIR ALUNO \n"
          f"(2) CONSULTAR ALUNO \n"
          f"(3) CONSULTAR TODOS OS ALUNOS \n"
          f"(4) ALTERAR ALUNO \n"
          f"(5) DELETAR ALUNO \n"
          f"(6) SAIR")
    print("-" * 50)

def rodarMenu():
    flag_menu = True
    while flag_menu:
        printarMenu()
        opcao = int(input('Digite o número da opção desejada: '))

        match opcao:
            case 1: inserirAluno()
            case 2: consultarPorID()
            case 3: consultarTodos()
            case 4: alterarCursoDoAluno()
            case 5: deletarAluno()
            case 6:
                flag_menu = False
                print("Sistema Encerrado.")
            case _: print("Opção Inválida. Tente Novamente.")

# EXECUTANDO AS FUNÇÕES
# inserirAluno()
# alterarCursoDoAluno()
# consultarID()
# deletarAluno()
rodarMenu()
