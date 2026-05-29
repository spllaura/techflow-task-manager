# tests/test_notifications.py
# Testes da mudanca de escopo — Notificacoes

from datetime import datetime, timedelta
from src.models import Usuario, Tarefa
from src.notification_service import NotificationService


class TestNotificationService:
    def test_detectar_tarefa_proxima_vencimento(self):
        """Testa se tarefas proximas ao vencimento sao detectadas."""
        user = Usuario("Laura", "l@t.com", "123")
        tarefa = Tarefa("Urgente", "Desc", "alta", user,
                       data_vencimento=datetime.now() + timedelta(days=1))
        service = NotificationService(dias_antecedencia=2)
        proximas = service.verificar_tarefas_proximas([tarefa])
        assert len(proximas) == 1

    def test_ignorar_tarefa_concluida(self):
        """Testa que tarefas concluidas nao geram notificacao."""
        user = Usuario("Laura", "l@t.com", "123")
        tarefa = Tarefa("Concluida", "Desc", "alta", user,
                       data_vencimento=datetime.now() + timedelta(days=1))
        tarefa.alterar_status("Concluido")
        service = NotificationService(dias_antecedencia=2)
        proximas = service.verificar_tarefas_proximas([tarefa])
        assert len(proximas) == 0

    def test_enviar_notificacao(self):
        """Testa o envio de notificacao."""
        user = Usuario("Laura", "l@t.com", "123")
        tarefa = Tarefa("Prazo", "Desc", "alta", user,
                       data_vencimento=datetime.now() + timedelta(days=1))
        service = NotificationService(dias_antecedencia=2)
        resultados = service.enviar_notificacoes([tarefa])
        assert len(resultados) == 1
        assert "Prazo" in resultados[0]

    def test_ignorar_tarefa_sem_vencimento(self):
        """Testa que tarefas sem data de vencimento sao ignoradas."""
        user = Usuario("Laura", "l@t.com", "123")
        tarefa = Tarefa("Sem prazo", "Desc", "media", user)
        service = NotificationService(dias_antecedencia=2)
        proximas = service.verificar_tarefas_proximas([tarefa])
        assert len(proximas) == 0

    def test_ignorar_tarefa_vencimento_distante(self):
        """Testa que tarefas com vencimento distante sao ignoradas."""
        user = Usuario("Laura", "l@t.com", "123")
        tarefa = Tarefa("Distante", "Desc", "baixa", user,
                       data_vencimento=datetime.now() + timedelta(days=30))
        service = NotificationService(dias_antecedencia=2)
        proximas = service.verificar_tarefas_proximas([tarefa])
        assert len(proximas) == 0
