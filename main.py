import car_counter
import decision_maker
import cv2
import math


def main_module(main_street_vsource, secondary_street_vsource, show_output=False, show_logs=False,
                show_count=False):
    time = 0
    counter = 0
    main_road = 0
    main_vsource = cv2.VideoCapture(main_street_vsource)
    main_vsource_fps = math.ceil(main_vsource.get(cv2.CAP_PROP_FPS))
    print('Frame rate for main video source is: {}'.format(main_vsource_fps))
    secondary_vsource = cv2.VideoCapture(secondary_street_vsource)
    secondary_vsource_fps = math.ceil(secondary_vsource.get(cv2.CAP_PROP_FPS))
    print('Frame rate for secondary video source is: {}'.format(secondary_vsource_fps))

    if main_vsource_fps != secondary_vsource_fps:
        print('Error: video sources have different frame rates')
        exit()

    if not main_vsource.isOpened() or not secondary_vsource.isOpened():
        print('Error: could not open video sources')
        exit()

    while main_vsource.isOpened() and secondary_vsource.isOpened():
        main_status, main_frame = main_vsource.read()
        secondary_status, secondary_frame = secondary_vsource.read()
        if not main_status or not secondary_status:
            break
        # Process 1 frame per second
        if counter == main_vsource_fps/2:
            street_1_count, street_1_bbox = car_counter.car_counter(main_frame,
                                                                    ['bicycle, motorcycle', 'car', 'truck', 'bus'],
                                                                    debug_log=show_logs)
            street_2_count, street_2_bbox = car_counter.car_counter(secondary_frame,
                                                                    ['bicycle, motorcycle', 'car', 'truck', 'bus'],
                                                                    debug_log=show_logs)
            main_road, time = decision_maker.decision_maker(street_1_count, street_2_count, time, main_road)
            if show_count:
                print('Vehicles at street #1: {0}\n Vehicles at street #2: {1}'.format(street_1_count, street_2_count))
            if show_output:
                cv2.imshow('Street #1', street_1_bbox)
                cv2.imshow('Street #2', street_2_bbox)

        counter += 1
        if counter == main_vsource_fps:
            counter = 0
            time += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    main_vsource.release()
    secondary_vsource.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # TODO: Change video routes from hardcoded to dynamic
    main_module('Video/DJI_0054.MP4', 'Video/DJI_0055.MP4', show_output=True, show_count=True)
