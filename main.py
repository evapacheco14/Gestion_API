from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from models import Usuario, Producto, Pedido
from gestor_archivos import GestorArchivosGenerico

app = FastAPI()


gestor_usuarios = GestorArchivosGenerico(Usuario, 'usuarios.json')
gestor_productos = GestorArchivosGenerico(Producto, 'productos.json')
gestor_pedidos = GestorArchivosGenerico(Pedido, 'pedidos.json')

@app.get("/usuarios", response_model=List[Usuario])
def listar_usuarios():
    return gestor_usuarios.get_all()

@app.get("/usuarios/{id}", response_model=Usuario)
def obtener_usuario(id: int):
    return gestor_usuarios.get_by_id(id)

@app.post("/usuarios", status_code=201)
def crear_usuario(usuario: Usuario):
    gestor_usuarios.add(usuario)

@app.put("/usuarios/{id}")
def actualizar_usuario(id: int, usuario: dict):
    gestor_usuarios.update(id, usuario)

@app.delete("/usuarios/{id}")
def eliminar_usuario(id: int):
    gestor_usuarios.delete(id)


@app.get("/productos", response_model=List[Producto])
def listar_productos():
    return gestor_productos.get_all()

@app.get("/productos/{id}", response_model=Producto)
def obtener_producto(id: int):
    return gestor_productos.get_by_id(id)

@app.post("/productos", status_code=201)
def crear_producto(producto: Producto):
    gestor_productos.add(producto)

@app.put("/productos/{id}")
def actualizar_producto(id: int, producto: dict):
    gestor_productos.update(id, producto)

@app.delete("/productos/{id}")
def eliminar_producto(id: int):
    gestor_productos.delete(id)

@app.get("/pedidos", response_model=List[Pedido])
def listar_pedidos():
    return gestor_pedidos.get_all()


@app.get("/pedidos/{id}", response_model=Pedido)
def obtener_pedido(id: int):
    return gestor_pedidos.get_by_id(id)


@app.post("/pedidos", status_code=201)
def crear_pedido(pedido: Pedido):
    gestor_pedidos.add(pedido)


@app.put("/pedidos/{id}")
def actualizar_pedido(id: int, pedido: Pedido):
    gestor_pedidos.update(id, pedido.dict())


@app.delete("/pedidos/{id}")
def eliminar_pedido(id: int):
    gestor_pedidos.delete(id)