"""Tipos compartilhados pelo sistema."""

from typing import TypedDict


class Aluno(TypedDict):
    """Estrutura de dados usada para representar um aluno."""
    
    nome: str
    n1: float
    n2: float
    media: float
