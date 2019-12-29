import pyautogui


def click(name):    # Performs a click after checking for loaded image
    location = None
    image_file = name

    while location is None:
        try:
            location = pyautogui.locateOnScreen(image_file, confidence=0.8)
        except Exception as e:
            print(e)

    coordinates = pyautogui.center(location)
    x, y = coordinates
    pyautogui.click(coordinates)


def click_compare(name, name2):     # Performs a click after comparing availability of two loaded images
    location = None
    image_file_1 = name
    image_file_2 = name2

    while location is None:
        try:
            location = pyautogui.locateOnScreen(image_file_1, confidence=0.8) or pyautogui.locateOnScreen(image_file_2, confidence=0.7)
        except Exception as e:
            print(e)

    coordinates = pyautogui.center(location)
    x, y = coordinates
    pyautogui.click(coordinates)


def check(name):        # Checks for the the presence of loaded image until found
    location = None
    image_file = name

    while location is None:
        try:
            location = pyautogui.locateOnScreen(image_file, confidence=0.8)
        except Exception as e:
            print(e)


def compare(name, name2):       # Performs a check after comparing two loaded images until found
    location = None
    image_file_1 = name
    image_file_2 = name2

    while location is None:
        try:
            location = pyautogui.locateOnScreen(image_file_1, confidence=0.8) or pyautogui.locateOnScreen(image_file_2, confidence=0.7)
        except Exception as e:
            print(e)
