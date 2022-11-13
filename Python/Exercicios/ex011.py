metros = map(float, input().split())
larg, alt = metros
area = larg * alt
qtd_tint = area / 2
print('A area e {} e a qtd de tinta necessaria para ser pintada e {}'.format(area, qtd_tint))
