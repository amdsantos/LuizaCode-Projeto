from fastapi import FastAPI
from typing import List
from pydantic import BaseModel


app = FastAPI()

OK = "OK"
FALHA = "FALHA"


############### CLASSES ###############
class Endereco(BaseModel):
    rua: str
    cep: str
    cidade: str
    estado: str

class Usuario(BaseModel):
    id: int
    nome: str
    email: str
    senha: str

class ListaDeEnderecosDoUsuario(BaseModel):
    usuario: Usuario
    enderecos: List[Endereco] = []

class Produto(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float

class CarrinhoDeCompras(BaseModel):
    id_usuario: int
    id_produtos: List[Produto] = []
    preco_total: float
    quantidade_de_produtos: int


db_usuarios = {}
db_produtos = {}
db_enderecos = {}        
db_carrinhos = {}


# Criar um usuário
@app.post("/usuario/")
async def criar_usuario(usuario: Usuario):
    if usuario.id in db_usuarios:
        return FALHA
    db_usuarios[usuario.id] = usuario
    return OK, db_usuarios


# Buscar usuário pelo id
@app.get("/usuario/")
async def retornar_usuario(id: int):
    if id in db_usuarios:
        return db_usuarios[id]
    return FALHA


# Buscar usuário pelo nome
@app.get("/usuario/nome")
async def retornar_usuario_com_nome(nome: str):
    for id, usuario in db_usuarios.items():
        if usuario.nome == nome:
            return db_usuarios[id]
        return FALHA


# Deletar usuário pelo id e deletar também endereços e carrinhos vinculados a ele
@app.delete("/usuario/")
async def deletar_usuario(id: int):
    if id in db_usuarios:
        del db_usuarios[id]
        db_usuarios
        return OK
    return FALHA


# Retornar todos os emails que possuem o mesmo domínio
@app.get("/usuarios/emails/")
async def retornar_emails(dominio: str):
    email = []
    for emails in db_usuarios.items():
        if emails.dominio == dominio: 
            email.append(emails.dominio)
        return FALHA
    

# Criar um endereço, vincular ao usuário e retornar OK
@app.post("/endereco/{id_usuario}/")
async def criar_endereco(endereco: Endereco, id_usuario: int):
    if id_usuario in db_usuarios:
        db_enderecos.setdefault(id_usuario, []).append(endereco)
        return OK, db_enderecos
    return FALHA


#Retornar endereços do usuário
@app.get("/usuario/{id_usuario}/enderecos/")
async def retornar_enderecos_do_usuario(id_usuario: int):
    for id_usuario in db_usuarios.items():
        if id_usuario != db_usuarios:
            return FALHA   
        elif id_usuario == id_usuario:
            return db_enderecos[id_usuario]
        return []


# Se não existir endereço com o id_endereco retornar falha, 
# senão deleta endereço correspondente ao id_endereco e retornar OK
# (lembrar de desvincular o endereço ao usuário)
@app.delete("/usuario/{id_usuario}/endereco/{id_endereco}/")
async def deletar_endereco(id_endereco: int):
    for id_endereco in db_enderecos.item():
        if id_endereco != id:
            return FALHA
        del db_enderecos[id_endereco]
        return OK


# Se tiver outro produto com o mesmo ID retornar falha, 
# senão cria um produto e retornar OK
@app.post("/produto/")
async def criar_produto(produto: Produto):
    if produto.id in db_produtos: 
        return FALHA
    db_produtos[produto.id] = produto
    return OK


# Se não existir produto com o id_produto retornar falha, 
# senão deleta produto correspondente ao id_produto e retornar OK
# (lembrar de desvincular o produto dos carrinhos do usuário)
@app.delete("/produto/{id_produto}/")
async def deletar_produto(id_produto: int):
    for id_produto in db_produtos:
        if id_produto in db_produtos:
            del db_produtos[id_produto]
            return OK
        return FALHA


# Se não existir usuário com o id_usuario ou id_produto retornar falha, 
# se não existir um carrinho vinculado ao usuário, crie o carrinho
# e retornar OK
# senão adiciona produto ao carrinho e retornar OK
@app.post("/carrinho/{id_usuario}/{id_produto}/")
async def adicionar_carrinho(id_usuario: int, id_produto: int):
    return FALHA


# Se não existir carrinho com o id_usuario retornar falha, 
# senão retorna o carrinho de compras.
@app.get("/carrinho/{id_usuario}/")
async def retornar_carrinho(id_usuario: int):
    if id_usuario in db_carrinhos:
        return db_carrinhos[id_usuario]
    return FALHA


# Se não existir carrinho com o id_usuario retornar falha, 
# senão retorna o o número de itens e o valor total do carrinho de compras.
@app.get("/carrinho/total/{id_usuario}/")
async def retornar_total_carrinho(id_usuario: int):
    return FALHA

    
# Se não existir usuário com o id_usuario retornar falha, 
# senão deleta o carrinho correspondente ao id_usuario e retornar OK
@app.delete("/carrinho/{id_usuario}/")
async def deletar_carrinho(id_usuario: int):
    if id_usuario in db_usuarios:
        del db_carrinhos[id_usuario]
        return OK, db_carrinhos
    return FALHA


@app.get("/")
async def bem_vinda():
    site = "Seja bem vinda"
    return site.replace('\n', '')
