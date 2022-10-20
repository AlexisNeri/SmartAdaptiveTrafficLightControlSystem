from time import sleep


def decision_maker(street_1_counter, street_2_counter, time_last_change, main_road):
    if main_road == 1:
        if street_1_counter < street_2_counter + time_last_change:
            print('Street #1: Yellow')
            print('Street #2: Red')
            sleep(3)
            print('Street #1: Red')
            print('Street #2: Green')
            main_road = 2
            time_last_change = 0
    else:
        if street_2_counter < street_1_counter + time_last_change:
            print('Street #2: Yellow')
            print('Street #1: Red')
            sleep(3)
            print('Street #2: Red')
            print('Street #1: Green')
            main_road = 1
            time_last_change = 0

    return main_road, time_last_change
