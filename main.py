import pandas as pd
import time
from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#setup
driver = wb.Firefox()
daneSlownik = pd.read_csv("dane.txt",header=None)   #otwiera plik
slownik = dict(zip (daneSlownik[0].values,daneSlownik[1].values) )  #czarodziejskim sposobem robi słownik z pliku


def pobierzPytanie():   #czarodziej pobiera pytanie ze strony
    pytanie = 0
    
    return pytanie

def podajOdpowiedz(odpowiedz):  #czarodziej wklepuje odpowiedź na stronkę
    global daneSlownik

    return 0

def dodajOdpowiedzDoSlownika(pytanie,odpowiedz):  #czarodziej dodaje pytanie i odpowiedź do słownika
    global daneSlownik
    

def main(): #trzeba też jakoś zakończyć pętle
    global daneSlownik
    
    while True: #jakoś wyłapać że to ekran końcowy
        pytanie = pobierzPytanie()
        if pytanie in daneSlownik:
            odpowiedz = daneSlownik[pytanie]
            podajOdpowiedz(odpowiedz)
        else:
            dodajOdpowiedzDoSlownika(pytanie,odpowiedz)
 

















#DEBIL AREA - NAUKA CYFEREK Z MATZOO
def matZoo():
    slownikmatz = {"zero":"0","jeden":"1","dwa":"2","trzy":"3","cztery":"4","pięć":"5","sześć":"6","siedem":"7","osiem":"8","dziewięć":"9"}

    driver.get("https://matzoo.pl/zerowka/50")
    time.sleep(8) #MASZ OSIEM SEKUND NA ZAAKCEPTOWANIE CIASTEK

    def odpowiedzNaPytanie():
        pytanie = driver.find_element(By.ID,"zadanie").text #czarodziejskie narzędzie znajduje elemet po ID, wyciąga z niego tekst

        odpowiedzi = { #czarodziejskie narzędzie robi słownik {treść przycisku: obiekt przycisku}
            (driver.find_element(By.ID,"0").text):(driver.find_element(By.ID,"0")),
            driver.find_element(By.ID,"1").text:driver.find_element(By.ID,"1"),
            driver.find_element(By.ID,"2").text:driver.find_element(By.ID,"2"),}

        if pytanie in slownikmatz.keys(): #czarodziejskie narzędzie znajduje przycisk z właściwą odpowiedzią i ją wciska
            odpowiedz = (odpowiedzi[slownikmatz[pytanie]])
        odpowiedz.click()

    for i in range(80):
        odpowiedzNaPytanie()
#KONIEC DEBIL AREI
input()