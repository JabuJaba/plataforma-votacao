from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime
from app.database import get_db
from app.models import Assembleia

router = APIRouter(prefix="/assembleias", tags=["Assembleias"])

# Esquema de dados para criação de uma assembleia
class AssembleiaCreate(BaseModel):
    titulo: str
    descricao: str
    data_fim: datetime  # Deve ser enviado no formato ISO (ex.: "2025-12-31T23:59:59")

@router.get("/")
def listar_assembleias(db: Session = Depends(get_db)):
    """
    Endpoint para listar todas as assembleias.
    """
    assembleias = db.query(Assembleia).all()
    return assembleias

@router.post("/")
def criar_assembleia(assembleia: AssembleiaCreate, db: Session = Depends(get_db)):
    """
    Endpoint para criar uma nova assembleia.
    Define data_inicio como o momento atual e finalizada como False.
    """
    nova_assembleia = Assembleia(
        titulo=assembleia.titulo,
        descricao=assembleia.descricao,
        data_inicio=datetime.utcnow(),
        data_fim=assembleia.data_fim,
        finalizada=False
    )
    db.add(nova_assembleia)
    db.commit()
    db.refresh(nova_assembleia)
    return nova_assembleia
