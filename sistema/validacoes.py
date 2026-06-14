def ler_nota(mensagem):
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

def ler_texto_obrigatorio(mensagem):
    while True:
        texto = input(mensagem).strip()
        
        if texto == "":
            print("Este campo nao pode ficar vazio.")
            continue
        
        return texto
