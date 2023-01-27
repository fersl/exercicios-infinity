import mysql.connector
import pandas as pd

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'loja'
)

cursor = conexao.cursor()

def inserirProduto():
    novo_nome_produto = input('Digite o nome do produto: ')
    novo_preco_produto = float(input('Digite o preço do produto: '))

    comandoSQL = f'INSERT INTO produtos (nome_produto, preco_produto)' \
                 f'VALUES ("{novo_nome_produto}", "{novo_preco_produto}")'

    cursor.execute(comandoSQL)
    print('Produto inserido com sucesso.')
    conexao.commit()

def consultarProduto():
    consulta_id_produto = int(input('Digite o ID do produto: '))

    comandoSQL = f'SELECT * FROM produtos WHERE id_produto={consulta_id_produto}'
    cursor.execute(comandoSQL)
    resultado = cursor.fetchall()
    dfResultado = pd.DataFrame(resultado)
    print(dfResultado)

def listarProdutos():
    comandoSQL = f'SELECT * FROM produtos'
    cursor.execute(comandoSQL)
    resultado = cursor.fetchall()
    dfResultado = pd.DataFrame(resultado)
    print(dfResultado)

def alterarProduto():
    consulta_id_produto = int(input('Digite o ID do produto: '))

    # novo_nome = input('Digite o novo nome do produto: ')
    novo_preco = int(input('Digite o novo preço do produto: '))
    comandoSQL = f'UPDATE produtos' \
                 f'SET preco_produto = "{novo_preco}"' \
                 f'WHERE id_produto = "{consulta_id_produto}"'

    cursor.execute(comandoSQL)
    print('Produto alterado com sucesso.')
    conexao.commit()

def deletarProduto():
    id_produto = int(input('Digite a ID do produto: '))
    comandoSQL = f'DELETE FROM produtos' \
                 f'WHERE id_produto = "{id_produto}"'

    cursor.execute(comandoSQL)
    print('Produto deletado com sucesso.')
    conexao.commit()


while True:
    menu = int(input(f"{' MENU DA LOJA ':=^50}\n"
                 f"[1] Cadastrar novo produto\n"
                 f"[2] Listar produtos\n"
                 f"[3] Consultar produto por id\n"
                 f"[4] Alterar produto\n"
                 f"[5] Deletar produto\n"
                 f"[6] Sair\n"
                 f"{'':=^50}\n"
                 f"Digite o número da opção desejada: "))

    match menu:
        case 1: inserirProduto()
        case 2: listarProdutos()
        case 3: consultarProduto()
        case 4: alterarProduto()
        case 5: deletarProduto()
        case 6: break
        case _: print('Opção Inválida. Tente novamente.')

