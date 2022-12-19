class Detection:
    import cv2 as cv
    import time

    # порог увереренности, отображать будем те блоки, в которых сеть уверенна на это значение и более
    CONFIDENCE_THRESHOLD = 0.2
    NMS_THRESHOLD = 0.4
    def __init__(self, class_names=["person"], yolo_cfg='detection\yolo-obj.cfg', yolo_weight='detection\yolo-obj_final.weights'):
        self.class_names = class_names
        # Подгружаем нейронку
        self.yolo = self.cv.dnn.readNetFromDarknet(yolo_cfg, yolo_weight)
        self.yolo.setPreferableBackend(self.cv.dnn.DNN_BACKEND_OPENCV)
        # модель обнаружения сети yolo
        self.model = self.cv.dnn_DetectionModel(self.yolo)
        self.model.setInputParams(size=(416, 416), scale=1/255)

    def detect(self, frame):
         # обнаружение объектов
        start_detecting = self.time.time()
        classes, scores, boxes = self.model.detect(frame, self.CONFIDENCE_THRESHOLD, self.NMS_THRESHOLD)
        end_detecting = self.time.time()
        print("start_detecting:", start_detecting)
        print("end_detecting:", end_detecting)
        return classes, scores, boxes