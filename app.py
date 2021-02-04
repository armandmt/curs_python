import platform
import os
import time


def executar_comandament(cmd1,cmd2):
    print("Netejar pantalla...")
    time.sleep(2)
    os.system(cmd1)
    print("Llistat fitxers...")
    time.sleep(1)
    os.system(cmd2)

    print("Llistat fitxers  del directori pare...")
    time.sleep(1)
    os.chdir("../") 
    time.sleep(1)
    os.system(cmd2)
if platform.system() == "Windows":
    # lllançar comandaments propis de Windows
    #cls,dir
    executar_comandament("cls","dir")
else:
    #comandaments propis de Linux/Mac
    #clear,ls -lrt
    executar_comandament("clear","ls -lrt")
