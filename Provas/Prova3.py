import cv2
import time

COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

class_names = [] 
with open("Provas/coco.names", "r") as f: 
    class_names = [cname.strip() for cname in f.readlines()]

capture = cv2.VideoCapture("videoplayback.mp4")
# capture = cv2.VideoCapture(0)

net = cv2.dnn.readNet("Provas/yolov4-tiny.weights", "Provas/yolov4-tiny.cfg")

model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416,416), scale = 1/255)

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

if(not capture.isOpened()):
    print('Erro ao exibir video')
else:
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    output = cv2.VideoWriter("videoCarDetected.avi", fourcc, int(fps), (int(frame_width), int(frame_height)))
    while capture.isOpened():
        _,frame = capture.read()

        classes, scores, boxes = model.detect(frame, 0.1, 0.2)

        for(classid,score,box) in zip(classes, scores, boxes):
            color = COLORS[ int(classid) % len(COLORS)]

            label = f"{class_names[classid]} : {score}"

            cv2.rectangle(frame, box, color, 2)
            
            cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX,0.5, color,2)

        output.write(frame)
        cv2.imshow("video", frame)
        key = cv2.waitKey(20)
        if key == ord('q'):
            break
capture.release()
cv2.destroyAllWindows()
