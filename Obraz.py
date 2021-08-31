import cv2
from PIL import Image

class Obraz:

    def __init__(self, img_path):
        self.image = cv2.imread(img_path)
        self.edged = None
        self.denoised = None

    def pokaz(self):
        cv2.imshow("XXX", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def resize(self, procent):
        height = int(self.image.shape[0]/100*procent)
        width = int(self.image.shape[1]/100*procent)
        dim = (width, height)
        self.image = cv2.resize(self.image, dim, interpolation=cv2.INTER_LANCZOS4)

    def obrot(self):

        if (self.image.shape[0]>self.image.shape[1]):
            self.image = cv2.rotate(self.image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        else:
            None

