# project 14 is a qr code generator app that geneartes qr codes from given url 
# the app will use qrcode module to generate qr codes
# the user can input the url and the app will save the qr code as an image file

# import qrcode

# URL=input("Enter the URL to generate QR code: ")
# filename=input("Enter the filename to save the QR code image (without extension): ")

# if not (filename.endswith('.png')):
#     filename += '.png'

# img=qrcode.make(URL)
# img.save(filename)
# print(f"QR code generated and saved as {filename}")
import qrcode

url = input("Enter the URL to generate QR code: ").strip()
filename = input("Enter the filename to save the QR code image (without extension): ").strip()

if not url:
    print("Error: URL cannot be empty")
    exit()

if not filename:
    print("Error: Filename cannot be empty")
    exit()

filename += ".png"

img = qrcode.make(url)
img.save(filename)

print(f"QR code generated and saved as {filename}")
