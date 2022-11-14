import imutils
import cvlib as cv
from cvlib.object_detection import draw_bbox


def car_counter(frame, target_labels, debug_log=False):
    object_count = 0
    if (frame.shape[1] % 2 == 0) and (frame.shape[0] % 2 == 0):
        image_width = int(frame.shape[1]/2)
        image_height = int(frame.shape[0]/2)
        frame = imutils.resize(frame, width=image_width, height=image_height)
    bbox, label, conf = cv.detect_common_objects(frame, confidence=0.25, model='yolov4-tiny')
    if debug_log:
        print(bbox, label, conf)
    for current_label in target_labels:
        object_count += label.count(current_label)
    output_image = draw_bbox(frame, bbox, label, conf, write_conf=True)
    return object_count, output_image
