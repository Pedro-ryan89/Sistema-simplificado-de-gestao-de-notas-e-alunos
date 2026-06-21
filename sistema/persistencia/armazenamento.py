# =========================
# SALVAR E CARREGAR DADOS
# =========================

import json
import os

from sistema.tipos import Aluno


CAMINHO_ARQUIVO: str = "dados/alunos.json"


def salvar_dados(alunos: list[Aluno]) -> None:
    """Salva a lista de alunos no arquivo JSON."""
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, ensure_ascii=False, indent=4)

def carregar_dados() -> list[Aluno]:
    """Carrega os alunos salvos ou devolve uma lista vazia."""
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []
    
    try:
        with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except json.JSONDecodeError:
        # Impede que um JSON corrompido interrompa a execucao do programa.
        print("Arquivo de dados invalido. Iniciando com lista vazia.")
        return []
