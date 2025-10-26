import qrcode
upi_id = input("Enter the UPI ID = ")
phonepe = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
Google_pay = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
phonepe_qr = qrcode.make(phonepe)
paytm_qr = qrcode.make(paytm)
Google_pay_qr = qrcode.make(Google_pay)
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
Google_pay_qr.save("Google_pay_qr.png")
phonepe_qr.show()
paytm_qr.show()
Google_pay_qr.show()