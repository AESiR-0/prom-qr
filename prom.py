# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode


# String which represents the QR code
s = "https://linktr.ee/promcomesagain"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.png('Prom.png', scale = 5)
