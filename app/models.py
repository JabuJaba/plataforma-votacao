from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime

# Cria a base declarativa que será usada para definir os modelos
Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)
    admin = Column(Boolean, default=False)

    # Relação com votos (um usuário pode ter vários votos)
    votos = relationship("Voto", back_populates="usuario")


class Assembleia(Base):
    __tablename__ = 'assembleias'

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    descricao = Column(Text, nullable=False)
    data_inicio = Column(DateTime, default=datetime.utcnow)
    data_fim = Column(DateTime, nullable=True)
    finalizada = Column(Boolean, default=False)

    # Relação com votos (uma assembleia pode ter vários votos)
    votos = relationship("Voto", back_populates="assembleia")


class Voto(Base):
    __tablename__ = 'votos'

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    assembleia_id = Column(Integer, ForeignKey("assembleias.id"), nullable=False)
    opcao = Column(String(100), nullable=False)
    registrado_em = Column(DateTime, default=datetime.utcnow)

    # Relação de volta com os modelos Usuario e Assembleia
    usuario = relationship("Usuario", back_populates="votos")
    assembleia = relationship("Assembleia", back_populates="votos")
