import qrcode

data = "Ingresa un texto o una URL."

img = qrcode.make(data)

img.save("C:/Users/Gonza/Pictures/myqrcode.png")
