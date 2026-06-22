# =========================
# FUNCOES AUXILIARES
# =========================

from sistema.interface.tela import limpar_tela
from sistema.tipos import Aluno
from sistema.validacoes import ler_termo_busca


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


def selecionar_aluno(alunos: list[Aluno], mensagem_busca: str) -> Aluno | None:
    """Busca alunos e devolve o aluno selecionado pelo usuario."""
    if not possui_alunos(alunos):
        return None

    erro_busca: str | None = None
    while True:
        termo = ler_termo_busca(mensagem_busca, erro_busca)
        if termo is None:
            return None

        alunos_encontrados = encontrar_alunos_por_nome(alunos, termo)
        if not alunos_encontrados:
            erro_busca = "Nenhum aluno encontrado. Tente novamente ou digite 0 para cancelar."
            continue

        if len(alunos_encontrados) == 1:
            return alunos_encontrados[0]

        erro_escolha: str | None = None
        # Repete apenas a escolha numerica, sem obrigar uma nova busca.
        while True:
            limpar_tela()
            print("\n--- ALUNOS ENCONTRADOS ---")
            for i, aluno in enumerate(alunos_encontrados, start=1):
                print(f"{i}. {aluno['nome']}")
            print("0. Cancelar")
            if erro_escolha:
                print(f"\n{erro_escolha}")

            escolha = input("Escolha o aluno pelo numero: ")

            if escolha == "0":
                return None

            if not escolha.isdigit():
                erro_escolha = "Opcao invalida."
                continue

            indice = int(escolha) - 1
            if indice < 0 or indice >= len(alunos_encontrados):
                erro_escolha = "Opcao invalida."
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
