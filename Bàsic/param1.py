#!/usr/bin/python
import sys    # per importar la llibreria necessària
if(len(sys.argv) > 1):     # si el nombre de parámetres és superior a 1. és a dir, n’hi han
    print("Obrint " + sys.argv[1])   # et mostra el primer paràmetre
else:
    print("Has d'indicar el nom de l'arxiu")
