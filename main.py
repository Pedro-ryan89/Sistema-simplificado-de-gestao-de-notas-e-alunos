from sistema.menus import menu_principal
from sistema.armazenamento import carregar_dados


alunos = carregar_dados()
menu_principal(alunos)

