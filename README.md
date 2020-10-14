# LRU_UNIP

O trabalho diz respeito ao algoritmo de troca de páginas, mais especificamente, o LRU (Least Recently Used) ou Menos Recentemente Usado, em português. 	
Este algoritmo parte do pressuposto que as páginas utilizadas recentemente irão retornar a serem usadas num futuro breve, então ele acaba substituindo as páginas que estão há bastante tempo sem uso. Mas como tudo tem seu lado ruim, com o algoritmo LRU não é diferente. O LRU deixa uma lista encadeada de todas as páginas que ficam na memória, e isso acaba sendo muito caro, pois a lista é reordenada toda vez que existe uma referência à memória.
