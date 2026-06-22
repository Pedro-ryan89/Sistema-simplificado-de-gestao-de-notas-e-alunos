"""Funcoes de validacao das entradas do usuario."""

from sistema.interface.tela import limpar_tela


def ler_nota(mensagem: str) -> float:
    """Solicita uma nota valida entre 0 e 10."""
    erro: str | None = None
    while True:
        limpar_tela()
        if erro:
            print(erro)

        entrada = input(mensagem)
        try:
            nota = float(entrada)
        except ValueError:
            erro = "Digite uma nota valida."
            continue

        if nota < 0 or nota > 10:
            erro = "A nota deve estar entre 0 e 10."
            continue

        return nota

def ler_texto_obrigatorio(mensagem: str) -> str:
    """Solicita um nome completo formado apenas por letras e espacos."""
    erro: str | None = None
    while True:
        limpar_tela()
        if erro:
            print(erro)

        texto = input(mensagem).strip()
        partes = texto.split()

        if texto == "":
            erro = "Este campo nao pode ficar vazio."
            continue

        if texto.isdigit():
            erro = "Este campo nao pode conter apenas numeros."
            continue

        if not texto.replace(" ", "").isalpha():
            erro = "Este campo deve conter apenas letras e espacos."
            continue

        if len(partes) < 2:
            erro = "Digite nome e sobrenome."
            continue

        
        return texto

def ler_termo_busca(
    mensagem: str, erro_inicial: str | None = None
) -> str | None:
    """Solicita um termo de busca ou devolve None quando o usuario cancela."""
    erro = erro_inicial

    while True:
        limpar_tela()
        print("Digite 0 para cancelar.")
        if erro:
            print(erro)

        texto = input(mensagem).strip()

        if texto == "0":
            return None

        if not texto:
            erro = "Este campo nao pode ficar vazio."
            continue

        if not texto.replace(" ", "").isalpha():
            erro = "Digite apenas letras e espacos."
            continue

        return texto
