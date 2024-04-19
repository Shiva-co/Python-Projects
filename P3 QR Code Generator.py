# Project 3 : QR Code Generator

# Type 1 - Simple

# import qrcode as qr
# img = qr.make("https://www.youtube.com")
# img.save("Youtube.png")

# Type 2 - Customize

import qrcode as qrc
from PIL import Image

qr = qrc.QRCode(version=1,error_correction=qrc.constants.ERROR_CORRECT_H,
                box_size=20,border=5)
qr.add_data("https://www.youtube.com/")
qr.make(fit=True)
img= qr.make_image(fill_color="red",back_color="beige")
img.save("Youtube.png")

