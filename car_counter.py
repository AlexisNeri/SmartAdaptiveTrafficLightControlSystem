import imutils
import cvlib as cv
from cvlib.object_detection import draw_bbox


def car_counter(frame, target_labels, debug_log=False):
    object_count = 0
    # TODO: Make frame resizing dynamic to 1/2 of input
    frame = imutils.resize(frame, width=960, height=540)
    bbox, label, conf = cv.detect_common_objects(frame)
    if debug_log:
        print(bbox, label, conf)
    for current_label in target_labels:
        object_count += label.count(current_label)
    output_image = draw_bbox(frame, bbox, label, conf, write_conf=True)
    return object_count, output_image
