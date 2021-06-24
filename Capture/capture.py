import win32gui
import win32ui
from ctypes import windll
from PIL import Image
import pyvda
import time
import pyocr, pyocr.builders

# OCR initialize
ocr = pyocr.get_available_tools()[0]
print(ocr)
builder = pyocr.builders.TextBuilder()

# show list of all window
def EnumWindowsProc(hWnd, lParam):
    if win32gui.IsWindow(hWnd):
        winname = win32gui.GetWindowText(hWnd)
        if winname == '':
            pass
        else:
            print(hWnd, winname.strip())
win32gui.EnumWindows(EnumWindowsProc, 0)

# input target window
hwnd = int(input())

target = pyvda.AppView(hwnd=hwnd)
# while False:
for i in range(1):
    # target Window is on current desktop?
    current_vda = pyvda.VirtualDesktop.current()
    if target.is_on_current_desktop():
        pass
    else:
        target.move(current_vda)

    # screen capture
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bottom - top

    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    saveDC.SelectObject(saveBitMap)

    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)

    image = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    # Get Text with OCR
    result = ocr.image_to_string(image, lang='jpn', builder=builder)
    print(result)

    # Read Text

    time.sleep(0.5)

