# =========================
# MENUS DO SISTEMA
# =========================

from sistema.alunos import cadastrar_aluno, listar_alunos, buscar_aluno, editar_aluno, excluir_aluno
from sistema.armazenamento import salvar_dados
from sistema.consultas import filtrar_aprovados, filtrar_reprovados, filtrar_por_intervalo, ordenar_por_media
from sistema.estatisticas import mostrar_estatisticas


def mostrar_menu_principal():
    print()
    print("===========================================")
    print("sistema de gerenciamento de notas e alunos")
    print("===========================================")
    print("\n--- MENU ---")
    print("1. Gestao de alunos")
    print("2. Filtros e estatisticas")
    print("3. Salvar e sair")

def mostrar_menu_gestao_alunos():
    print()
    print(" ----------- GESTAO DE ALUNOS -----------")
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Buscar Aluno por nome")
    print("4. Editar Aluno")
    print("5. Excluir Aluno")
    print("6. voltar ao menu principal")


def mostrar_menu_filtro_estatisticas():
    print()
    print(" ----------- FILTROS E ESTATISTICAS -----------")
    print("1. Filtrar aprovados")
    print("2. Filtrar reprovados")
    print("3. Filtrar por intervalo de media")
    print("4. Ordenar por media")
    print("5. Mostrar estatisticas da turma")
    print("6. voltar ao menu principal")

def menu_principal(alunos):

    while True:
    
        mostrar_menu_principal()   
    
        opcao = input("\nSelecione uma opcao entre 1-3: ")

        match opcao:
            case "1":
                menu_gestao_alunos(alunos)
            case "2":
                menu_filtro_estatisticas(alunos)
            case "3":
                salvar_dados(alunos)
                break
            case _:
                print("Opcao invalida, insira somente as opcoes disponiveis")
                
def menu_gestao_alunos(alunos):
    while True:
        
        mostrar_menu_gestao_alunos()

        opcao = input("\nSelecione uma opcao entre 1-6: ")

        match opcao:
            case "1":
                cadastrar_aluno(alunos)
            case "2":
                listar_alunos(alunos)
            case "3":
                buscar_aluno(alunos)
            case "4":
                editar_aluno(alunos)
            case "5":
                excluir_aluno(alunos)
            case "6":
                break
            case _:
                print("Opcao invalida, insira somente as opcoes disponiveis")
        
def menu_filtro_estatisticas(alunos):
    while True:
        
        mostrar_menu_filtro_estatisticas()

        opcao = input("\nSelecione uma opcao entre 1-6: ")

        match opcao:
            case "1":
                filtrar_aprovados(alunos)
            case "2":
                filtrar_reprovados(alunos)
            case "3":
                filtrar_por_intervalo(alunos)
            case "4":
                ordenar_por_media(alunos)
            case "5":
                mostrar_estatisticas(alunos)
            case "6":
                break
            case _:
                print("Opcao invalida, insira somente as opcoes disponiveis")
