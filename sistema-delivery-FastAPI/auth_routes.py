from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])
# dominio/auth/...

@auth_router.get("/")
async def autenticar():
    """
    Essa é a rota padrão de autenticação do sistema
    """
    return {"mensagem": "Você acessou a rota padrão de autenticação", "autenticado": False}