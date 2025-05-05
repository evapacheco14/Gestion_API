import json
import os
from typing import TypeVar, Type, List
from pydantic import BaseModel

ModelType = TypeVar('ModelType', bound=BaseModel)

class GestorArchivosGenerico:

    def __init__(self, modelo: Type[ModelType], archivo_path: str):
        self.modelo = modelo
        self.archivo_path = archivo_path
        
       
        if not os.path.exists(self.archivo_path):
            with open(self.archivo_path, 'w', encoding='utf-8') as archivo:
                json.dump([], archivo)

    def get_all(self) -> List[ModelType]:
        with open(self.archivo_path, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            return [self.modelo(**item) for item in datos]

    def get_by_id(self, id: int) -> ModelType:
        with open(self.archivo_path, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            for item in datos:
                if item['id'] == id:
                    return self.modelo(**item)
            raise ValueError(f"{self.modelo.__name__} con id {id} no encontrado")

    def add(self, objeto: ModelType):
        with open(self.archivo_path, 'r+', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            ids = [item['id'] for item in datos]
            if objeto.id in ids:
                raise ValueError(f"{self.modelo.__name__} con id {objeto.id} ya existe")
            datos.append(objeto.dict())
            archivo.seek(0)
            json.dump(datos, archivo, indent=4)
            archivo.truncate()

    def update(self, id: int, datos: dict):
        with open(self.archivo_path, 'r+', encoding='utf-8') as archivo:
            datos_json = json.load(archivo)
            for idx, item in enumerate(datos_json):
                if item['id'] == id:
                    datos_json[idx].update(datos)
                    archivo.seek(0)
                    json.dump(datos_json, archivo, indent=4)
                    archivo.truncate()
                    return
            raise ValueError(f"{self.modelo.__name__} con id {id} no encontrado")

    def delete(self, id: int):
        with open(self.archivo_path, 'r+', encoding='utf-8') as archivo:
            datos_json = json.load(archivo)
            for idx, item in enumerate(datos_json):
                if item['id'] == id:
                    del datos_json[idx]
                    archivo.seek(0)
                    json.dump(datos_json, archivo, indent=4)
                    archivo.truncate()
                    return
            raise ValueError(f"{self.modelo.__name__} con id {id} no encontrado")
