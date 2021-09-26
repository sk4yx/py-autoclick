import time
import threading
import configparser
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

config = configparser.ConfigParser()
config.read(".config.ini")

left_key_1 = config['Configs']['right_key']
left_put_1 = config['Configs']['right_put']

delay = 0.8/int(left_put_1)
button = Button.right
start_stop_key = KeyCode(char=left_key_1)


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def exit():
    click_thread.exit()
    listener.stop()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == KeyCode(char='h'):
        exit()

def main():
    with Listener(on_press=on_press) as listener:
        listener.join()

main()
