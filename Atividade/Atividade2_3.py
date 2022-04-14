import cv2
import random as rd


capture = cv2.VideoCapture("IFMA Campus Caxias.mp4")

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

def ruido(frame):
    random_px = rd.randint(1000, 5000)
    for i in range(random_px):
        x = rd.randint(0, frame_height-1)
        y = rd.randint(0,frame_width-1)
        frame[x,y] = rd.randint(0, 254)
    
    return frame

print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(frame_width))
print("CV_CAP_PROP_FRAME_HEIGHT : '{}'".format(frame_height))

if not capture.isOpened():
    print("Erro ao acessar camera")
else:
    while capture.isOpened():
        ret, frame = capture.read()
        frame = ruido(frame)
        if ret is True:
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            cv2.imshow('Cinza', gray)
            
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
            
        else: break

capture.release()
cv2.destroyAllWindows()
