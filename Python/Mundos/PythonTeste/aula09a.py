#strings:

#fatiamentro:

#[:5] vai de 0 ate o 5 tirando o 5, ou seja, ate o 4
#[5:] vai do 5 ate o final da string, tirando o caracter final
#[0:10:2] vai de 0 ate o 10, de 2 em 2 e tirando o 10, ou seja, ate o 9

#.len() faz com que conte o tamanho da string

#.count() faz com que procure e diga quantos caracteres
# tem dentro da string
#mesmos parametros do fatiamento da string
#mas com '' para procurar o caracter
#e substituindo o : por ,

#.find() encontra uma determinada frase dentro da string
#ele mostra em que posicao a frase comeca na string
#se der um caracter que nao aparece na string ele retorna -1

#'caracter' in string
# esse 'in' verifica se o caracter pertence a string, true ou false

#transformacao:

#.replace() ele pega um caracter e substitui por outro na string
#ex = frase.replace('python', 'android') troca python por android na string frase

#.upper() coloca tudo em maiusculo

#.lower() coloca tudo em minusculo

#.capitalize() coloca tudo para minusculo e apenas o primeiro caracter fica em maiusculo

#.title() coloca por meio de separacao de espacos na string os primeiros caracteres em maiusculo

#ex: frase = ['curso em video python']
# frase.title()
# nova_frase = ['Curso Em Video Python']

#.strip() remove espacos no comeco e fim da string

#.rstrip() remove espacos da direita da string, espacos que tem no final

#.lstrip() remove espacos da esquerda da string, espacos que tem no inicio da string

#divisao:

#.split() divide uma string, quando tem espacos em outras strings, listas
#ex: frase = ['curso em video python']
#frase.split()
# frase = ['curso', 'em', 'video', 'python']
#usando print([0] [4])
#vai pegar 'curso' e printar o caracter 'o'

#juncao:

# ''.join() junta uma string, em relacao aonde tinha espacos

#ex: frase = ['curso em video python']
# '-'.join(frase)
# frase = ['curso-em-video-python']

#Dicas:

print('''fhfjgfasfgfgfgffgfg
fhfhfhffhfhfhfhfh
fhfhfhfhfhfhhfhfh
fhffhfhfhfhfhfhfhf''') #vai printar a string toda pelo '''