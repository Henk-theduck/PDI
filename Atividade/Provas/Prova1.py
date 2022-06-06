#1-Utilizar o processo de Inpaint para remover a logomarca no canto superior direito do vídeo.
#2-Utilizar a tecla 'a' para alterar o aspect ratio do vídeo para alterá-lo entre 16:9 (padrão do vídeo) e 4:3.
# 3-Utilizar a tecla 'c' para realizar um recorte na parte central do vídeo para aterá-lo entre 16:9 (padrão do vídeo) e 4:3.
import cv2
import numpy as np

# Imports
capture = cv2.VideoCapture('IFMA Campus Caxias.mp4')
logo = cv2.imread('logo-if-vertical.png')

# Redimensão da logo
logo = cv2.resize(logo,(153,208), interpolation=cv2.INTER_AREA)
rows, cols = logo.shape[0:2]
gray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray,125, 255,cv2.THRESH_BINARY_INV) # mascara


#dimensoes do video
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH) #largura
frame_heigth = capture.get(cv2.CAP_PROP_FRAME_HEIGHT) # altura
fps = capture.get(cv2.CAP_PROP_FPS)
print("WIDTH: '{}' ".format(frame_width))
print("HEIGTH: '{}' ".format(frame_heigth))

#define o lugar onde a logo ira ficar
cropX = frame_width - cols #define o inicio no eixo x
cropY = 0

widthResize = 1280

# adiciona a logo frame a frame
def removeLogo(img):
    imgCrop = img[0:rows,int(cropX):int(frame_width)]
    ns = cv2.inpaint(imgCrop,mask,3,cv2.INPAINT_NS)
    img[0:rows,int(cropX):int(frame_width)] = ns
    return img

def aspectRatio(img, width):
    img = cv2.resize(img, (width,720), interpolation=cv2.INTER_AREA)
    return img

def clippingVideo(img):
    return img

    

if(not capture.isOpened()):
    print('Erro ao exibir video')
else:
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    output = cv2.VideoWriter('video_com_logo.avi', fourcc, int(fps),(int(frame_width), int(frame_heigth)))

    while capture.isOpened():
        ret,frame = capture.read()
        key = cv2.waitKey(20)
        if key == ord('q'):
                break
        if key == ord('a'):
                print('Original', frame.shape)
                print('a')
                if widthResize == 1280:
                    widthResize = 960
                    print('re', frame.shape)
                else:
                    widthResize = 1280
                    print('Original', frame.shape)
                print('widthResize', widthResize)
        if ret is True:
            # frame = removeLogo(frame)
            frame = aspectRatio(frame, widthResize)
            cv2.imshow('Video com logo', frame)
            

        else: break
capture.release()
cv2.destroyAllWindows()
