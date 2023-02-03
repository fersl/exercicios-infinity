
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

# criando a variável para receber a conexão ***ANTES DE RODAR O PROGRAMA, VERIFICAR O CAMINHO AO BANCO***
engine = create_engine('mysql+pymysql://root:admin@localhost:3306/loja319')
print(engine)

# criando super classe através do 'declarative_base'
Base = declarative_base()

# criando a variável da sessão
Sessao = sessionmaker(bind=engine)
sessao = Sessao()


# criando Entidades(Classe)
class Usuario(Base):
    # criando a tabela
    __tablename__ = 'usuario'

    # criando os campos da tabela
    nome_usuario = Column(String, primary_key=True)
    endereco_usuario = Column(String, nullable=False)
    idade_usuario = Column(Integer, nullable=False)

    # método para exibir os dados
    def __repr__(self):
        return f'Nome: {self.nome_usuario}, ' \
               f'Endereço: {self.endereco_usuario}, ' \
               f'Idade: {self.idade_usuario}\n'


# --------------------------- INÍCIO -------------------------------
# criando SQL

while True:
    opcao = int(input('------------- BANCO DE DADOS -------------\n'
                      'Para manipular o BD escolha uma opção:\n'
                      '[1] - VISUALIZAR REGISTROS\n'
                      '[2] - INSERIR UM REGISTRO\n'
                      '[3] - EDITAR UM REGISTRO\n'
                      '[4] - EXCLUIR UM REGISTRO\n'
                      '[5] - SAIR DO SISTEMA\n'))
    match opcao:
        case 1:
            # consultando registros(select)
            banco_loja_in_select = sessao.query(Usuario).all()
            for contador_linhas in banco_loja_in_select:
                print(contador_linhas, end='')

        case 2:
            # inserindo registro(insert)
            nome = str(input('Informe o nome: ')).title()
            endereco = str(input('Informe o endereço: '))
            idade = int(input('Informe a idade: '))

            print('Confira os dados antes de continuar!')
            inserir = str(input('Confirma o novo cadastro? [S/N]: ')).upper()

            if inserir[0] == 'S':
                banco_loja_in_insert = Usuario(nome_usuario=nome,
                                               endereco_usuario=endereco,
                                               idade_usuario=idade)
                sessao.add(banco_loja_in_insert)
        case 3:
            nome_registro = str(input('Informe o nome do registro a ser editado: ')).title()
            banco_loja_in_select = sessao.query(Usuario).all()

            for nome in banco_loja_in_select:
                if nome_registro in nome.nome_usuario:
                    editar_registro = str(input('Informe o campo a ser editado [Nome, Endereço ou Idade]: ')).title()

                    if editar_registro == 'Nome':
                        # editando um registro pelo nome (update)
                        novo_nome = str(input('Informe o novo nome: '))
                        sessao.query(Usuario).filter(Usuario.nome_usuario == nome_registro).update({'nome_usuario': novo_nome})

                    elif editar_registro == 'Endereço':
                        # editando um registro pelo endereço (update)
                        novo_endereco = str(input('Informe o novo endereço: '))
                        Sessao.query(Usuario).filter(Usuario.nome_usuario == nome_registro).update(
                            {'endereco_usuario': novo_endereco})

                    elif editar_registro == 'Idade':
                        # editando um registro pela idade (update)
                        nova_idade = str(input('Informe a nova idade: '))
                        Sessao.query(Usuario).filter(Usuario.nome_usuario == nome_registro).update(
                            {'idade_usuario': nova_idade})
                    else:
                        print('Campo não encontrado!')

        case 4:
            apagar_registro = str(input('Informe o nome do registro a ser excluído: '))
            # apagando um registro (delete)
            apagar = str(input('Tem certeza que deseja excluir algum registro [S/N]: ')).upper()
            if apagar[0] == 'S':
                Sessao.query(Usuario).filter(Usuario.nome_usuario == apagar_registro).delete()

        case 5:
            print('SAINDO DO SISTEMA...')
            break

        case _:
            print('OPÇÃO INVÁLIDA!')

    # aplica as modificações ao banco
sessao.commit()  # MODIFICAR - UPDATE | INSERT | DELETE
sessao.close()
