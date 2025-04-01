from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime
from app.database import get_db
from app.models import Voto, Usuario, Assembleia

router = APIRouter(prefix="/votos", tags=["Votos"])


# Esquema de dados para criação de um voto
class VotoCreate(BaseModel):
    usuario_id: int
    assembleia_id: int
    opcao: str


@router.get("/")
def listar_votos(db: Session = Depends(get_db)):
    """
    Endpoint para listar todos os votos.
    """
    votos = db.query(Voto).all()
    return votos


@router.post("/")
def criar_voto(voto: VotoCreate, db: Session = Depends(get_db)):
    """
    Endpoint para registrar um voto.
    Verifica se o usuário e a assembleia existem antes de registrar.
    """
    # Verifica se o usuário existe
    usuario = db.query(Usuario).filter(Usuario.id == voto.usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    # Verifica se a assembleia existe
    assembleia = db.query(Assembleia).filter(Assembleia.id == voto.assembleia_id).first()
    if not assembleia:
        raise HTTPException(status_code=404, detail="Assembleia não encontrada")

    novo_voto = Voto(
        usuario_id=voto.usuario_id,
        assembleia_id=voto.assembleia_id,
        opcao=voto.opcao,
        registrado_em=datetime.utcnow()
    )
    db.add(novo_voto)
    db.commit()
    db.refresh(novo_voto)
    return novo_voto
