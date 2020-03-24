#https://www.thepythoncode.com/article/generate-read-qr-code-python

import qrcode

number_of_rooms = 140

for room in range(number_of_rooms):

    data = room #should be a url in the future
    # output file name
    filename = (str(room) + "_number.png")
    # generate QR code
    img = qrcode.make(data)
    # save image to a file
    img.save(filename)
