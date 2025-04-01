from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db
from app.models import Usuario

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


# Esquema de dados para criação de um usuário
class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str
    admin: bool = False  # Valor padrão é False


@router.get("/")
def listar_usuarios(db: Session = Depends(get_db)):
    """
    Endpoint para listar todos os usuários.
    """
    usuarios = db.query(Usuario).all()
    return usuarios


@router.post("/")
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    """
    Endpoint para criar um novo usuário.
    Verifica se o email já existe para evitar duplicatas.
    """
    # Verifica se já existe um usuário com o mesmo email
    usuario_existente = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="Email já registrado")

    novo_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha=usuario.senha,
        admin=usuario.admin
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario
