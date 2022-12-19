class Video:
    import cv2 as cv
    import sys
    import PIL
    import video.distanse as distanse

    # цвета
    BLUE = (255, 234, 0)
    RED = (0, 51, 255)
    BLACK = (0, 0, 0)

    def __init__(self, filepath, detection, focus_direction_camera):
        self.filepath = filepath
        self.detection = detection
        self.video_capture = self.cv.VideoCapture(self.filepath)
        self.video_fps = int(self.video_capture.get(self.cv.CAP_PROP_FPS))
        self.video_size = (int(self.video_capture.get(self.cv.CAP_PROP_FRAME_WIDTH)),
                           int(self.video_capture.get(self.cv.CAP_PROP_FRAME_HEIGHT)))
        self.video_central_frame = (self.video_size[0] / 2, self.video_size[1] / 2)
        self.distanse_objs = self.distanse.Distanse(focus_direction_camera, self.video_central_frame)

    def drawDetectingData(self, frame, classes, scores, boxes, lines):
        for (classid, score, box) in zip(classes, scores, boxes):
            # подпись
            label = "%s : %f" % (self.detection.class_names[0], score)
            label = label.upper()
            # рамка для человека (на основе данных x, y верхнего левого угла, w, h рамки)
            self.cv.rectangle(frame, box, self.BLUE, 2)
            # размещаем подпись над коробкой
            self.cv.putText(frame, label, (box[0], box[1] - 10), self.cv.FONT_HERSHEY_SIMPLEX, 0.5, self.RED, 2)
            # чертим линии расстояний между людьми, пишем расстояние над линией в метрах
            for line in lines:
                self.cv.line(frame, line[0], line[1], self.BLACK, 2)
                label_dist = "{:.1f}m".format(line[2])
                self.cv.putText(
                    frame,
                    label_dist,
                    (int((line[0][0] + line[1][0]) * 0.5),
                     int((line[0][1] + line[1][1]) * 0.5)),
                    self.cv.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    self.RED,
                    2
                )

    def getFrame(self):
        ret, frame = self.video_capture.read()
        frame = self.frameToBlackAndWhite(frame)
        classes, scores, boxes = self.detection.detect(frame)
        lines = self.distanse_objs.getDistBetweenObj(boxes)
        self.drawDetectingData(frame, classes, scores, boxes, lines)
        return (ret, frame)

    def frameToBlackAndWhite(self, frame):
        return frame
