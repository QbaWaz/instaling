#TU NIE ZAGLĄDAMY, TO WCZORAJSZE PRÓBY TEGO BEZ SELENA
import pandas as pd #czyta csv
import pyautogui as gui #robi wiekszosc roboty
import pytesseract as ocr #znajduje pytanie
from PIL import ImageGrab as scr #screnshotuje pytanie
#otwiera plik
daneSlownik = pd.read_csv("dane.txt",header=None)
#czarodziejskim sposobem robi słownik
slownik = dict(zip (daneSlownik[0].values,daneSlownik[1].values) )


# screnshota robisz
#plik = scr.grab(bbox=(kordynatyw pikselach)

#tekst = ocr.image_to_string(plik)
#teraz ten tekst zafitować do słownika i wysłać odpowiedź, ewentualnie dodać
#do słownika
'''
plik = scr.grab(bbox=(640,450,930,490))
tekstZpliku = ocr.image_to_string(plik)
print(tekstZpliku)
'''
#DODAĆ TESERAKTA DO PATHA
# ok
