from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Obtém a string de conexão definida no .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Cria a engine do SQLAlchemy usando a string de conexão
engine = create_engine(DATABASE_URL)

# Cria uma sessão local para o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria a base declarativa que será usada para definir os modelos
Base = declarative_base()

# Função para obter uma sessão (usada em dependências do FastAPI)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
