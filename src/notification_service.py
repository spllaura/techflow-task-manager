# src/notification_service.py
# Servico de notificacoes — Mudanca de Escopo

from datetime import datetime, timedelta
from src.models import Notificacao


class NotificationService:
    """Servico que verifica tarefas proximas ao vencimento e envia notificacoes."""

    def __init__(self, dias_antecedencia=2):
        self.dias_antecedencia = dias_antecedencia
        self.notificacoes_enviadas = []

    def verificar_tarefas_proximas(self, tarefas):
        """Verifica quais tarefas estao proximas do vencimento."""
        hoje = datetime.now()
        limite = hoje + timedelta(days=self.dias_antecedencia)
        tarefas_proximas = []
        for tarefa in tarefas:
            if (tarefa.data_vencimento
                and tarefa.status != "Concluido"
                and tarefa.data_vencimento <= limite):
                tarefas_proximas.append(tarefa)
        return tarefas_proximas

    def enviar_notificacoes(self, tarefas):
        """Envia notificacoes para tarefas proximas ao vencimento."""
        tarefas_proximas = self.verificar_tarefas_proximas(tarefas)
        resultados = []
        for tarefa in tarefas_proximas:
            mensagem = (f"A tarefa '{tarefa.titulo}' vence em "
                       f"{tarefa.data_vencimento.strftime('%d/%m/%Y')}!")
            notificacao = Notificacao(mensagem, tarefa, tarefa.responsavel)
            resultado = notificacao.enviar()
            self.notificacoes_enviadas.append(notificacao)
            resultados.append(resultado)
        return resultados
