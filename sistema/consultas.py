# =========================
# BUSCAS E FILTROS
# =========================

from sistema.validacoes import ler_nota


def mostrar_tabela_alunos(alunos, titulo):
    print(f"\n--- {titulo} ---")
    print("+----------------------+-------+")
    print("| Nome                 | Media |")
    print("+----------------------+-------+")
    for aluno in alunos:
        print(f"| {aluno['nome']:<20} | {aluno['media']:<5.2f} |")
    print("+----------------------+-------+")


def filtrar_aprovados(alunos):
    if not alunos:
        print("Lista vazia. Cadastre um aluno primeiro.")
        return
    
    aprovados = []
    
    
    for alunos_aprovados in alunos:
        if alunos_aprovados["media"] >= 7:
            aprovados.append(alunos_aprovados)
        
    if not aprovados:
        print("Nenhum aluno aprovado.")
        return
        
    mostrar_tabela_alunos(aprovados, "ALUNOS APROVADOS")
            
            
def filtrar_reprovados(alunos):
    if not alunos:
        print("Lista vazia. Cadastre um aluno primeiro.")
        return
    
    reprovados = []
    
    
    for alunos_reprovados in alunos:
        if alunos_reprovados["media"] < 7:
            reprovados.append(alunos_reprovados)
        
    if not reprovados:
        print("Nenhum aluno reprovado.")
        return
        
    mostrar_tabela_alunos(reprovados, "ALUNOS REPROVADOS")


def filtrar_por_intervalo(alunos):
    if not alunos:
        print("Lista vazia. Cadastre um aluno primeiro.")
        return
    
    media_minima = ler_nota("Digite a media minima: ")
    media_maxima = ler_nota("Digite a media maxima: ")
    
    if media_minima > media_maxima:
        print("A media minima nao pode ser maior que a media maxima.")
        return
    
    alunos_filtrados = []
    
    for aluno_filtrado in alunos:
        if media_minima <= aluno_filtrado["media"] <= media_maxima:
            alunos_filtrados.append(aluno_filtrado)
            
    if not alunos_filtrados:
        print("Nenhum aluno encontrado nesse intervalo.")
        return
    
    
    mostrar_tabela_alunos(alunos_filtrados, "ALUNOS NO INTERVALO")
        
def ordenar_por_media(alunos):
    if not alunos:
        print("Lista vazia. Cadastre um aluno primeiro.")
        return

    alunos_ordenados = sorted(alunos, key=lambda aluno: aluno["media"], reverse=True)
    
    mostrar_tabela_alunos(alunos_ordenados, "ALUNOS ORDENADOS POR MEDIA")
