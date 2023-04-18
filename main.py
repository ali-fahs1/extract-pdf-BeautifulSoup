import pdfplumber

doc = pdfplumber.open('pgb11a.pdf')

page = doc[2]
pic = page.pixmap()
pic.save("alli.png")