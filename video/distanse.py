class Distanse:
    from scipy.spatial import distance as dist
    from math import sqrt
    # рост человека среднестатистического человека 
    BASE_HEIGHT_PERSON = 170

    def __init__(self, focus_direction_camera, video_central_frame):
        self.focus_direction_camera = focus_direction_camera
        self.video_central_frame = video_central_frame

    def getCentralPoint(self, coord_tl, size):
        top_left_x, top_left_y = coord_tl
        height, width = size
        central_x = abs(top_left_x + width / 2)
        central_y = abs(top_left_y + height / 2)
        return central_x, central_y

    def getDistCameraToObjInCm(self, height_object_px):
        return (self.BASE_HEIGHT_PERSON * self.focus_direction_camera) / height_object_px

    def getDistBetweenTwoObjOnZAxis(self, coord_center_obj1, height_obj1, coord_center_obj2, height_obj2):
        # сколько пикселей в сантиметре для 1 и 2
        px_in_cm_obj1, px_in_cm_obj2 = height_obj1 / self.BASE_HEIGHT_PERSON, height_obj2 / self.BASE_HEIGHT_PERSON
        # расстояние от камеры до объекта в px
        camera_to_obj1, camera_to_obj2 = self.getDistCameraToObjInCm(height_obj1), self.getDistCameraToObjInCm(
            height_obj2)
        # расстояние от центра кадра до объекта в см
        dist_center_frame_to_obj1 = self.dist.euclidean(self.video_central_frame, coord_center_obj1) / px_in_cm_obj1
        dist_center_frame_to_obj2 = self.dist.euclidean(self.video_central_frame, coord_center_obj2) / px_in_cm_obj2
        # расстояние от камеры до центра кадра для 1 и 2 объекта
        camera_to_center_obj1 = self.sqrt(abs(camera_to_obj1 ** 2 - dist_center_frame_to_obj1 ** 2))
        camera_to_center_obj2 = self.sqrt(abs(camera_to_obj2 ** 2 - dist_center_frame_to_obj2 ** 2))
        # разница эnих расстояний и есть глубина (растояние по оси z) 
        dist_z = abs(camera_to_center_obj1 - camera_to_center_obj2)
        return dist_z

    def getDistBetweenObj(self, boxes):
        distances = []
        if len(boxes) > 1:
            for first in range(len(boxes) - 1):
                for next in range(first + 1, len(boxes)):
                    # w, h, x, y для первого человека 
                    size_first = (boxes[first][3], boxes[first][2])
                    coord_tl_first = (boxes[first][0], boxes[first][1])
                    # w, h, x, y для следующего человека
                    size_next = (boxes[next][3], boxes[next][2])
                    coord_tl_next = boxes[next][0], boxes[next][1]
                    # координаты центра первого человека 
                    coord_center_first = self.getCentralPoint(coord_tl_first, size_first)
                    # координаты центра второго человека 
                    coord_center_next = self.getCentralPoint(coord_tl_next, size_next)
                    distanse_z = self.getDistBetweenTwoObjOnZAxis(coord_center_first, size_first[0], coord_center_next,
                                                                  size_next[0])
                    distanse_x = abs(coord_center_first[0] - coord_center_next[0])
                    # расстояние между двумя людьми, итоговый результат
                    dist_first_to_next = self.sqrt(distanse_z ** 2 + distanse_x ** 2) / 100
                    distances.append(
                        [(int(coord_center_first[0]), int(coord_center_first[1])),
                         (int(coord_center_next[0]), int(coord_center_next[1])),
                         dist_first_to_next]
                    )
        return distances
