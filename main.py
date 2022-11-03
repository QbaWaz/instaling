import pandas as pd
import time
from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from random import choice

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
 
# times = [0.9856,1.27,3.12,3.45,4.764,7.03948]

# profile_path = r'C:\Users\bogda\AppData\Roaming\Mozilla\Firefox\Profiles\4mscljzm.default-release'
# options=Options()
# options.set_preference('profile', profile_path)
# options.set_preference("dom.webdriver.enabled", False)
# options.set_preference('useAutomationExtension', False)
# options.add_argument('--disable-blink-features=AutomationControlled')
# service = Service('C:\Drivers\geckodriver-v0.32.0-win64\geckodriver.exe')
# driver = Firefox(service=service, options=options)
# driver.get("https://bot.incolumitas.com/")
# # rchoice = choice(times)
# # print(rchoice)
# # sleep(rchoice)
# # driver.get("https://www.youtube.com")
# # rchoice = choice(times)
# # print(rchoice)
# # sleep(rchoice)
# driver.quit()

















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