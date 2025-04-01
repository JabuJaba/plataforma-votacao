from fastapi import FastAPI

# Importe as rotas que você criou
from app.routes import usuarios, assembleias, votos

# Crie a instância da aplicação FastAPI
app = FastAPI(title="Plataforma de Votação Digital")

# Inclua os routers de cada arquivo de rota
app.include_router(usuarios.router)
app.include_router(assembleias.router)
app.include_router(votos.router)

# Ponto de entrada opcional (permite rodar com: python -m app.main)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
