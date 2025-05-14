from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from entrega import responder_llm
app = FastAPI(title="Asistente Legal LUC")
class PreguntaInput(BaseModel):
    pregunta: str
    k: int = 3  # número de chunks a recuperar por default
    @app.get("/")
    def read_root():
     return {"mensaje": "Asistente Legal LUC listo para responder"}
@app.post("/preguntar")
def preguntar(input: PreguntaInput):
    try:
        respuesta = responder_llm(input.pregunta, k=input.k)
        return {"respuesta": respuesta}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    if name == "main":
     uvicorn.run("FP:app", host="127.0.0.1", port=8000, reload=True)