from fastapi import FastAPI
import uvicorn
from db_conexion import base_de_datos

app = FastAPI()

# Api para obtener info de usuarios en db según ID
@app.get("/inicio/{id}")
async def InfoUsuarioId(id: int):
    conexion = base_de_datos()
    return {"Resultado Consulta": f'{conexion.seleccionar_id(id)}'}

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)