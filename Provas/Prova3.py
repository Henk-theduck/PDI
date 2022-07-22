import cv2
import time

COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0), (0, 0, 255)]

class_names = [] 
with open("Provas/coco.names", "r") as f: 
    class_names = [cname.strip() for cname in f.readlines()]

capture = cv2.VideoCapture("Provas/videoplayback.mp4")
# capture = cv2.VideoCapture(0)

net = cv2.dnn.readNet("Provas/yolov4-tiny.weights", "Provas/yolov4-tiny.cfg")

model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416,416), scale = 1/255)

if(not capture.isOpened()):
    print('Erro ao exibir video')
else:
    while capture.isOpened():
        _,frame = capture.read()

        start = time.time()

        classes, scores, boxes = model.detect(frame, 0.1, 0.2)

        end = time.time()

        for(classid,score,box) in zip(classes, scores, boxes):

            color = COLORS[ int(classid) % len(COLORS)]

            # label = f"{class_names[classid[0]]} : {score}"

            cv2.rectangle(frame, box, color, 2)
            
            # cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX,0.5, color,2)

        fps_label = f"FPS: {round((1.0/(end -start)),2)}"

        cv2.putText(frame, fps_label, (0,25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 5)
        cv2.putText(frame, fps_label, (0,25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)

        cv2.imshow("video", frame)
        key = cv2.waitKey(20)
        if key == ord('q'):
            break
capture.release()
cv2.destroyAllWindows()
