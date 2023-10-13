from pynput.mouse import Button, Controller, Listener
from screeninfo import get_monitors
from collections import Counter

mouse = Controller()
button = Button.left
prev_screen_id = 0


def most_frequent(lis_t):
    count = Counter(lis_t)
    return count.most_common(1)[0][0]


def on_move(x, y):
    global prev_screen_id
    monitors = get_monitors()

    midis = []

    for monitor in monitors:
        if (-1 * monitor.y) <= y < monitor.height + (-1 * monitor.y):
            midis.append(monitors.index(monitor))

        if monitor.x <= x < monitor.width + monitor.x:
            midis.append(monitors.index(monitor))

    screen_id = most_frequent(midis)

    if screen_id != prev_screen_id:
        prev_screen_id = screen_id
        mouse.click(button, 1)


if __name__ == '__main__':
    try:
        print("Auto Screen Focus have been enabled, Please make sure you allow your script or your IDE to monitor your "
              "inputs from you system settings.")
        with Listener(on_move=on_move) as listener:
            listener.join()


    except:
        print("Auto Screen focus have been stopped.")
