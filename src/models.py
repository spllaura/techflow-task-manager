# src/models.py
# Classes do sistema de gerenciamento de tarefas — TechFlow Solutions

from datetime import datetime


class Usuario:
    """Representa um usuario do sistema."""
    _contador = 0

    def __init__(self, nome, email, senha, papel="comum"):
        Usuario._contador += 1
        self.id = Usuario._contador
        self.nome = nome
        self.email = email
        self.senha = senha
        self.papel = papel  # "comum" ou "admin"

    def cadastrar(self):
        """Registra o usuario no sistema."""
        return f"Usuario '{self.nome}' cadastrado com sucesso. ID: {self.id}"

    def autenticar(self, email, senha):
        """Verifica se o email e senha correspondem."""
        return self.email == email and self.senha == senha

    def atualizar_perfil(self, nome=None, email=None):
        """Atualiza os dados do perfil do usuario."""
        if nome:
            self.nome = nome
        if email:
            self.email = email
        return f"Perfil do usuario {self.id} atualizado."


class Tarefa:
    """Representa uma tarefa no sistema."""
    _contador = 0

    def __init__(self, titulo, descricao, prioridade, responsavel, data_vencimento=None):
        Tarefa._contador += 1
        self.id = Tarefa._contador
        self.titulo = titulo
        self.descricao = descricao
        self.status = "A Fazer"  # padrao inicial
        self.prioridade = prioridade  # "alta", "media", "baixa"
        self.data_criacao = datetime.now()
        self.data_vencimento = data_vencimento
        self.responsavel = responsavel  # objeto Usuario

    def criar(self):
        """Confirma a criacao da tarefa."""
        return f"Tarefa '{self.titulo}' criada com sucesso. ID: {self.id}"

    def editar(self, titulo=None, descricao=None, prioridade=None):
        """Edita os campos da tarefa."""
        if titulo:
            self.titulo = titulo
        if descricao:
            self.descricao = descricao
        if prioridade:
            self.prioridade = prioridade
        return f"Tarefa {self.id} editada com sucesso."

    def excluir(self):
        """Marca a tarefa como excluida."""
        return f"Tarefa {self.id} ('{self.titulo}') excluida."

    def alterar_status(self, novo_status):
        """Altera o status da tarefa (A Fazer, Em Progresso, Concluido)."""
        status_validos = ["A Fazer", "Em Progresso", "Concluido"]
        if novo_status not in status_validos:
            raise ValueError(f"Status invalido. Use: {status_validos}")
        self.status = novo_status
        return f"Tarefa {self.id} -> status alterado para '{novo_status}'."


class Notificacao:
    """Representa uma notificacao de prazo para uma tarefa."""
    _contador = 0

    def __init__(self, mensagem, tarefa, destinatario):
        Notificacao._contador += 1
        self.id = Notificacao._contador
        self.mensagem = mensagem
        self.data_envio = datetime.now()
        self.tarefa = tarefa  # objeto Tarefa
        self.destinatario = destinatario  # objeto Usuario

    def enviar(self):
        """Simula o envio da notificacao."""
        return (f"Notificacao enviada para {self.destinatario.email}: "
                f"'{self.mensagem}' (Tarefa: {self.tarefa.titulo})")


class Relatorio:
    """Gera relatorios de desempenho baseados nas tarefas."""

    def __init__(self, periodo, tarefas):
        self.periodo = periodo
        self.tarefas = tarefas  # lista de objetos Tarefa

    @property
    def total_tarefas(self):
        return len(self.tarefas)

    @property
    def tarefas_concluidas(self):
        return len([t for t in self.tarefas if t.status == "Concluido"])

    @property
    def tarefas_pendentes(self):
        return len([t for t in self.tarefas if t.status != "Concluido"])

    def gerar(self):
        """Gera o relatorio de desempenho."""
        return {
            "periodo": self.periodo,
            "total_tarefas": self.total_tarefas,
            "concluidas": self.tarefas_concluidas,
            "pendentes": self.tarefas_pendentes,
            "taxa_conclusao": f"{(self.tarefas_concluidas / self.total_tarefas * 100):.1f}%"
            if self.total_tarefas > 0 else "0%"
        }
