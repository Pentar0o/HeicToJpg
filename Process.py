#-*- coding: utf-8 -*-

import os
import time
import sys
import whatimage
import pyheif
import io
from PIL import Image


def decodeImage(nomfichier, repertoire, bytesIo):
    print(nomfichier)
    os.path.join(repertoire)
    fmt = whatimage.identify_image(bytesIo)
    if fmt in ['heic', 'avif']:
        i = pyheif.read_heif(bytesIo)
        pi = Image.frombytes(mode=i.mode, size=i.size, data=i.data)
        pi.save(nomfichier[:-4]+'jpg', format="jpeg")



def main(repertoire): 
    for filename in os.listdir(repertoire):
        fichier = os.path.join(repertoire, filename)
        img = open(fichier,'rb')
        decodeImage(filename, repertoire, img.read())      
        print(filename +  ': Opération Réussie !')

#Main Code
if __name__ == '__main__':
    if len(sys.argv) <= 0:
        print('USAGE: repertoire')
    else:
        t1 = time.time()
        main(sys.argv[1])
        print('Temps de Traitement : %d ms'%((time.time()-t1)*1000))
