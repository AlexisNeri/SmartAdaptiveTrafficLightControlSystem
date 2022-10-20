import car_counter
import decision_maker
import cv2


def main_module(main_street_vsource, secondary_street_vsource, show_output=False, show_logs=False,
                show_count=False):
    main_vsource = cv2.VideoCapture(main_street_vsource)
    secondary_vsource = cv2.VideoCapture(secondary_street_vsource)

    if not main_vsource.isOpened() or not secondary_vsource.isOpened():
        print("Error: could not open video sources")
        exit()

    while main_vsource.isOpened() and secondary_vsource.isOpened():
        main_status, main_frame = main_vsource.read()
        secondary_status, secondary_frame = secondary_vsource.read()
        if not main_status or not secondary_status:
            break

        street_1_count, street_1_bbox = car_counter.car_counter(main_frame, ['car', 'truck', 'motorcycle'],
                                                                debug_log=show_logs)
        street_2_count, street_2_bbox = car_counter.car_counter(secondary_frame, ['car', 'truck', 'motorcycle'],
                                                                debug_log=show_logs)
        # TODO: Integrate decision maker module.
        if show_count:
            print('Vehicles at street #1: {0}\n Vehicles at street #2: {1}'.format(street_1_count, street_2_count))
        if show_output:
            cv2.imshow("Street #1", street_1_bbox)
            cv2.imshow("Street #2", street_2_bbox)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    main_vsource.release()
    secondary_vsource.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main_module('Video/DJI_0054.MP4', 'Video/DJI_0055.MP4', show_output=True, show_count=True)
