import pyautogui
import time
import keyboard
import win32api
import win32con

time.sleep(2)


def click(x, y):
    win32api.SetCursorPos((x, y))
    # press down
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    # release
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q') == False:
    flag = 0
    pic = pyautogui.screenshot(region=(91, 345, 620, 430))
    width, height = pic.size
    # target rgb value = (215,219,195)
    for x in range(0, width, 5):
        for y in range(0, height, 5):
            r, g, b = pic.getpixel((x, y))
            if b == 195 and r == 255 and g == 219:
                flag = 1
                click(x+91, y+345)
                time.sleep(0.05)
                # break so we won't click the same place again
                break
        if flag == 1:
            break


# pyautogui.displayMousePosition()
# (91, 345)
# (620, 450)
# iml = pyautogui.screenshot(region=(91, 345, 620, 430))
# iml.save(r"C:\Users\Panagiotis\Documents\Job\python\aimbooster\aim.png")
