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
        partes = texto.split()
        
        if texto == "":
            print("Este campo nao pode ficar vazio.")
            continue

        if texto.isdigit():
            print("Este campo nao pode conter apenas numeros.")
            continue
        
        if not texto.replace(" ","").isalpha(): 
            print("Este campo nao pode conter numeros,letras e caracteres especiais.")
            continue
        
        if len(partes) < 2:
            print("Digite nome e sobrenome")
            continue
        
        return texto
