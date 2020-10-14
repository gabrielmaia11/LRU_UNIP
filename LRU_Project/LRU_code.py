"""
Algoritmo de substituição de páginas feito em Python apresentado ao Professor Ricardo Piantola
da Unip Campus Paraíso. Sistemas de Informação, TURMA SI5P68

                                                                                Gabriel Maia - N3610F-8
"""

import time
P1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
memoriaRam = [0, 0, 0]
pontP1 = 0
pontMemoriaRAM = 0
falta_pagina = 0
while True:
  if pontMemoriaRAM < 3:
    memoriaRam[pontMemoriaRAM] = P1[0]
    for i in range(len(P1)):
      if i < len(P1)-1:
        P1[i] = P1[i+1]
    pontMemoriaRAM = pontMemoriaRAM + 1
    P1.pop()
  else:
    pontMemoriaRAM = 0
    memoriaRam[pontMemoriaRAM] = P1[0]
    for i in range(len(P1)):
      if i < len(P1)-1:
        P1[i] = P1[i+1]
    pontMemoriaRAM = pontMemoriaRAM + 1
    P1.pop()
  pontP1 = pontP1 + 1
  print(memoriaRam)
  print(P1)
  if pontMemoriaRAM != memoriaRam:
    falta_pagina = falta_pagina + 1
    print("Houve " + str(falta_pagina) + " faltas de páginas")
    time.sleep(1)
time.sleep(1)
