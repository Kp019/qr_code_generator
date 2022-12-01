import qrcode
import csv
name = open("name.csv", 'r')
ds = open("link.csv", 'r')
for each in ds:
    print(each)
    img = qrcode.make(each)
    img.save("./qr code/name.png")
