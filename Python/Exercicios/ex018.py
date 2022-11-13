import math
ang = float(input())
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O angulo e {}\no seno e {:.2f}\no cosseno e {:.2f}\na tangente e {:.2f}'.format(ang, sen, cos, tang))
