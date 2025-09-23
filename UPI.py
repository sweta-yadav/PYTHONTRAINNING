import qrcode
upi_id="6301227972-2@axl"
name="sujata"
amount="1"
note="payment for coffee"
upi_link=f"upi://pay?pa={upi_id}&pn={name}&am={amount}&tn={note}"
qr=qrcode.make(upi_link)
qr.save("sujata.png")
print("QR code generated and saved as upi_payment_qr.png")