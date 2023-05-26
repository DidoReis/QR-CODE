import qrcode

data = 'Don\'t forget to subscribe'

img = qrcode.make(data)

img.save("put the path where the Qrcode will be saved")




"""Change Color and size"""


''' import qrcode

data = 'Don\'t forget to subscribe'

qr = qrcode.QRCode(version = 1, box_size =10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'red', black_color = 'white')

img.save('put the path where the Qrcode will be saved') '''
