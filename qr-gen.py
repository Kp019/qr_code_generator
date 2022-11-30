import qrcode


img = qrcode.make("www.linkedin.com/in/tobsramp07")
img.save("toby.jpg")