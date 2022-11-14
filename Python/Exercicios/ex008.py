medida = float(input())
km = medida / 1000
hctm = medida / 100
dam = medida / 10
m = medida
dm = medida * 10
cm = medida * 100
mm = medida * 1000
cores = {'vermelho':'\033[29;41m',
         'limpar':'\033[m'}
print('{}km = {}{}'.format(cores['vermelho'], km, cores['limpar']))
print('{}hctm = {}{}'.format(cores['vermelho'], hctm, cores['limpar']))
print('{}dam = {}{}'.format(cores['vermelho'], dam, cores['limpar']))
print('{}m = {}{}'.format(cores['vermelho'], m, cores['limpar']))
print('{}dm = {}{}'.format(cores['vermelho'], dm, cores['limpar']))
print('{}cm = {}{}'.format(cores['vermelho'], cm, cores['limpar']))
print('{}mm = {}{}'.format(cores['vermelho'], mm, cores['limpar']))