# =========================
# SALVAR E CARREGAR DADOS
# =========================

import json
import os

CAMINHO_ARQUIVO = "dados/alunos.json"

def salvar_dados(alunos):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, ensure_ascii=False, indent=4)

def carregar_dados():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []
    
    try:
        with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as  arquivo:
            return json.load(arquivo)
    except json.JSONDecodeError:
        print("Arquivo de dados invalido. Iniciando com lista vazia.")
        return []
