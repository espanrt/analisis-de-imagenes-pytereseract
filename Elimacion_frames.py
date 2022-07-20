
"""
Eliminacion de frames 
Alejandro Vidal 
5/07/22

"""

import os 

i=0 # generamos un contador inicializado en la primera imagen 
j=100 #terminamos el contador en la ultima imagen generada estandar de 100 
l=str(i)
while i<=j:
    if i%15==0:
        i+=1
        continue
    else:
        os.remove("photo_%06d.png"%i)
        i+=1

    print(i)
print("terminado")
