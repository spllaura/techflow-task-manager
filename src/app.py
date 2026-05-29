# src/app.py
# Aplicacao principal — TechFlow Solutions

from src.task_manager import TaskManager


def main():
    print("=" * 50)
    print("  TechFlow Solutions - Gerenciador de Tarefas")
    print("=" * 50)

    manager = TaskManager()

    # Cadastrar usuarios
    admin = manager.cadastrar_usuario("Laura Admin", "admin@techflow.com", "admin123", "admin")
    user = manager.cadastrar_usuario("Joao Dev", "joao@techflow.com", "joao123", "comum")
    print(f"\n>>> {admin.cadastrar()}")
    print(f">>> {user.cadastrar()}")

    # Criar tarefas
    t1 = manager.criar_tarefa("Configurar banco de dados", "Instalar e configurar PostgreSQL", "alta", admin)
    t2 = manager.criar_tarefa("Criar tela de login", "Implementar autenticacao", "alta", user)
    t3 = manager.criar_tarefa("Escrever documentacao", "Atualizar README.md", "media", admin)
    t4 = manager.criar_tarefa("Corrigir bug no filtro", "Filtro de status nao funciona", "baixa", user)

    print(f"\nTarefas criadas: {len(manager.listar_tarefas())}")

    # Alterar status
    t1.alterar_status("Em Progresso")
    t2.alterar_status("Concluido")

    # Filtrar
    em_progresso = manager.filtrar_por_status("Em Progresso")
    print(f"\nEm Progresso: {[t.titulo for t in em_progresso]}")

    alta_prioridade = manager.filtrar_por_prioridade("alta")
    print(f"Alta prioridade: {[t.titulo for t in alta_prioridade]}")

    # Editar
    manager.editar_tarefa(t3.id, titulo="Escrever documentacao completa")
    print(f"\nTarefa {t3.id} editada: '{t3.titulo}'")

    # Excluir
    resultado = manager.excluir_tarefa(t4.id)
    print(f"{resultado}")
    print(f"Tarefas restantes: {len(manager.listar_tarefas())}")


if __name__ == "__main__":
    main()
