import pyautogui
import time
import keyboard
import win32api
import win32con


print('starting game . . .')


def click(x, y):
    win32api.SetCursorPos((x, y))
    # press down
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    # release
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q') == False:
    flag = 0
    pic = pyautogui.screenshot(region=(30, 102, 724, 726))
    width, height = pic.size
    # target rgb value = (255,0,0)
    for x in range(0, width, 5):
        for y in range(0, height, 5):
            r, g, b = pic.getpixel((x, y))
            if r == 255 and g == 0:
                flag = 1
                click(x+30, y+102)
                # break so we won't click the same place again
                break
        if flag:
            break


# pyautogui.displayMousePosition()
# # (30,102)
# # (724,726)
# iml = pyautogui.screenshot(region=(30, 102, 724, 726))
# iml.save(r"C:\Users\Panagiotis\Documents\Job\python\aimtrainer\s.png")
