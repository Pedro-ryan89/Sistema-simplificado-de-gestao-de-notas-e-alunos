"""Funcoes para controlar a exibicao das telas no terminal."""

import os


def limpar_tela() -> None:
    """Limpa a area visivel do terminal em Windows, Linux e macOS."""
    comando = "cls" if os.name == "nt" else "clear"
    os.system(comando)


def pausar() -> None:
    """Espera o usuario ler o resultado antes de trocar de tela."""
    input("\nPressione Enter para continuar...")
