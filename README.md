# 📰 Web Scraper de Notícias da BBC

🚀 Um **Web Scraper** que captura notícias da **BBC** usando **Playwright** e armazena no banco de dados **MySQL** via **SQLAlchemy**.

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Playwright](https://img.shields.io/badge/Playwright-1.39-green?style=for-the-badge)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?style=for-the-badge)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?style=for-the-badge)

---

## 📌 Funcionalidades
✔ Captura automaticamente os **títulos das notícias** do site da BBC.  
✔ **Salva no banco de dados** MySQL usando SQLAlchemy.  
✔ **Criação automática da tabela** caso não exista.  
✔ **Registra logs** detalhados em um arquivo de log.  
✔ **Timeout ajustável** para evitar falhas de carregamento.  

---

## 🛠️ Pré-requisitos
Antes de rodar o projeto, **certifique-se de ter instalado**:

- **Python 3.12** ou superior
- **MySQL 8.0** ou superior
- **Git** (para clonar o repositório)

Além disso, tenha um **banco de dados MySQL rodando** e crie um banco chamado `news_db`:
```sql
CREATE DATABASE news_db;
```
### ⚙️ Instalação e Configuração
1️⃣ Clone o repositório
```
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
```
2️⃣ Crie um ambiente virtual (recomendado)
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows
```
3️⃣ Instale as dependências
```
pip install -r requirements.txt
```
4️⃣ Configure o banco de dados no .env
Crie um arquivo .env na raiz do projeto e adicione suas credenciais do MySQL:
```
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=sua_senha
MYSQL_DATABASE=news_db
```
🚀 Como Rodar
✅ execute no terminal:
```
python main.py
```
Isso irá:

  
  Acessar o site da BBC
  
  Capturar o título da primeira notícia
  
  Salvar a notícia no banco de dados

  
✅  Conferir os logs
O arquivo news_scraper.log contém os registros da execução:

```
cat news_scraper.log
```

📊 Estrutura do Projeto

```📂 rpa-scrapping/
├── 📄 main.py          # Executa o scraper
├── 📄 scraper.py       # Captura as notícias da BBC
├── 📄 database.py      # Conexão e manipulação do MySQL
├── 📄 config.py        # Configuração do banco de dados
├── 📄 requirements.txt # Dependências do projeto
├── 📄 README.md        # Documentação
└── 📄 .env             # Configuração das credenciais do banco
```

## 🛠️ Tecnologias Utilizadas
🔹 Python 3.12 - Linguagem principal

🔹 Playwright - Para acessar e capturar notícias

🔹 SQLAlchemy - Para conexão com o banco MySQL

🔹 MySQL - Banco de dados

🔹 Dotenv - Para carregar variáveis de ambiente


