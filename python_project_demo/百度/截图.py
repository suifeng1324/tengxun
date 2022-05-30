"""
@Author :       yangleiw
@File   :       .py
@Time   :       2022年05月22日 09:32
@Desc   :
"""

import time

import keyboard
from PIL import ImageGrab  # pip install pillow


def screenShot():
    if keyboard.wait(hotkey="alt+a") == None:
        time.sleep(1)
        print("dddd")
        image = ImageGrab.grabclipboard()
        image.save('example.jgp')

# if __name__ == "__main__":
#     pass
