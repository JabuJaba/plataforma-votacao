@echo off
echo ====================================================
echo    Configurando Ambiente de Desenvolvimento       
echo ====================================================
echo.

:: Define o diretório do projeto baseado na localização do script
set "PROJECT_ROOT=%~dp0"
cd /D "%PROJECT_ROOT%"

echo Verificando Python...
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo ERRO: Python nao encontrado no PATH. Instale Python e adicione ao PATH.
    pause
    exit /b 1
)

echo Verificando Git...
git --version > nul 2>&1
if %errorlevel% neq 0 (
    echo ERRO: Git nao encontrado no PATH. Instale Git e adicione ao PATH.
    pause
    exit /b 1
)

echo Criando/Verificando Ambiente Virtual (env)...
if not exist env (
    echo Criando pasta env...
    python -m venv env
    if %errorlevel% neq 0 (
        echo ERRO: Falha ao criar ambiente virtual.
        pause
        exit /b 1
    )
) else (
    echo Pasta env ja existe.
)

echo Ativando o Ambiente Virtual...
call env\Scripts\activate.bat
if not defined VIRTUAL_ENV (
   echo ERRO: Falha ao ativar ambiente virtual.
   pause
   exit /b 1
)

echo Instalando dependencias de requirements.txt...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERRO: Falha ao instalar dependencias. Verifique requirements.txt e conexao.
    pause
    exit /b 1
)

echo Configurando arquivo .env (se nao existir)...
if not exist .env (
    if exist .env.example (
        echo Copiando .env.example para .env...
        copy .env.example .env > nul
        echo POR FAVOR: Edite o arquivo .env e configure sua senha do PostgreSQL.
    ) else (
        echo AVISO: Arquivo .env.example nao encontrado. Crie o .env manualmente.
    )
) else (
    echo Arquivo .env ja existe. Verifique se esta correto.
)

echo.
echo =======================================================
echo   Verificando Configuracao do Banco de Dados e Alembic  
echo =======================================================
echo Verificando conexao com Alembic (tentando historico)...
alembic history
 if %errorlevel% neq 0 (
    echo.
    echo ERRO: Falha ao executar Alembic. Verifique se o PostgreSQL esta instalado,
    echo       rodando e se a DATABASE_URL no .env esta correta (banco 'plataforma',
    echo       usuario 'postgres' e a senha correta).
    echo.
    echo       Voce pode precisar criar o banco 'plataforma' manualmente no pgAdmin:
    echo       CREATE DATABASE plataforma;
    pause
    exit /b 1
)

echo Aplicando migracoes do banco de dados (Alembic)...
alembic upgrade head
if %errorlevel% neq 0 (
    echo ERRO: Falha ao aplicar migracoes. Verifique a conexao e logs do Alembic/PostgreSQL.
    pause
    exit /b 1
)

echo.
echo ====================================================
echo    Configuracao Concluida com Sucesso!             
echo ====================================================
echo.
echo Para iniciar o servidor, use o comando:
echo uvicorn app.main:app --reload
echo.
echo Este terminal ja esta com o ambiente virtual ativado.
echo Pressione qualquer tecla para fechar esta janela inicial ou continue usando este terminal.

:: Deixa o prompt aberto para o usuário
cmd /k