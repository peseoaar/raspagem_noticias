from bs4 import BeautifulSoup
import requests

## exemplo CNN
link1 = "https://www.cnnbrasil.com.br/"
header = {'User-agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0"}
requisicao = requests.get(link1, headers=header)

site = BeautifulSoup(requisicao.text, "html.parser")

noticiaTitulo1 = site.find("h2", class_="block__news__title")
noticiaSubtitulo1 = site.find("h3", class_="block__news__title")
print("1."+noticiaTitulo1.getText())
print()
print("",noticiaSubtitulo1.getText())
print()
print(".CNN BRasil")
print()
print("----------------------------------------------")
# exemplo BBC
link2 = "https://www.bbc.com/portuguese"
header = {"User-agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0"}
requisicao = requests.get(link2, headers=header)

site = BeautifulSoup(requisicao.text, "html.parser")

noticiaTitulo2 = site.find("h3", class_="bbc-14nw343 e47bds20")
noticiaSubtitulo2 = site.find("p", class_="promo-paragraph bbc-1xza832 ewjbyra0")
print("2."+noticiaTitulo2.getText())
print()
print("", noticiaSubtitulo2.getText())
print()
print(".BBC Brasil")