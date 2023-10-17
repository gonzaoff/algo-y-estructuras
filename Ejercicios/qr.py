import qrcode

data = "https://drive.google.com/drive/folders/1chzkgGUwhxcbVdGnWH_WK1KYBdcfTEIB"

img = qrcode.make(data)

img.save("C:/Users/Gonza/Pictures/myqrcode.png")
