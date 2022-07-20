

"""
imagenes_directorio_optimizacion_1
Alejandro Vidal 
5/07/22

"""

#importamos las librerias importantes para el trabajo

#permite el trabajar con matrices y numeros usados en el calculo de imagenes
import numpy as np

#permite el trabajo con los archivos e imagenes 
import os
#importamos la libreria de la inteligencia artifical que leera las imagenes generadas
import cv2 
#se usara al final pytesseract para calcular revisar los valores
import pytesseract
#Es necesario generar escribir la direccion en la que se encuentra instalado pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\USUARIO\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

#Primero generamos una funcion para el tratamiento de los datos 

def tratamiento_imagenes(img):
    """
    generamos las variables que usaremos para el tratamiento de imagenes
    """
    #array_auxiliar sera el primero array donde generaremos y guardaremos los datos antes del tratamiento definitivo de los datos
    array_auxiliar=[]
    array_retornado=[]
    #kernel nos permite trabajar con una gamma de colores si desea cambiar los valores consulte la documentacion
    kernel=np.ones((5,5),np.uint8)

    #contadores usados para la limpieza de los datos
    Limpiador_comillas=0
    confirmador_limpiar_comillas=0

    #los valores de alphanumeric y options son usados en el tratamiento y lectura de imagenes 
    alphanumeric="0123456789"
    options="-c tessedit_char_whitelist={}".format(alphanumeric)
    options+="--psm 7"

    #empezamos el tratamiento de imagenes generando diferentes gammas de la imagen 

    #generamos el uso de cv2.COLOR_BGR2GRAY para pasar a tonos grises 
    img_Gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )

    #generamos uso del  threshold el cual establece y les genera un valor a los pixeles de la imagen en base a un pixel dato 
    img_Thereshold_1=cv2.threshold(img_Gray,50,350,cv2.THRESH_BINARY_INV)[1]
    img_Thereshold_2=cv2.threshold(img_Gray,75,350,cv2.THRESH_BINARY_INV)[1] 
    img_Thereshold_3=cv2.threshold(img_Gray,80,375,cv2.THRESH_BINARY_INV)[1]    
    img_Blur=cv2.GaussianBlur(img_Gray,(5,5),1)#genera una  imagen imagen sin blur 

    #usamos el metodo canny para generar una cilueta de la imagen
    img_Canny=cv2.Canny(img,100,100)

    #generamos una dilatacion de la imagen  en base a la cilueta de la imagen 
    img_Dilatation=cv2.dilate(img_Canny, kernel, iterations=1)

    #erosionamos la imagen 
    img_Eroded=cv2.erode(img_Dilatation,kernel,iterations=1)

    #pasamos un filtro a la imagen en blanco y negro (si se desea modificar los valores predeterminados por favor consultar documentacion sobre cv2)
    img_Gray_Black=cv2.adaptiveThreshold(img_Gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

    #invertimos las imagenes tomadas hasta ahora 
    inverte_img=cv2.bitwise_not(img)
    inverte_img_Gray=cv2.bitwise_not(img_Gray)
    inverte_img_Canny=cv2.bitwise_not(img_Canny)
    inverte_img_Dilatation=cv2.bitwise_not(img_Dilatation)
    inverte_img_Eroded=cv2.bitwise_not(img_Eroded)
    inverte_img_Thereshold_1=cv2.bitwise_not(img_Thereshold_1)
    inverte_img_Thereshold_2=cv2.bitwise_not(img_Thereshold_2)
    inverte_img_Thereshold_3=cv2.bitwise_not(img_Thereshold_3)
    inverte_img_Gray_Black=cv2.bitwise_not(img_Gray_Black) 
    inverte_img_Blur=cv2.bitwise_not(img_Blur)

    #realizamos la lectura de los datos utlizando pytesseract 

    """
    revisar clases para realizar una mejora del codigo y escritura
    """

    lectura_img=pytesseract.image_to_string(img,config=options)

    lectura_img_Gray=pytesseract.image_to_string(img_Gray,config=options)

    lectura_img_Thereshold_1=pytesseract.image_to_string(img_Thereshold_1,config=options)

    lectura__img_Thereshold_2=pytesseract.image_to_string(img_Thereshold_2,config=options)

    lectura__img_Thereshold_3=pytesseract.image_to_string(img_Thereshold_3,config=options)

    lectura_img_Blur=pytesseract.image_to_string(img_Blur,config=options)

    lectura_img_Canny=pytesseract.image_to_string(img_Canny,config=options)

    lectura_img_Dilatation=pytesseract.image_to_string(img_Dilatation,config=options)

    lectura_img_Eroded=pytesseract.image_to_string(img_Eroded,config=options)

    lectura_img_Gray_Black=pytesseract.image_to_string(img_Gray_Black,config=options)

    lectura_inverte_img=pytesseract.image_to_string(inverte_img,config=options)

    lectura_inverte_img_Gray=pytesseract.image_to_string(inverte_img_Gray,config=options)

    lectura_inverte_img_Canny=pytesseract.image_to_string(inverte_img_Canny,config=options)

    lectura_inverte_img_Blur=pytesseract.image_to_string(inverte_img_Blur,config=options)

    lectura_inverte_img_Dilatation=pytesseract.image_to_string(inverte_img_Dilatation,config=options)

    lectura_inverte_img_Eroded=pytesseract.image_to_string(inverte_img_Eroded,config=options)

    lectura_inverte_img_Thereshold_1=pytesseract.image_to_string(inverte_img_Thereshold_1,config=options)

    lectura_inverte_img_Thereshold_2=pytesseract.image_to_string(inverte_img_Thereshold_2,config=options)

    lectura_inverte_img_Thereshold_3=pytesseract.image_to_string(inverte_img_Thereshold_3,config=options)

    lectura_inverte_img_Gray_Black=pytesseract.image_to_string(inverte_img_Gray_Black,config=options)

    #ingresamos los valores al array_auxiliar para el tratamiento de datos

    array_auxiliar.append(lectura_img)
    array_auxiliar.append(lectura_img_Gray)
    array_auxiliar.append(lectura_img_Thereshold_1)
    array_auxiliar.append(lectura__img_Thereshold_2)
    array_auxiliar.append(lectura__img_Thereshold_3)
    array_auxiliar.append(lectura_img_Blur)
    array_auxiliar.append(lectura_img_Canny)
    array_auxiliar.append(lectura_img_Dilatation)
    array_auxiliar.append(lectura_img_Eroded)
    array_auxiliar.append(lectura_img_Gray_Black)
    array_auxiliar.append(lectura_inverte_img)
    array_auxiliar.append(lectura_inverte_img_Gray)
    array_auxiliar.append(lectura_inverte_img_Canny)
    array_auxiliar.append(lectura_inverte_img_Blur)
    array_auxiliar.append(lectura_inverte_img_Dilatation)
    array_auxiliar.append(lectura_inverte_img_Eroded)
    array_auxiliar.append(lectura_inverte_img_Thereshold_1)
    array_auxiliar.append(lectura_inverte_img_Thereshold_2)
    array_auxiliar.append(lectura_inverte_img_Thereshold_3)
    array_auxiliar.append(lectura_inverte_img_Gray_Black)

    #limpiamos el array_auxiliar de posibles valores =""

    while Limpiador_comillas<len(array_auxiliar):
        if array_auxiliar[Limpiador_comillas]=='':
            array_auxiliar.pop(Limpiador_comillas) 
        Limpiador_comillas+=1
    
    array_final= [x.replace('\n', '').replace('-', '') for x in array_auxiliar]

    #confirmamos que se eliminaron los vacios del array
    while confirmador_limpiar_comillas<len(array_final):
        if array_final[confirmador_limpiar_comillas]=='' or "" or " " or ' ':
            array_final.pop(confirmador_limpiar_comillas)
        confirmador_limpiar_comillas+=1

    #despues de la limpieza de los datos agregamos al array el valor mas repetido de la lectura de los datos

    appen=max(set(array_final),key=array_final.count)
    array_retornado.append(appen)
    return array_retornado


#para el tratamiento escogido se usaron 3 funciones tomando los valores de presion flujo y nivel 

def nivel(img):
    image=cv2.imread(img)
    image_nivel=image[798:852,37:185]
    valor_nivel=tratamiento_imagenes(image_nivel)
    return valor_nivel 

def presion(img):
    image=cv2.imread(img)
    image_presion=image[550:615,780:925]
    valor_presion=tratamiento_imagenes(image_presion)
    return valor_presion

def flujo(img):
    image=cv2.imread(img)
    image_flujo=image[850:925,1450:1600]
    valor_flujo=tratamiento_imagenes(image_flujo)
    return valor_flujo



#generamos la direccion a usar en el proceso 
direccion=(r"C:\Users\USUARIO\Desktop\prueba_imagen completa") 
contenido = os.listdir(direccion)
imagenes_nivel = []
imagenes_presion=[]
imagenes_flujo=[]


#por ultimo combinamos las funciones 


for fichero in contenido:
    if os.path.isfile(os.path.join(direccion, fichero)) and fichero.endswith('.png'):
        print(fichero)#se imprime el fichero para saber en que imagen se encuentra de la iteracion
        valor_nivel=nivel(fichero)
        valor_presion=presion(fichero)
        valor_flujo=flujo(fichero)
        imagenes_nivel.append(valor_nivel) 
        imagenes_presion.append(valor_presion)
        imagenes_flujo.append(valor_flujo)

#imprimimos los arrays



print('\n')
print('el flujo es \n')
print(imagenes_flujo)
print('\n')

print('el nivel es \n')
print(imagenes_nivel)
print('\n')

print('la presion es \n')
print(imagenes_presion)
print('\n')

cv2.destroyAllWindows()

print('terminado')


    

