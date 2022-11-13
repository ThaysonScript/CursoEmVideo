n1 = 0
mv = 0
homem = ''
mulh = 0
for n in range(1, 5):
    print('-=-' * 5,f'[{n}]','-=-' * 8)
    nome = str(input('Digite os nomes de 4 pessoas, {} de 4: '.format(n)))
    idade = int(input('Digite as idades de 4 pessoas, {} de 4: '.format(n)))
    sexo = str(input('Digite os sexos de 4 pessoas, {} de 4: '.format(n))).upper()
    n1 = idade + n1
    if idade > mv and sexo == 'M':
        mv = idade
        print('O homem mais velho tem o nome: {}'.format(nome))
        homem = nome
    elif sexo == 'F' and idade < 20:
        mulh = mulh + 1
        print('A quantidade de mulheres menores que 20 anos sao: {}\n'.format(mulh))

media = n1 / 4
print('A media total das idades do grupo e: {}'.format(media))
print('O homem mais velho do grupo todo e: {}'.format(homem))
print('A quantidade total de mulheres menores que 20 anos no grupo sao: {}'.format(mulh))
