# =========================
# GESTAO DE ALUNOS
# =========================

from sistema.validacoes import ler_nota, ler_texto_obrigatorio


        
def calcular_media(n1, n2):
    return (n1 + n2) / 2


def cadastrar_aluno(alunos):
    if len(alunos) >= 20:
        print("Limite de 20 alunos atingido.")
        return

    nome = ler_texto_obrigatorio("Nome do aluno: ")
    n1 = ler_nota("Nota 1: ")
    n2 = ler_nota("Nota 2: ")

    aluno = {
        "nome": nome,
        "n1": n1,
        "n2": n2,
        "media": calcular_media(n1, n2),
    }
    
    alunos.append(aluno)

    print("\nAluno cadastrado com sucesso.")


def listar_alunos(alunos):
    if not alunos:
        print("lista esta vazia,cadraste aluno e tente novamente")
        return
    else:
        print("\n+----------------------+-------+-------+-------+")
        print("| Nome                 | N1    | N2    | Media |")
        print("+----------------------+-------+-------+-------+")
        for aluno in alunos:
            print(f"| {aluno['nome']:<20} | {aluno['n1']:<5.2f} | {aluno['n2']:<5.2f} | {aluno['media']:<5.2f} |")
        print("+----------------------+-------+-------+-------+")


def buscar_aluno(alunos):
    if not alunos:
        print("lista esta vazia,cadraste aluno e tente novamente")
        return

    nome_para_busca = ler_texto_obrigatorio("Digite o nome do aluno: ")

    alunos_com_nomes_parecidos = []
    for nomes_parecidos in alunos:
        if nome_para_busca.lower() in nomes_parecidos["nome"].lower():
            alunos_com_nomes_parecidos.append(nomes_parecidos)

    if not alunos_com_nomes_parecidos:
        print("Nenhum aluno encontrado.")
        return

    if len(alunos_com_nomes_parecidos) == 1:
        aluno_escolhido = alunos_com_nomes_parecidos[0]

        print("\n--- DADOS DO ALUNO ---")
        print(f"Nome: {aluno_escolhido['nome']}")
        print(f"N1: {aluno_escolhido['n1']}")
        print(f"N2: {aluno_escolhido['n2']}")
        print(f"Media: {aluno_escolhido['media']}")
        print("----------------------")
        return

    print("\n--- ALUNOS ENCONTRADOS ---")
    for i, aluno in enumerate(alunos_com_nomes_parecidos):
        print(f"{i + 1}. {aluno['nome']}")

    escolha = input("Escolha o aluno pelo numero: ")

    if not escolha.isdigit():
        print("Opcao invalida.")
        return

    indice = int(escolha) - 1
    if indice < 0 or indice >= len(alunos_com_nomes_parecidos):
        print("Opcao invalida.")
        return

    aluno_escolhido = alunos_com_nomes_parecidos[indice]

    print("\n--- DADOS DO ALUNO ---")
    print(f"Nome: {aluno_escolhido['nome']}")
    print(f"N1: {aluno_escolhido['n1']}")
    print(f"N2: {aluno_escolhido['n2']}")
    print(f"Media: {aluno_escolhido['media']}")
    print("----------------------")


def editar_aluno(alunos):
    if not alunos:
        print("Lista vazia. Cadastre um aluno primeiro.")
        return

    nome_para_busca = ler_texto_obrigatorio("Digite o nome do aluno que deseja editar: ")
    alunos_encontrados = []

    for aluno in alunos:
        if nome_para_busca.lower() in aluno["nome"].lower():
            alunos_encontrados.append(aluno)

    if not alunos_encontrados:
        print("Nenhum aluno encontrado.")
        return

    if len(alunos_encontrados) == 1:
        aluno_escolhido = alunos_encontrados[0]
    else:
        print("\n--- ALUNOS ENCONTRADOS ---")
        for i, aluno in enumerate(alunos_encontrados):
            print(f"{i + 1}. {aluno['nome']}")

        escolha = input("Escolha o aluno pelo número: ")

        if not escolha.isdigit():
            print("Opcao invalida.")
            return

        indice = int(escolha) - 1

        if indice < 0 or indice >= len(alunos_encontrados):
            print("Opcao invalida.")
            return

        aluno_escolhido = alunos_encontrados[indice]

    print("\n--- EDITAR ALUNO ---")
    print("1. Editar nome")
    print("2. Editar N1")
    print("3. Editar N2")
    print("4. Cancelar")

    opcao = input("Escolha o que deseja editar: ")

    match opcao:
        case "1":
            novo_nome = ler_texto_obrigatorio("Novo nome: ")
            aluno_escolhido["nome"] = novo_nome
            print("\nNome atualizado com sucesso.")
        case "2":
            nova_n1 = ler_nota("Nova N1: ")
            aluno_escolhido["n1"] = nova_n1
            aluno_escolhido["media"] = calcular_media(aluno_escolhido["n1"], aluno_escolhido["n2"])
            print("\nN1 atualizada com sucesso.")
        case "3":
            nova_n2 = ler_nota("Nova N2: ")
            aluno_escolhido["n2"] = nova_n2
            aluno_escolhido["media"] = calcular_media(aluno_escolhido["n1"], aluno_escolhido["n2"])
            print("\nN2 atualizada com sucesso.")
        case "4":
            print("Edicao cancelada.")
        case _:
            print("Opcao invalida.")


def excluir_aluno(alunos):
    if not alunos:
        print("Lista vazia. Cadastre um aluno primeiro.")
        return

    nome_para_busca = ler_texto_obrigatorio("Digite nome do aluno que deseja excluir: ")
    alunos_encontrados = []

    for aluno_encontrado in alunos:
        if nome_para_busca.lower() in aluno_encontrado["nome"].lower():
            alunos_encontrados.append(aluno_encontrado)

    if not alunos_encontrados:
        print("Nenhum aluno encontrado.")
        return

    if len(alunos_encontrados) == 1:
        aluno_escolhido = alunos_encontrados[0]
    else:
        print("\n--- ALUNOS ENCONTRADOS ---")
        for i, aluno in enumerate(alunos_encontrados):
            print(f"{i + 1}. {aluno['nome']}")

        escolha = input("Escolha aluno pelo numero: ")

        if not escolha.isdigit():
            print("Opcao invalida.")
            return

        indice = int(escolha) - 1

        if indice < 0 or indice >= len(alunos_encontrados):
            print("Opcao invalida")
            return

        aluno_escolhido = alunos_encontrados[indice]

    confirmacao = input(f"Tem certeza que deseja excluir {aluno_escolhido['nome']}  (s/n)")

    if confirmacao.lower() == "s":
        alunos.remove(aluno_escolhido)
        print("\nAluno excluido com sucesso")
    else:
        print("\nExclusao cancelada")
