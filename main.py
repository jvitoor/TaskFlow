import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from supabase import create_client, Client

# Inicialização do FastAPI
app = FastAPI(title="TaskFlow API", version="1.0")

# Configuração de CORS para permitir requisições do Front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Suas credenciais do Supabase
SUPABASE_URL = "https://ecplfkzzsresfnvscloy.supabase.co"
SUPABASE_KEY = "sb_publishable_eJYBpJ3GltN3YeZVii5euA__NQa3zxt"

# ==========================================
# CAMADA DE ORIENTAÇÃO A OBJETOS (POO)
# ==========================================

class Task:
    """Classe de domínio que representa a Tarefa."""
    def __init__(self, title: str, description: str, status: str = "Pendente"):
        self.title = title
        self.description = description
        self.status = status

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status
        }


class TaskRepository:
    """Classe responsável exclusivamente por gerenciar a persistência no Supabase."""
    def __init__(self, supabase_client: Client):
        self.supabase = supabase_client

    def get_all_tasks(self):
        response = self.supabase.table("tasks").select("*").execute()
        return response.data

    def create_task(self, task: Task):
        response = self.supabase.table("tasks").insert(task.to_dict()).execute()
        return response.data


# Instanciação dos objetos
try:
    supabase_client: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    task_repository = TaskRepository(supabase_client)
except Exception as e:
    print(f"Erro ao conectar com o Supabase: {e}")


# ==========================================
# SCHEMAS DE VALIDAÇÃO (Pydantic)
# ==========================================

class TaskCreateSchema(BaseModel):
    title: str
    description: str
    status: str = "Pendente"


# ==========================================
# ROTAS DA API (Endpoints)
# ==========================================

@app.get("/")
def read_root():
    return {"message": "API TaskFlow rodando com sucesso!"}

@app.get("/tasks")
def list_tasks():
    try:
        tasks = task_repository.get_all_tasks()
        return {"tasks": tasks}
    except Exception as e:
        print(f"\n[ERRO DETALHADO NO GET /tasks]: {e}\n")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/tasks")
def create_task(task_data: TaskCreateSchema):
    try:
        # Instanciando o objeto da classe Task (POO)
        new_task = Task(
            title=task_data.title, 
            description=task_data.description, 
            status=task_data.status
        )
        
        # Salvando através do repositório
        result = task_repository.create_task(new_task)
        return {"message": "Tarefa criada com sucesso!", "data": result}
    except Exception as e:
        print(f"\n[ERRO DETALHADO NO POST /tasks]: {e}\n")
        raise HTTPException(status_code=500, detail=str(e))
