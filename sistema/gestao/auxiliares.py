# =========================
# FUNCOES AUXILIARES
# =========================

from sistema.validacoes import ler_termo_busca
from sistema.tipos import Aluno


def possui_alunos(alunos: list[Aluno]) -> bool:
    """Informa se ha alunos cadastrados e avisa quando a lista esta vazia."""
    if not alunos:
        print("Lista vazia. Cadastre um aluno primeiro.")
        return False
    return True


def encontrar_alunos_por_nome(alunos: list[Aluno], termo: str) -> list[Aluno]:
    """Retorna os alunos cujo nome contem o termo informado."""
    return [
        aluno
        for aluno in alunos
        if termo.lower() in aluno["nome"].lower()
    ]


def selecionar_aluno(
    alunos: list[Aluno], mensagem_busca: str
) -> Aluno | None:
    """Busca alunos e devolve o aluno selecionado pelo usuario."""
    if not possui_alunos(alunos):
        return None

    termo = ler_termo_busca(mensagem_busca)
    alunos_encontrados = encontrar_alunos_por_nome(alunos, termo)

    if not alunos_encontrados:
        print("Nenhum aluno encontrado.")
        return None

    if len(alunos_encontrados) == 1:
        return alunos_encontrados[0]

    print("\n--- ALUNOS ENCONTRADOS ---")
    for i, aluno in enumerate(alunos_encontrados, start=1):
        print(f"{i}. {aluno['nome']}")

    # Repete apenas a escolha numerica, sem obrigar uma nova busca.
    while True:
        escolha = input("Escolha o aluno pelo numero: ")

        if not escolha.isdigit():
            print("\n")
            print("===================================")
            print("         Opcao invalida            ")
            print("===================================")
            continue

        indice = int(escolha) - 1
        if indice < 0 or indice >= len(alunos_encontrados):
            print("Opcao invalida.")
            continue

        return alunos_encontrados[indice]


def mostrar_dados_aluno(aluno: Aluno) -> None:
    """Exibe os dados completos de um aluno."""
    print("\n--- DADOS DO ALUNO ---")
    print(f"Nome: {aluno['nome']}")
    print(f"N1: {aluno['n1']}")
    print(f"N2: {aluno['n2']}")
    print(f"Media: {aluno['media']}")
    print("----------------------")
