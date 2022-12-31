import time
import oled
import timer


def main():
    oled_display = oled.setup()
    oled.show_task(oled_display, "testing testing")
    timer.task_countdown()
    time.sleep(30)


main()
