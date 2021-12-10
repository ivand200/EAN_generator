import barcode
from barcode.writer import ImageWriter
import random


for i in range(10):
    code = random.randint(111111111111,999999999999)
    ean = barcode.get('ean13', f'{str(code)}', writer=ImageWriter())
    filename = ean.save(f'ean13-{i}')
    filename
