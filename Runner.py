import cv2
from Cutter import Cutter
from Obraz import Obraz
from Denoiser import Denoiser
from Thresholder import Thresholder
from ContourFinder import ContourFinder

def przerob(obraz):
    #Uzywam Denoisera
    obraz.denoised = den(obraz.image)
    #Używam ContourFindera
    obraz.edged = confin(obraz.denoised)
    confin.conmax(obraz.image, obraz.edged)
    # Cutter wycina obraz i o ustawia
    obraz.image = cutter(obraz.image, confin)

def pokaz(Obraz):
    cv2.imshow("Pokazuje", Obraz.image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def run(i):
    for i in range(i):
        try:
            #Wczytuję obraz i skaluję go
            obraz = Obraz("zasob/fiszka ({}).jpg".format(i+1))
            obraz.resize(25)
            obraz.obrot()
            przerob(obraz)
            cv2.imwrite("przerobione/fiszka ({}).jpg".format(i+1), obraz.image)
        except:
            print("Nie udało mi się wykonać zadania dla obrazu nr: {}".format(i+1))
            pass

den = Denoiser()
confin = ContourFinder()
cutter = Cutter()
thresh = Thresholder()

run(8)