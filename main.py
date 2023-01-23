import car_counter
import decision_maker
import cv2
import math
import time
import datetime
import xlsxwriter


def main_module(main_street_vsource, secondary_street_vsource, show_output=False, show_inf_logs=False):
    timer = 0
    counter = 0
    main_road = 0
    current_row = 0
    column = 0
    filename = str(datetime.datetime.now()).replace(':', '-')
    workbook = xlsxwriter.Workbook('{}.xlsx'.format(filename))
    worksheet = workbook.add_worksheet(name='Results')
    worksheet.write_row(current_row, column, ('street_1_count', 'street_2_count', 'inference_time', 'main_road',
                                              'time_last_change'))

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
            begin = time.time()
            street_1_count, street_1_bbox = car_counter.car_counter(main_frame, ['vehicle_entering_intersection'],
                                                                    debug_log=show_inf_logs)
            street_2_count, street_2_bbox = car_counter.car_counter(secondary_frame, ['vehicle_entering_intersection'],
                                                                    debug_log=show_inf_logs)
            end = time.time()
            main_road, timer = decision_maker.decision_maker(street_1_count, street_2_count, timer, main_road)

            inference_time = end - begin
            current_row += 1
            worksheet.write_row(current_row, column, (street_1_count, street_2_count, inference_time, main_road, timer))

            if show_output:
                cv2.imshow('Street #1', street_1_bbox)
                cv2.imshow('Street #2', street_2_bbox)

        counter += 1
        if counter == main_vsource_fps:
            counter = 0
            timer += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    main_vsource.release()
    secondary_vsource.release()
    cv2.destroyAllWindows()
    workbook.close()


# TODO: Change video routes from hardcoded to dynamic
if __name__ == '__main__':
    main_module('Video/DJI_0075CM.MP4', 'Video/DJI_0076CS.MP4', show_output=True)
