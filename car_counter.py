import imutils
from cvlib.object_detection import YOLO

YOLO_WEIGHTS_PATH = 'dataset/custom_yolo_weights/yolov7-tiny-custom_best.weights'
YOLO_CFG_PATH = 'dataset/custom_yolo_weights/yolov7-tiny-custom.cfg'
YOLO_NAMES_PATH = 'dataset/custom_yolo_weights/obj.names'

yolo = YOLO(YOLO_WEIGHTS_PATH, YOLO_CFG_PATH, YOLO_NAMES_PATH, version='yolov7-tiny')


def car_counter(frame, target_labels, debug_log=False):
    object_count = 0

    image_width = frame.shape[1] // 2
    image_height = frame.shape[0] // 2
    frame = imutils.resize(frame, width=image_width, height=image_height)

    bbox, label, conf = yolo.detect_objects(frame)
    if debug_log:
        print(bbox, label, conf)
    for current_label in target_labels:
        object_count += label.count(current_label)
    yolo.draw_bbox(frame, bbox, label, conf, write_conf=True)
    return object_count, frame
