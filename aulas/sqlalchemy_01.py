# ============================= IMPORTAÇÃO DE BIBLIOTECAS / CONFIGURAÇÃO  =====================================
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base     # declarativa é super classe
from sqlalchemy.orm import sessionmaker

# criando uma variavel para chamar o motor de conexão
engine = create_engine('mysql+pymysql://root:@localhost:3306/infinity')
#variável = função do motor (<driver>://<usuario>:<senha>@<servidor>:<porta>/<bd>)

# criando uma sessão
Session = sessionmaker(bind=engine)
session = Session()

# ============================================ CLASSES ===================================================
# Super Classe
Classe_base = declarative_base()

# Elementos da tabela
