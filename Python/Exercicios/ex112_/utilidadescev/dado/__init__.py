def leiaDinheiro(msg):
    validade = False
    while validade is False:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" e um preco invalido!\033[m')
        else:
            validade = True
            return float(entrada)
