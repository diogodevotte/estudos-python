from fastapi import APIRouter

order_router = APIRouter(prefix="/order", tags=["order"])
# dominio/order/...

@order_router.get("/") # Atribui uma funcionalidade nova 
async def pedidos():
    """
    Essa é a rota padrão de pedidos do sistema. Todas as rotas dos pedidos precisam de autenticação.
    """
    return {"mensagem": "Você acessou a rota de pedidos"}