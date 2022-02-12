import time
import qrcode
t = time.localtime()
filename = time.strftime("%H;%M", t)
s = input("введите текст или ссылку:")
img = qrcode.make(s)
type(img)
img.save(filename + ".png")