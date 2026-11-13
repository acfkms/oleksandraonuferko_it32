import qrcode
text = "Олександра Онуферко, ІТ-32 AAAAAAAA@gmail.com"
image = qrcode.make(text)
image.save("contact.png")
print("saved: contact.png")