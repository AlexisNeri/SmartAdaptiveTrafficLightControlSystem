from gpiozero import LED
from time import sleep

# Initialize GPIO ports to use for traffic light control
TRAFFIC_LIGHT_1 = {'red': LED(18), 'yellow': LED(15), 'green': LED(14)}
TRAFFIC_LIGHT_2 = {'red': LED(4), 'yellow': LED(3), 'green': LED(2)}


def stop_traffic_flow(traffic_light):
    traffic_light['red'].off()
    traffic_light['yellow'].on()
    traffic_light['green'].off()
    sleep(3)
    traffic_light['red'].on()
    traffic_light['yellow'].off()


def start_traffic_flow(traffic_light):
    traffic_light['red'].off()
    traffic_light['yellow'].off()
    traffic_light['green'].on()


def decision_maker(street_1_counter, street_2_counter, time_last_change, current_main_road):
    if current_main_road == 1:
        if street_2_counter > street_1_counter or time_last_change >= 42:
            stop_traffic_flow(TRAFFIC_LIGHT_1)
            start_traffic_flow(TRAFFIC_LIGHT_2)
            current_main_road = 2
            time_last_change = 0
    else:
        if street_1_counter > street_2_counter or time_last_change >= 26:
            stop_traffic_flow(TRAFFIC_LIGHT_2)
            start_traffic_flow(TRAFFIC_LIGHT_1)
            current_main_road = 1
            time_last_change = 0

    return current_main_road, time_last_change
