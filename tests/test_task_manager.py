# tests/test_task_manager.py
# Testes automatizados — TechFlow Solutions

import pytest
from src.models import Usuario, Tarefa, Notificacao, Relatorio
from src.task_manager import TaskManager


# =============================================
# TESTES UNITARIOS - USUARIO
# =============================================
class TestUsuario:
    def test_criar_usuario(self):
        """Testa a criacao de um usuario."""
        user = Usuario("Laura", "laura@test.com", "123", "comum")
        assert user.nome == "Laura"
        assert user.email == "laura@test.com"
        assert user.papel == "comum"

    def test_autenticar_sucesso(self):
        """Testa autenticacao com credenciais corretas."""
        user = Usuario("Laura", "laura@test.com", "123")
        assert user.autenticar("laura@test.com", "123") == True

    def test_autenticar_falha(self):
        """Testa autenticacao com credenciais erradas."""
        user = Usuario("Laura", "laura@test.com", "123")
        assert user.autenticar("laura@test.com", "errada") == False

    def test_atualizar_perfil(self):
        """Testa a atualizacao do perfil."""
        user = Usuario("Laura", "laura@test.com", "123")
        user.atualizar_perfil(nome="Laura Araujo")
        assert user.nome == "Laura Araujo"


# =============================================
# TESTES UNITARIOS - TAREFA
# =============================================
class TestTarefa:
    def test_criar_tarefa(self):
        """Testa a criacao de uma tarefa."""
        user = Usuario("Laura", "laura@test.com", "123")
        tarefa = Tarefa("Teste", "Descricao", "alta", user)
        assert tarefa.titulo == "Teste"
        assert tarefa.status == "A Fazer"
        assert tarefa.prioridade == "alta"

    def test_alterar_status_valido(self):
        """Testa alteracao de status com valor valido."""
        user = Usuario("Laura", "laura@test.com", "123")
        tarefa = Tarefa("Teste", "Desc", "alta", user)
        tarefa.alterar_status("Em Progresso")
        assert tarefa.status == "Em Progresso"

    def test_alterar_status_invalido(self):
        """Testa que status invalido gera erro."""
        user = Usuario("Laura", "laura@test.com", "123")
        tarefa = Tarefa("Teste", "Desc", "alta", user)
        with pytest.raises(ValueError):
            tarefa.alterar_status("Invalido")

    def test_editar_tarefa(self):
        """Testa a edicao de uma tarefa."""
        user = Usuario("Laura", "laura@test.com", "123")
        tarefa = Tarefa("Titulo Original", "Desc", "media", user)
        tarefa.editar(titulo="Titulo Editado")
        assert tarefa.titulo == "Titulo Editado"


# =============================================
# TESTES DO CRUD - TASK MANAGER
# =============================================
class TestTaskManager:
    def test_criar_tarefa_valida(self):
        """Testa criacao de tarefa via manager."""
        manager = TaskManager()
        user = manager.cadastrar_usuario("Laura", "l@t.com", "123")
        tarefa = manager.criar_tarefa("Teste", "Desc", "alta", user)
        assert len(manager.listar_tarefas()) == 1

    def test_criar_tarefa_titulo_vazio(self):
        """Testa que titulo vazio gera erro."""
        manager = TaskManager()
        user = manager.cadastrar_usuario("Laura", "l@t.com", "123")
        with pytest.raises(ValueError):
            manager.criar_tarefa("", "Desc", "alta", user)

    def test_criar_tarefa_prioridade_invalida(self):
        """Testa que prioridade invalida gera erro."""
        manager = TaskManager()
        user = manager.cadastrar_usuario("Laura", "l@t.com", "123")
        with pytest.raises(ValueError):
            manager.criar_tarefa("Teste", "Desc", "urgente", user)

    def test_excluir_tarefa(self):
        """Testa exclusao de tarefa."""
        manager = TaskManager()
        user = manager.cadastrar_usuario("Laura", "l@t.com", "123")
        tarefa = manager.criar_tarefa("Para excluir", "Desc", "baixa", user)
        manager.excluir_tarefa(tarefa.id)
        assert len(manager.listar_tarefas()) == 0

    def test_filtrar_por_status(self):
        """Testa filtro por status."""
        manager = TaskManager()
        user = manager.cadastrar_usuario("Laura", "l@t.com", "123")
        t1 = manager.criar_tarefa("T1", "D", "alta", user)
        t2 = manager.criar_tarefa("T2", "D", "media", user)
        t1.alterar_status("Concluido")
        concluidas = manager.filtrar_por_status("Concluido")
        assert len(concluidas) == 1
        assert concluidas[0].titulo == "T1"

    def test_filtrar_por_prioridade(self):
        """Testa filtro por prioridade."""
        manager = TaskManager()
        user = manager.cadastrar_usuario("Laura", "l@t.com", "123")
        manager.criar_tarefa("T1", "D", "alta", user)
        manager.criar_tarefa("T2", "D", "baixa", user)
        altas = manager.filtrar_por_prioridade("alta")
        assert len(altas) == 1


# =============================================
# TESTES DE INTEGRACAO
# =============================================
class TestIntegracao:
    def test_fluxo_completo_tarefa(self):
        """Testa o fluxo: criar -> editar -> alterar status -> concluir."""
        manager = TaskManager()
        user = manager.cadastrar_usuario("Laura", "l@t.com", "123")
        tarefa = manager.criar_tarefa("Fluxo completo", "Teste de integracao", "alta", user)
        manager.editar_tarefa(tarefa.id, titulo="Fluxo completo editado")
        tarefa.alterar_status("Em Progresso")
        tarefa.alterar_status("Concluido")
        assert tarefa.titulo == "Fluxo completo editado"
        assert tarefa.status == "Concluido"

    def test_relatorio(self):
        """Testa a geracao de relatorio."""
        user = Usuario("Laura", "l@t.com", "123")
        t1 = Tarefa("T1", "D", "alta", user)
        t2 = Tarefa("T2", "D", "media", user)
        t1.alterar_status("Concluido")
        relatorio = Relatorio("Maio 2026", [t1, t2])
        resultado = relatorio.gerar()
        assert resultado["total_tarefas"] == 2
        assert resultado["concluidas"] == 1
        assert resultado["pendentes"] == 1
