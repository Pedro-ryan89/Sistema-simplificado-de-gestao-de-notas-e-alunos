# =========================
# GESTAO DE ALUNOS
# =========================

from sistema.gestao.auxiliares import mostrar_dados_aluno, possui_alunos, selecionar_aluno
from sistema.interface.tela import limpar_tela
from sistema.tipos import Aluno
from sistema.validacoes import ler_nota, ler_texto_obrigatorio


def calcular_media(n1: float, n2: float) -> float:
    """Calcula a media aritmetica de duas notas."""
    return (n1 + n2) / 2


def cadastrar_aluno(alunos: list[Aluno]) -> None:
    """Solicita os dados e adiciona um novo aluno a lista."""

    if len(alunos) >= 20:
        print("Limite de 20 alunos atingido.")
        return

    nome = ler_texto_obrigatorio("Nome do aluno: ")
    n1 = ler_nota("Nota 1: ")
    n2 = ler_nota("Nota 2: ")

    aluno: Aluno = {
        "nome": nome,
        "n1": n1,
        "n2": n2,
        "media": calcular_media(n1, n2),
    }

    alunos.append(aluno)

    print("\nAluno cadastrado com sucesso.")


def listar_alunos(alunos: list[Aluno]) -> None:
    """Exibe uma tabela com todos os alunos cadastrados."""
    if not possui_alunos(alunos):
        return

    print("\n+----------------------+-------+-------+-------+")
    print("| Nome                 | N1    | N2    | Media |")
    print("+----------------------+-------+-------+-------+")
    for aluno in alunos:
        print(f"| {aluno['nome']:<20} | {aluno['n1']:<5.2f} | {aluno['n2']:<5.2f} | {aluno['media']:<5.2f} |")
    print("+----------------------+-------+-------+-------+")


def buscar_aluno(alunos: list[Aluno]) -> None:
    """Localiza e mostra os dados de um aluno."""
    aluno_escolhido = selecionar_aluno(alunos, "Digite o nome do aluno: ")

    if aluno_escolhido:
        mostrar_dados_aluno(aluno_escolhido)


def editar_aluno(alunos: list[Aluno]) -> None:
    """Permite alterar o nome ou as notas de um aluno selecionado."""
    aluno_escolhido = selecionar_aluno(
        alunos, "Digite o nome do aluno que deseja editar: "
    )

    if not aluno_escolhido:
        return

    mensagem: str | None = None
    while True:
        limpar_tela()
        print("\n--- EDITAR ALUNO ---")
        print("1. Editar nome")
        print("2. Editar N1")
        print("3. Editar N2")
        print("4. Cancelar")
        if mensagem:
            print(f"\n{mensagem}")

        opcao = input("Escolha o que deseja editar: ")

        match opcao:
            case "1":
                novo_nome = ler_texto_obrigatorio("Novo nome: ")
                aluno_escolhido["nome"] = novo_nome
                mensagem = "Nome atualizado com sucesso."
            case "2":
                nova_n1 = ler_nota("Nova N1: ")
                aluno_escolhido["n1"] = nova_n1
                aluno_escolhido["media"] = calcular_media(aluno_escolhido["n1"], aluno_escolhido["n2"])
                mensagem = "N1 atualizada com sucesso."
            case "3":
                nova_n2 = ler_nota("Nova N2: ")
                aluno_escolhido["n2"] = nova_n2
                aluno_escolhido["media"] = calcular_media(aluno_escolhido["n1"], aluno_escolhido["n2"])
                mensagem = "N2 atualizada com sucesso."
            case "4":
                print("\nEdicao cancelada.")
                break
            case _:
                mensagem = "Opcao invalida."
                continue


def excluir_aluno(alunos: list[Aluno]) -> None:
    """Remove um aluno apos confirmacao do usuario."""
    if not possui_alunos(alunos):
        return

    while True:
        aluno_escolhido = selecionar_aluno(
            alunos, "Digite nome do aluno que deseja excluir: "
        )

        if not aluno_escolhido:
            return

        erro_confirmacao: str | None = None
        while True:
            limpar_tela()
            print("\n--- EXCLUIR ALUNO ---")
            print(f"Aluno: {aluno_escolhido['nome']}")
            if erro_confirmacao:
                print(f"\n{erro_confirmacao}")

            confirmacao = input(
                f"Tem certeza que deseja excluir {aluno_escolhido['nome']}? (s/n): "
            )

            if confirmacao.lower() == "s":
                alunos.remove(aluno_escolhido)
                print("\nAluno excluido com sucesso.")
                return
            if confirmacao.lower() == "n":
                print("\nExclusao cancelada.")
                return

            erro_confirmacao = "Opcao invalida. Digite s ou n."
