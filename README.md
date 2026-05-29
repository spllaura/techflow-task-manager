# TechFlow Solutions — Sistema de Gerenciamento de Tarefas

## Descricao do Projeto
Sistema web basico de gerenciamento de tarefas desenvolvido pela TechFlow Solutions
para uma startup de logistica. O sistema permite criar, visualizar, editar e excluir
tarefas, alem de filtra-las por status e prioridade.

## Objetivo
Acompanhar o fluxo de trabalho em tempo real, priorizar tarefas criticas e monitorar
o desempenho da equipe, utilizando metodologias ageis.

## Metodologia
**Kanban** — fluxo continuo com quadro visual organizado em 3 colunas:
- To Do (A Fazer)
- In Progress (Em Progresso)
- Done (Concluido)

## Tecnologias Utilizadas
- **Linguagem:** Python 3.11
- **Testes:** Pytest
- **CI/CD:** GitHub Actions
- **Gestao:** GitHub Projects (Kanban)

## Estrutura do Projeto
```
techflow-task-manager/
├── .github/workflows/ci.yml   # Pipeline de CI
├── src/
│   ├── __init__.py
│   ├── models.py               # Classes: Usuario, Tarefa, Notificacao, Relatorio
│   ├── task_manager.py          # CRUD de tarefas
│   ├── notification_service.py  # Notificacoes (mudanca de escopo)
│   └── app.py                   # Aplicacao principal
├── tests/
│   ├── __init__.py
│   ├── test_task_manager.py     # Testes unitarios e de integracao
│   └── test_notifications.py    # Testes da mudanca de escopo
├── docs/                        # Diagramas UML e prints
├── requirements.txt
└── README.md
```

## Como Executar
```bash
# Clonar o repositorio
git clone https://github.com/seuusuario/techflow-task-manager.git
cd techflow-task-manager

# Instalar dependencias
pip install -r requirements.txt

# Rodar o sistema
python -m src.app

# Rodar os testes
python -m pytest tests/ -v
```

## Mudanca de Escopo
Durante o desenvolvimento, o cliente identificou a necessidade de um **sistema de
notificacoes automaticas por e-mail** para tarefas com prazo de vencimento proximo.

**Justificativa:** Em operacoes logisticas, o nao cumprimento de prazos gera efeito
cascata em toda a cadeia de entregas. A equipe frequentemente perdia visibilidade
sobre tarefas prestes a vencer.

**Acoes tomadas:**
1. Avaliacao do impacto sobre a arquitetura
2. Criacao de novo card no Kanban
3. Implementacao do `NotificationService`
4. Criacao de testes especificos
5. Atualizacao deste README

## Testes Automatizados
O projeto utiliza **Pytest** com testes unitarios e de integracao, executados
automaticamente via **GitHub Actions** a cada push na branch main.

### Tipos de testes implementados:
- **Testes Unitarios:** Validacao de entradas, criacao/edicao/exclusao de tarefas, autenticacao
- **Testes de Integracao:** Fluxo completo criar -> editar -> concluir, geracao de relatorios
- **Testes de Notificacao:** Deteccao de prazo proximo, ignorar tarefas concluidas

### Executar testes:
```bash
python -m pytest tests/ -v
```
