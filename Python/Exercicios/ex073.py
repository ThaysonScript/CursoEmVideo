tabela = ('Palmeiras', 'Internacional', 'Flamengo', ' Fluminense',
          'Corinthians', 'Atletico Paranaence', 'Atletico Mineiro',
          'America', 'Fortaleza', 'Sao Paulo', 'Botafogo', 'Santos',
          'Bragantino', 'Goias', 'Curitiba', 'Ceara', 'Cuiaba',
          'Goianiense', 'Avai', 'Chapecoense')
print('-=-'*15)
print(f'Lista de times do brasileirao: {tabela}')
print('-=-'*15)
print(f'Os 5 primeiros na tabela sao: {tabela[0:5]}')
print('-=-'*15)
print(f'Os 4 ultimos na tabela sao: {tabela[-4:]}')
print('-=-'*15)
print(f'Os times em ordem alfabetica sao: {sorted(tabela)}')
print('-=-'*15)
print(f'O Chapecoense esta na {tabela.index("Chapecoense")+1} posicao')