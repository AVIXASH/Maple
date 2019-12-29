from methods import *
import pyautogui
import os
import time
import random

# Reference images are to be loaded here
images = [os.path.join("images", "back.png"),               # 0
          os.path.join("images", "crystal.png"),            # 1
          os.path.join("images", "follow.png"),             # 2
          os.path.join("images", "follow2.png"),            # 3
          os.path.join("images", "follow_insta.png"),       # 4
          os.path.join("images", "following.png"),          # 5
          os.path.join("images", "put_likes.png"),          # 6
          os.path.join("images", "watch_vids.png"),         # 7
          os.path.join("images", "hiketop.png"),            # 8
          os.path.join("images", "one.png"),                # 9
          os.path.join("images", "follow_insta2.png"),      # 10
          os.path.join("images", "following2.png"),         # 11
          ]


def gain_crystals():        # Gain Crystals via. following
    os.startfile("""C:\ProgramData\BlueStacks\Client\Bluestacks.exe""")

    time.sleep(60)
    check(images[8])
    time.sleep(10)
    click(images[8])
    click(images[2])
    for _ in range(random.randrange(10, 17)):
        click(images[9])
        pyautogui.scroll(2)
        pyautogui.sleep(random.randrange(5, 9))
        for _ in range(2):
            click(images[3])
            click_compare(images[4], images[10])
            compare(images[5], images[11])
            click(images[0])
