import os
import qrcode


input1 = input("Enter The URL: ")

img=qrcode.make(input1)
img.save("qr_code.png","PNG")
