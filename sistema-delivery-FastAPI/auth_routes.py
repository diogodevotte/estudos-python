from fastapi import APIRouter
from models import Usuario, db
from sqlalchemy.orm import sessionmaker

auth_router = APIRouter(prefix="/auth", tags=["auth"])
# dominio/auth/...

@auth_router.get("/")
async def home():
    """
    Essa é a rota padrão de autenticação do sistema
    """
    return {"mensagem": "Você acessou a rota padrão de autenticação", "autenticado": False}

@auth_router.post("/criar_conta") # Postando um item dentro do sistema
async def criar_conta(email: str, senha: str, nome: str):
    Session = sessionmaker(bind=db) # Criando uma conexão com o banco de dados 
    session = Session() # Criando uma instância do banco de dados
    usuario = session.query(Usuario).filter(Usuario.email==email).first() # Consulta no banco de dados
    if usuario:
        # Já existe um usuário com esse email
        return {"mesagem": "já existe um usuário com esse email."}
    else:
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit() # Edita o banco de dados 
        return {"mesagem": "usuário cadastrado com sucesso."}