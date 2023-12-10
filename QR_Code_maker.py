import pyqrcode

# Get Text From User
QR = input("Enter your text for making QR Code: ")
scale = input("\nEnter the scale you would like it to be (Just number): ")

# Create A QR Code
Create = pyqrcode.create(QR)
Create.svg("QR.svg", scale=scale)

print("\nDone")
input()
