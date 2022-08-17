from typing import Union, Optional
from pydantic import BaseModel
from fastapi import FastAPI, Header
class Item(BaseModel):
    id: int
    descricao: str
    quantidade: int
    valor: float

app = FastAPI()

banco_de_dados=[]

@app.post("/item")
def add_item(item: Item):
    banco_de_dados.append(item)

@app.get("/item")
def list_item():
    return banco_de_dados

@app.get("/item/valor_total")
def get_valor_total():
    valor_total = 0.0
    for item in banco_de_dados:
        valor_total+=item.valor*item.quantidade
        return valor_total
"""@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
"""