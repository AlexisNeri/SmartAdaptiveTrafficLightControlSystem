from gpiozero import LED
from time import sleep

# Initialize GPIO ports to use for traffic light control
red_1 = LED(22)
yellow_1 = LED(27)
green_1 = LED(17)
red_2 = LED(14)
yellow_2 = LED(15)
green_2 = LED(18)


def decision_maker(street_1_counter, street_2_counter, time_last_change, main_road):
    if main_road == 1:
        # If counter for street on red phase is greater than counter for street on green phase or waiting time exceed
        # 3 minutes, interchange states
        if street_2_counter > street_1_counter or time_last_change >= 180:
            print('Street #1: Yellow')
            red_1.off()
            yellow_1.on()
            green_1.off()
            print('Street #2: Red')
            red_2.on()
            yellow_2.off()
            green_2.off()
            sleep(3)
            print('Street #1: Red')
            red_1.on()
            yellow_1.off()
            green_1.off()
            print('Street #2: Green')
            red_2.off()
            yellow_2.off()
            green_2.on()
            main_road = 2
            time_last_change = 0
    else:
        if street_1_counter > street_2_counter or time_last_change >= 180:
            print('Street #2: Yellow')
            red_2.off()
            yellow_2.on()
            green_2.off()
            print('Street #1: Red')
            red_1.on()
            yellow_1.off()
            green_1.off()
            sleep(3)
            print('Street #2: Red')
            red_2.on()
            yellow_2.off()
            green_2.off()
            print('Street #1: Green')
            red_1.off()
            yellow_1.off()
            green_1.on()
            main_road = 1
            time_last_change = 0

    return main_road, time_last_change
