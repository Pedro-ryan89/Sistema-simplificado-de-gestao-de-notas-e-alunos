from sistema.interface.menus import menu_principal
from sistema.persistencia.armazenamento import carregar_dados
from sistema.tipos import Aluno


alunos: list[Aluno] = carregar_dados()
menu_principal(alunos)
