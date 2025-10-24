from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

# alembic -> migração do banco de dados
# Mudar o link do alembic.ini para o meu bancos de dados

# No deplpoy o link deve ser do banco de dados
# Cria a conexão do banco
db = create_engine("sqlite:///database/banco.db")

# Cria a base do banco de dados
Base = declarative_base()

# Cria as classes/tabelas do banco 
# Usuario, Pedido, ItemPedido

# Tradução de uma classe para tabela, Usuario é subclasse de Base
class Usuario(Base):
    __tablename__ = "usuarios" # Nome da tabela

    ## Comandos SQL
    id = Column("id", Integer, primary_key=True, autoincrement=True) # A chave primária deve ser um valor único
    nome = Column("nome", String)
    email = Column("email", String, nullable=False) # Impede que qualquer parte do código crie um Usuario sem esse parâmetro
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False): # Padrões, podem não ser passados
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

class Pedido(Base):
    __tablename__ = "pedidos"

    # STATUS_PEDIDOS = (
    #     ("PENDENTE","PENDENTE"),
    #     ("CANCELADO","CANCELADO"),
    #     ("FINALIZADO","FINALIZADO")
    # ) # Garante a integridade do banco de dados, valores padronizados.

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String) #PENDENTE, CANCELADO, FINALIZADO
    usuario = Column("usuario", ForeignKey("usuarios.id")) # Nome da tabela com campo único
    preco = Column("preco", Float)
    # itens = Column()

    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.preco = preco
        self.status = status

class ItemPedido(Base): 
    __tablename__ = "itens_pedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String) ## UMA TABELA DO BANCO DE DADOS
    tamanho = Column("tamanho", String) ## UMA TABELA DO BANCO DE DADOS
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", ForeignKey("pedidos.id"))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido

# Executa a criação dos metadados do seu banco (cria efetivamente o banco de dados)