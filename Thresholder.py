import cv2

class Thresholder:

    def __init__(self, thresh_one = 30, thresh_two = 140):
        self.thresh_one = thresh_one
        self.thresh_two = thresh_two

    def __call__(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #T_, image = cv2.threshold(image, self.thresh_one, self.thresh_two, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        T_, image = cv2.threshold(image, self.thresh_one, self.thresh_two, cv2.THRESH_TOZERO)

        return image