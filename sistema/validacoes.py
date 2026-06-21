"""Funcoes de validacao das entradas do usuario."""


def ler_nota(mensagem: str) -> float:
    """Solicita uma nota valida entre 0 e 10."""
    while True:
        entrada = input(mensagem)
        try:
            nota = float(entrada)
        except ValueError:
            print("Digite uma nota valida")
            continue

        if nota < 0 or nota > 10:
            print("A nota deve estar entre 0 e 10")
            continue

        return nota

def ler_texto_obrigatorio(mensagem: str) -> str:
    """Solicita um nome completo formado apenas por letras e espacos."""
    while True:
        texto = input(mensagem).strip()
        partes = texto.split()

        if texto == "":
            print("Este campo nao pode ficar vazio.")
            continue

        if texto.isdigit():
            print("Este campo nao pode conter apenas numeros.")
            continue

        if not texto.replace(" ", "").isalpha():
            print("Este campo deve conter apenas letras e espaços.")
            continue
        
        if len(partes) < 2:
            print("Digite nome e sobrenome")
            continue

        
        return texto

def ler_termo_busca(mensagem: str) -> str:
    """Solicita um termo valido para buscar alunos por nome."""

    while True:
        texto = input(mensagem).strip()

        if not texto:
            print("Este campo nao pode ficar vazio.")
            continue

        if not texto.replace(" ", "").isalpha():
            print("Digite apenas letras e espacos.")
            continue

        return texto
