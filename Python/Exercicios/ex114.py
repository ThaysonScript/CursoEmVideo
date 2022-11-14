import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('O site pudin nao esta acessivel no momento!')
else:
    print('Consegui acessar o site pudin com sucesso!')
