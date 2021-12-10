import barcode
from barcode.writer import ImageWriter
import random

def png_code():
    for i in range(10):
        code = random.randint(111111111111,999999999999)
        ean = barcode.get('ean13', f'{str(code)}', writer=ImageWriter())
        filename = ean.save(f'ean13-{i}')
        filename


def svg_code():
    ean = barcode.get('ean13', '123456789012')
    ean.get_fullcode()
    options = dict(compress=True)
    filename = ean.save('ean13-svg', options)
    filename

svg_code()
