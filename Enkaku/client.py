from PIL import Image, ImageGrab
import time
import serial
import win32api, win32con

# クライアントのウィンドウサイズ
wX = 640
wY = 480

# シリアル関連の変数
ser = None
serSpeed = 115200

# 比較用変数
oldBuf = 0
newBuf = 1

#########################################################
#
#   シリアル初期化
#
#########################################################
for i in range(20):
    serNo = 'COM' + str(i)
    try:
        ser = serial.Serial(serNo, serSpeed, timeout=0.2)
        line = ser.readline().strip().decode('utf-8')
    except:
        pass

    if ser is not None:
        if line == '__RMKBD__':
            ser.write(b'__DETECT__')
            break
        ser.close()

print('serNo : ', serNo)

#########################################################
#
#   シリアル関連の関数
#
#########################################################
def recvSer():
    data = ser.readline().strip().decode('utf-8')
    if data == '':
        pass
    else:
        print('data : ', data)

def sendSer(line):
    line = line +'|'
    ser.write(line.encode())

#########################################################
#
#   描画関連の関数
#
#########################################################

# 書き込みバッファの番号を交換
def changeBuf():
    global oldBuf, newBuf
    if oldBuf == 0:
        oldBuf = 1
        newBuf = 0
    else:
        oldBuf = 0
        newBuf = 1

# (x, y)のRGBを送信
def sendPixel(x, y, col):
    s = 'PXL,' + str(x) + ',' + str(y) + ',' + str(col[0]) + ',' + str(col[1]) + ',' + str(col[2])
    sendSer(s)

##########################################################
#
#   メイン部
#
##########################################################

# デスクトップサイズの取得
# wX = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
# wY = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

# RPiがソケット通信できるまで待機
print('RPi connecting...')
while True:
    data = ser.readline().strip().decode('utf-8')
    if data == 'CON':
        print('[OK] RPi connected')
        break

# 初期データを送信
data = 'WSZ' + ',' + str(wX) + ',' + str(wY)
sendSer(data)
imgBuf = [ImageGrab.grab(bbox=(0, 0, wX, wY)), ImageGrab.grab(bbox=(0, 0, wX, wY))]
for y in range(wY):
    for x in range(wX):
        col = imgBuf[oldBuf].getpixel((x, y))
        sendPixel(x, y, col)
print('[OK] send initialize data')
sendSer('END')

# キャプチャの比較
while True:
    print('kdjfalsj')
    imgBuf[newBuf] = ImageGrab.grab(bbox=(0, 0, wX, wY))
    for y in range(wY):
        for x in range(wX):
            oldColor = imgBuf[oldBuf].getpixel((x, y))
            newColor = imgBuf[newBuf].getpixel((x, y))
            if oldColor != newColor:
                sendPixel(x, y, newColor)
    sendSer('END')
    changeBuf()
    time.sleep(0.5)

