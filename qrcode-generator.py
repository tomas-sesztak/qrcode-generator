import qrcode
import string
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import GappedSquareModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask

class QRCODE:
  def __init__(self, qrcode_data = "CHANGEME", back_color = (255, 255, 255), front_color = (0, 0, 0)):
    self.back_color = back_color
    self.front_color = front_color
    self.qrcode_data = qrcode_data

    self.generateQRCode()
    self.addQRCodeData()
    self.fitQRCode()
    self.generateImage()
    self.saveImage()

  def generateQRCode(self):
    self.qr = qrcode.QRCode(error_correction = qrcode.constants.ERROR_CORRECT_L,
                            version = 1,
                            box_size = 20,
                            border = 1
                           )

  def addQRCodeData(self):
    self.qr.add_data(self.qrcode_data)

  def fitQRCode(self):
    self.qr.make(fit=True)

  def generateImage(self):
    self.img = self.qr.make_image(image_factory=StyledPilImage,
                                  module_drawer=GappedSquareModuleDrawer(),
                                  color_mask=SolidFillColorMask(front_color=self.front_color, back_color=self.back_color)
                                 )

  def saveImage(self):
    self.img.save("qrcode.png")

if __name__ == "__main__":
  qrcode = QRCODE(qrcode_data = 'https://docs.google.com/presentation/d/1-5goIWPnm11CHy0ZbSigM2ySsoJhvmEKLNf09hAb5eQ/edit#slide=id.p', front_color=(87, 67, 61), back_color=(255,255,255))

