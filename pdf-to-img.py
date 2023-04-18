from pypdf import PdfReader
from PIL import Image

reader = PdfReader('pgb11a.pdf')
page1 = reader.pages[2]
for i in page1.images:
  with open(i.name, 'wb') as f:
    f.write(i.data)

print("finish")
