from copy import copy
from random import randint
import cv2

# BLUE = (255, 0, 0)
# GREEN = (0,255, 0)
# RED = (0, 0, 255)
# BLACK = (0,0,0)
# GRAY = (125, 125, 125)

# COLORS = [BLUE, GREEN, RED, BLACK, GRAY]

# c=0

# def draw_circle(event,x,y,flags,param):
#     global c
#     if event == cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(frame,(x,y),3,COLORS[c],-1)

capture = cv2.VideoCapture("IFMA Campus Caxias.mp4")

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_heigth = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)
print("WIDTH: '{}' ".format(frame_width))
print("HEIGTH: '{}' ".format(frame_heigth))

if (not capture.isOpened()):
    print("Erro ao exibir video")
else:
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    output = cv2.VideoWriter("video_rabiscado.avi", fourcc, int(fps), (int(frame_width), int(frame_heigth)), True)

    # cv2.namedWindow('Input')
    # cv2.setMouseCallback('Input', draw_circle)
    while capture.isOpened():
        ret, frame = capture.read()
        
        if ret is True:

            #Pra desenhar, percebi que tem que salvar a coordenada do ponto
            #Mesmo assim, não consegui fazer :)

            

            #Nao consegui salvar uma copia, ou seja, não fiz nada 
            clone = frame.copy()
            
            output.write(clone)
           
            cv2.imshow('Input', frame)
            
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
            # if cv2.waitKey(20) & 0xFF == ord('c'):
            #    print('c pressionado')
            #    c = randint(0, len(COLORS)-1)
            # if cv2.waitKey(20) & 0xFF == ord(' '):
            #     print("espaco pressionado")
            #     frame = clone_frame
        else: break

capture.release()
output.release()
cv2.destroyAllWindows()

