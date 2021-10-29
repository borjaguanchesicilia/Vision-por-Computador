from PIL import Image
import numpy as np

imagen = Image.open("benijo.jpg", 'r')
datos = list(imagen.getdata())
col, row = imagen.size
count = 0
listaAux = []
pixels = []

for i in range(len(datos)):
    count += 1
    if(count != col):
        listaAux.append(datos[i])
    else:
        pixels.append(listaAux)
        count = 0
        listaAux = []

array = np.array(pixels, dtype=np.uint8)
new_image = Image.fromarray(array)
new_image.save('new.png')