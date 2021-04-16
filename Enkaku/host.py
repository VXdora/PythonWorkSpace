import socket
from PIL import Image, ImageTk
import tkinter as tk
import pyautogui
import win32gui
import socket
import threading

# 変数
host = '192.168.10.9'
port = 8080
bufSize = 256

# ウィンドウ位置
wX = 0
wY = 0

# ウィンドウサイズ
wWidth  = 960
wHeight = 720

# 表示するイメージの情報
image = None
imageX = 0
imageY = 0
imageWidth = 0
imageHeight = 0

# イメージ上のマウス
mouseX = 0
mouseY = 0

qFlag = True

###########################################################
#
#   メインウィンドウの初期化
#
###########################################################
root = tk.Tk()
root.geometry(str(wWidth) + 'x' + str(wHeight))
canvas = tk.Canvas(root, width=wWidth, height=wHeight)
canvas.pack()

###########################################################
#
#   ネットワーク初期化
#
###########################################################
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
print('SOCKET CONNECTED')

###########################################################
#
#   イベント
#
###########################################################
def mouseMotion(event):
    # 変数（ウィンドウ相対座標）
    global mouseX, mouseY
    global imageX, imageY

    mouseX = event.x
    mouseY = event.y
    dX = 0
    dY = 0
    changeImageFlag = False

    if mouseX < 40:
        o_imageX = imageX
        imageX = imageX -wWidth +2*45
        if imageX < 0:
            imageX = 0
        dX = o_imageX -imageX
    elif mouseX > wWidth -40:
        o_imageX = imageX
        imageX = imageX +wWidth -2 *45
        if imageX +wWidth > imageWidth:
            imageX = imageWidth -wWidth
        dX = o_imageX -imageX

    if mouseY < 40:
        o_imageY = imageY
        imageY = imageY -wHeight +2*45
        if imageY < 0:
            imageY = 0
        dY = o_imageY -imageY
    elif mouseY > wHeight -40:
        o_imageY = imageY
        imageY = imageY +wHeight -2*45
        if imageY +wHeight > imageHeight:
            imageY = imageHeight -wHeight
        dY = o_imageY -imageY

    sendText = 'MSE,' + str(imageX + mouseX) + ',' + str(imageY + mouseY) + '\n'
    send(sendText)

    if dX == 0 and dY == 0:
        pass
    else:
        pyautogui.moveTo(wX +mouseX +dX, wY +mouseY +dY)
        drawImage()

def keyboardMotion(event):
    print('keyboard')

def windowMotion(event):
    global wX, wY
    global mouseX, mouseY
    rect = win32gui.GetWindowRect(win32gui.GetForegroundWindow())
    wX = rect[0] +8
    wY = rect[1] +31
    drawImage()

def closeMotion():
    global qFlag
    qFlag = False
    sock.close()
    root.destroy()

###########################################################
#
#   ソケット関連の関数
#
###########################################################
def recv():
    global qFlag
    while qFlag:
        data = sock.recv(256).decode('utf-8').strip()
        if data == '':
            pass
        else:
            buf = []
            
            print('data : ', data[0:3])

def send(line):
    sock.send(line.encode())

###########################################################
#
#   描画関係の関数
#
###########################################################
def setPixel(x, y, r, g, b):
    global image
    image.putpixel((x, y), (r, g, b))

def drawImage():
    global image, img
    if image:
        img = ImageTk.PhotoImage(image=image)
        canvas.create_image(-imageX, -imageY, anchor='nw', image=img)

###########################################################
#
#   プログラムメイン
#
###########################################################
# イメージの読み込み
image = Image.open('sample.jpg')
img = ImageTk.PhotoImage(image=image)
imageWidth = img.width()
imageHeight = img.height()
drawImage()
# ms_image = canvas.create_rectangle(0, 0, 10, 10, fill='black')


send('TEST')

# イベントのハンドル
root.bind('<Motion>', mouseMotion)      # マウス移動
root.bind('<Configure>', windowMotion)  # ウィンドウ移動
root.protocol('WM_DELETE_WINDOW', closeMotion)  # 終了処理

# 受信したメッセージの処理
thread = threading.Thread(target=recv)
thread.start()

root.mainloop()

