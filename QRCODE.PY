import qrcode
text = "Hello students are u ok with studies"
a=qrcode.QRCode()
a.add_data(text)
a.make(fit=True)
res=a.make_image(fill_color="black",back_color="white")
res.save("cse.png")
print("the QR code is executed successfully")