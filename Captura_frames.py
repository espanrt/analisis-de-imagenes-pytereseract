#frames captura frames 


"""
Captura de frames 
Alejandro Vidal 
5/07/22

"""

import cv2
video_path=('C:\\Users\\USUARIO\\Desktop\\universidad\\Dinamica\\Proceso de imagenes\\comportamiento\\video\\COMP. DIANAMICO (2 FPS).mkv') #camino del video 
cap=cv2.VideoCapture(video_path)
img_index=0
while(cap.isOpened()):
    ret,frames=cap.read()
    if ret==False:
        break   
    cv2.imwrite('photo_%06d.png'%img_index,frames)
    img_index+=1
cap.release()
cv2.destroyAllWindows()

print('proceso de captura terminado')
