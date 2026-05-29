# src/task_manager.py
# Gerenciador de tarefas com operacoes CRUD — TechFlow Solutions

from src.models import Tarefa, Usuario


class TaskManager:
    """Classe que gerencia as operacoes CRUD de tarefas."""

    def __init__(self):
        self.tarefas = []
        self.usuarios = []

    # === CRUD DE USUARIOS ===
    def cadastrar_usuario(self, nome, email, senha, papel="comum"):
        """CREATE: Cadastra um novo usuario."""
        usuario = Usuario(nome, email, senha, papel)
        self.usuarios.append(usuario)
        return usuario

    # === CRUD DE TAREFAS ===
    def criar_tarefa(self, titulo, descricao, prioridade, responsavel, data_vencimento=None):
        """CREATE: Cria uma nova tarefa."""
        if not titulo or not titulo.strip():
            raise ValueError("O titulo da tarefa nao pode ser vazio.")
        if prioridade not in ["alta", "media", "baixa"]:
            raise ValueError("Prioridade deve ser 'alta', 'media' ou 'baixa'.")
        tarefa = Tarefa(titulo, descricao, prioridade, responsavel, data_vencimento)
        self.tarefas.append(tarefa)
        return tarefa

    def listar_tarefas(self):
        """READ: Retorna todas as tarefas."""
        return self.tarefas

    def buscar_tarefa_por_id(self, tarefa_id):
        """READ: Busca uma tarefa pelo ID."""
        for tarefa in self.tarefas:
            if tarefa.id == tarefa_id:
                return tarefa
        return None

    def editar_tarefa(self, tarefa_id, titulo=None, descricao=None, prioridade=None):
        """UPDATE: Edita uma tarefa existente."""
        tarefa = self.buscar_tarefa_por_id(tarefa_id)
        if not tarefa:
            raise ValueError(f"Tarefa com ID {tarefa_id} nao encontrada.")
        return tarefa.editar(titulo, descricao, prioridade)

    def excluir_tarefa(self, tarefa_id):
        """DELETE: Remove uma tarefa da lista."""
        tarefa = self.buscar_tarefa_por_id(tarefa_id)
        if not tarefa:
            raise ValueError(f"Tarefa com ID {tarefa_id} nao encontrada.")
        self.tarefas.remove(tarefa)
        return tarefa.excluir()

    # === FILTROS ===
    def filtrar_por_status(self, status):
        """Filtra tarefas pelo status."""
        return [t for t in self.tarefas if t.status == status]

    def filtrar_por_prioridade(self, prioridade):
        """Filtra tarefas pela prioridade."""
        return [t for t in self.tarefas if t.prioridade == prioridade]
