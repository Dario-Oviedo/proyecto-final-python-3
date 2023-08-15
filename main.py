# %%
import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

# %%
class Item(BaseModel):
    marca: str
    descripcion: str
    precio: float

app = FastAPI()


# %%
@app.post("/agregar_elemento/")
async def agregar_elemento(item: Item):
    conn = sqlite3.connect("watches.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO watch (marca, descripcion, precio) VALUES (?, ?, ?)", (item.marca, item.descripcion, item.precio))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos agregados"}


# %%
@app.put("/actualizar_elemento/{id}/")
async def actualizar_elemento(id: int, item: Item):
    conn = sqlite3.connect("watches.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE watch SET marca=?, descripcion=?, precio=? WHERE id=?", (item.marca, item.descripcion, item.precio))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos actualizados exitosamente"}


# %%
@app.get("/leer_elementos/")
async def leer_elementos():
    conn = sqlite3.connect("C:\\Users\\hj5k5r\\Python 3 Curso\\watches.db")
    cursor = conn.cursor()
    cursor.execute("SELECT precio, marca, descripcion FROM ranking")
    resultados = cursor.fetchall()
    conn.close()
    if resultados:
        return [{"precio": resultado[0], "descripcion": resultado[1], "marca": resultado[2]} for resultado in resultados]
    else:
        return {"mensaje": "No hay datos en la base de datos"}

# %%
@app.get("/leer_elemento/{id}")
async def leer_elemento(id: int):
    conn = sqlite3.connect("watches.db")
    cursor = conn.cursor()
    cursor.execute("SELECT marca, descripcion, precio FROM watch WHERE id=?", (id,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return [{"marca": resultado[0], "descripcion": resultado[1], "precio": resultado[2]} for resultado in resultado]
    else:
        return{"mensaje": "No hay datos en la DB"}
    



# %%
@app.delete("/eliminar_elemento/{id}/")
async def actualizar_elemento(id: int, item: Item):
    conn = sqlite3.connect("watches.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM watch WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos eliminados exitosamente"}


# %%
