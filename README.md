# Plataforma Votação - Projeto

Descrição breve do projeto.

## Pré-requisitos

Antes de começar, garanta que você tenha o seguinte software instalado em sua máquina Windows e **adicionado ao PATH do sistema** durante a instalação:

1.  **Python:** Versão 3.10 ou superior. [Download Python](https://www.python.org/downloads/) (Marque "Add Python X.Y to PATH" na instalação).
2.  **Git:** Para controle de versão. [Download Git](https://git-scm.com/download/win).
3.  **PostgreSQL:** Banco de dados. [Download PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-installer) (Anote a senha que definir para o usuário `postgres` durante a instalação).

## Configuração Rápida (Recomendado)

Após clonar o repositório, você pode configurar o ambiente automaticamente executando um script. **Faça isso apenas uma vez.**

1.  **Instale o PostgreSQL:** Se ainda não o fez, instale o PostgreSQL (veja pré-requisitos).
2.  **Crie o Banco de Dados `plataforma`:**
    *   Abra o **pgAdmin** (instalado com o PostgreSQL).
    *   Conecte-se ao seu servidor local (geralmente `localhost`, usuário `postgres`, senha definida na instalação).
    *   Clique com o botão direito em "Databases" -> "Create" -> "Database...".
    *   Digite `plataforma` como nome do banco e clique em "Save".
3.  **Execute o Script de Setup:**
    *   Navegue até a pasta onde você clonou o projeto (`plataforma-votacao`).
    *   Encontre o arquivo `setup_ambiente.bat`.
    *   Dê um **duplo clique** em `setup_ambiente.bat`.
4.  **Siga as Instruções:** O script irá:
    *   Verificar se Python e Git estão no PATH.
    *   Criar um ambiente virtual (`env`).
    *   Ativar o ambiente virtual.
    *   Instalar as dependências do `requirements.txt`.
    *   Copiar `.env.example` para `.env` (se `.env` não existir).
    *   **IMPORTANTE:** Pedir para você editar o `.env` e colocar a senha correta do seu PostgreSQL.
    *   Executar as migrações do banco de dados (`alembic upgrade head`).
5.  **Edite o `.env`:** Abra o arquivo `.env` (que foi criado na pasta do projeto) em um editor de texto e substitua `SUA_SENHA_AQUI` pela senha que você definiu para o usuário `postgres` ao instalar o PostgreSQL. Salve o arquivo.
6.  **Resultado:** Se tudo correu bem, uma janela de terminal permanecerá aberta com o ambiente virtual (`env`) ativado, pronto para uso.

## Uso Diário

Após a configuração inicial, para trabalhar no projeto:

1.  **Abra o Terminal (CMD ou PowerShell)** na pasta do projeto (`plataforma-votacao`).
2.  **Ative o Ambiente Virtual:**
    *   PowerShell: `.\env\Scripts\Activate.ps1`
    *   CMD: `env\Scripts\activate.bat`
    *   Seu prompt deve mudar para indicar `(env)`.
3.  **Inicie o Servidor (se necessário):**
    ```powershell
    uvicorn app.main:app --reload
    ```
4.  Acesse a API em `http://localhost:8000/docs`.

## Recebendo Atualizações

Quando houver atualizações no repositório principal:

1.  **Abra o Terminal** na pasta do projeto.
2.  **Ative o Ambiente Virtual.**
3.  **Puxe as Alterações:**
    ```powershell
    git pull origin main # ou sua branch principal
    ```
4.  **Atualize as Dependências (se `requirements.txt` mudou):**
    ```powershell
    pip install -r requirements.txt
    ```
5.  **Aplique Novas Migrações do Banco (se houver):**
    ```powershell
    alembic upgrade head
    ```

## Troubleshooting Comum

*   **Erro 'python'/'git'/'pip'/'alembic' não reconhecido:** Verifique se o software está instalado e adicionado ao PATH do sistema. Pode ser necessário reiniciar o terminal ou o computador após a instalação/atualização do PATH.
*   **Erro ao ativar ambiente virtual (PowerShell):** Pode ser necessário ajustar a política de execução. Abra o PowerShell como Administrador e execute: `Set-ExecutionPolicy RemoteSigned -Scope Process -Force`. Tente ativar novamente em um PowerShell normal.
*   **Erro de conexão com o banco / Alembic:** Verifique se o PostgreSQL está rodando, se o banco `plataforma` existe, e se o usuário (`postgres`) e a senha no arquivo `.env` estão corretos e correspondem à configuração do seu PostgreSQL.