# =========================
# ESTATISTICAS DA TURMA
# =========================

from sistema.gestao.auxiliares import possui_alunos
from sistema.tipos import Aluno


def mostrar_estatisticas(alunos: list[Aluno]) -> None:
    """Calcula e exibe os principais indicadores da turma."""
    if not possui_alunos(alunos):
        return
    
    total = len(alunos)
    medias = []
    
    for media_aluno in alunos:
        medias.append(media_aluno["media"])
        
    maior_media = max(medias)
    menor_media = min(medias)
    media_geral = sum(medias) / total
    
    aprovados = 0
    reprovados = 0
    
    for aluno in alunos:
        if aluno["media"] >= 7:
            aprovados += 1
        else:
            reprovados += 1
            
    print("+----------------------------+---------+")
    print("| Estatistica                | Valor   |")
    print("+----------------------------+---------+")
    print(f"| {'Total de alunos':<26} | {total:<7} |")
    print("+----------------------------+---------+")
    print(f"| {'Maior media':<26} | {maior_media:<7.2f} |")
    print(f"| {'Menor media':<26} | {menor_media:<7.2f} |")
    print(f"| {'Media geral da turma':<26} | {media_geral:<7.2f} |")
    print("+----------------------------+---------+")
    print(f"| {'Aprovados':<26} | {aprovados:<7} |")
    print(f"| {'Reprovados':<26} | {reprovados:<7} |")
    print("+----------------------------+---------+")
    
