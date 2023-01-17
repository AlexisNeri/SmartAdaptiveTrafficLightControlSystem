import imutils
from cvlib.object_detection import YOLO

yolo = YOLO('dataset/custom_yolo_weights/yolov7-tiny-custom_final.weights',
            'dataset/custom_yolo_weights/yolov7-tiny-custom.cfg',
            'dataset/custom_yolo_weights/obj.names', version='yolov7-tiny')


def car_counter(frame, target_labels, debug_log=False):
    object_count = 0
    if (frame.shape[1] % 2 == 0) and (frame.shape[0] % 2 == 0):
        image_width = int(frame.shape[1]/2)
        image_height = int(frame.shape[0]/2)
        frame = imutils.resize(frame, width=image_width, height=image_height)
    bbox, label, conf = yolo.detect_objects(frame)
    if debug_log:
        print(bbox, label, conf)
    for current_label in target_labels:
        object_count += label.count(current_label)
    yolo.draw_bbox(frame, bbox, label, conf, write_conf=True)
    return object_count, frame
