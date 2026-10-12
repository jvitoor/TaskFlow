# 🚀 TaskFlow - Gerenciador de Tarefas (Fullstack)

Aplicação web minimalista de gerenciamento de tarefas desenvolvida para demonstrar a integração entre Front-end moderno, Back-end orientado a objetos em Python (FastAPI) e persistência de dados em nuvem com Supabase.

---

## 🛠️ Tecnologias Utilizadas

* **Front-end:** HTML5, JavaScript (Vanilla ES6) e Tailwind CSS (via CDN).
* **Back-end:** Python, FastAPI, Pydantic e Programação Orientada a Objetos (POO).
* **Banco de Dados & Nuvem:** Supabase (PostgreSQL).

---

⚙️ Como Executar o Projeto Localmente
1. Pré-requisitos
Python instalado (versão 3.10 ou superior).

Uma conta e projeto criados no Supabase.

2. Configurar o Banco de Dados (Supabase)
No painel do Supabase, acesse o SQL Editor e execute o seguinte comando para criar a tabela:

3. Rodar o Back-end (Python)
Abra o terminal na pasta do projeto e instale as dependências:

pip install fastapi uvicorn supabase pydantic

-> Em seguida, certifique-se de que a chave do Supabase (SUPABASE_KEY) está configurada corretamente no arquivo main.py e inicie o servidor:

python -m uvicorn main:app --reload

4. Executar o Front-end
Dê um duplo clique no arquivo index.html para abri-lo diretamente no navegador

---

## 📂 Estrutura do Projeto

```text
taskflow-app/
│
├── main.py          # Código do back-end (FastAPI + POO + Supabase)
├── index.html       # Interface do usuário (Front-end)
├── .gitignore       # Arquivos ignorados pelo Git
└── README.md        # Documentação do projeto

