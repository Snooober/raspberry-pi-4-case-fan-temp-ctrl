import logging
import time
from gpiozero import PWMLED


HIGH_TEMP = 80
DELAY_SEC = 5
FAN = PWMLED(14)
CPU_TEMP_FILE = "/sys/class/thermal/thermal_zone0/temp"

is_high_temp = False
is_fan_on = None


def get_cpu_temp():
    with open(CPU_TEMP_FILE) as f:
        cpu_temp = f.read()
        cpu_temp = int(cpu_temp) / 1000
    return cpu_temp


def check_high_temp():
    global is_high_temp
    cpu_temp = get_cpu_temp()
    logging.debug("CPU Temp: " + str(cpu_temp))
    if cpu_temp >= HIGH_TEMP:
        is_high_temp = True
    elif is_high_temp:
        if cpu_temp <= (HIGH_TEMP - 5):
            is_high_temp = False


def toggle_fan(on):
    global is_fan_on
    if on is True:
        if is_fan_on is False or is_fan_on is None:
            FAN.value = 1
            is_fan_on = True
            logging.info("Case fan toggled ON.")
    else:
        if is_fan_on or is_fan_on is None:
            FAN.value = 0
            is_fan_on = False
            logging.info("Case fan toggled OFF.")


def main():
    logging.basicConfig(level=logging.INFO)
    try:
        while True:
            check_high_temp()
            if is_high_temp:
                toggle_fan(True)
            else:
                toggle_fan(False)
            time.sleep(DELAY_SEC)
    finally:
        FAN.value = 1
        logging.info("Exiting...case fan toggled ON.")


if __name__ == "__main__":
    main()
