import sys
from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime

def main(argv,argc):
    page = requests.get("https://www.bcv.org.ve/")
    soup = BeautifulSoup(page.text, "html.parser")
    search = soup.find("div",attrs={"id":"dolar"})
    dolar = float(re.findall('[\\d+]+,[1-9+]+',str(search))[0].replace(",","."))
    if argc == 1:
        print(f"Fecha: {datetime.today().strftime('%Y-%m-%d')}\n1.$ = {dolar}.Bs")
        return
    if argc != 3:
        return
    argv[2] = float(argv[2])
    if argv [1] == "-cB":
        print(f"{(argv[2]/dolar):.4f}.$")
    if argv [1] == "-c$":
        print(f"{(argv[2]*dolar):.4f}.Bs")


main(sys.argv,len(sys.argv))
