#coding: utf-8
#utilizar o ultimo resultado como fechamento

import random
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

group = []
opcao = []
contador = 0
listaUm = list(range(1,26))
resultado = []
lotofacil = []
	
url = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotofacil/'

def fetchHtmlForThePage(url, delay, block_name):
	options = webdriver.Chrome('/path/to/chromedriver')
	options.add_argument('headless')
	browser = webdriver.Chrome(chrome_options=options)
	browser.get(url)
	try:
		element_present = EC.presence_of_element_located((By.ID, block_name))
		WebDriverWait(browser, delay).until(element_present)
	except TimeoutException:
		print("Loading took too much time!")
	
	html = browser.page_source
	browser.quit()
	return html

if os.path.exists("lotofacil.txt"):
  os.remove("lotofacil.txt")
  print("Arquivo removido!")
else:
  print("Arquivo inexistente!")

print("\n#################### Buscar dados na WEB ##################\n")
html = fetchHtmlForThePage(url, 5, 're-Searchresult')

soup = BeautifulSoup(html,'html.parser')
divs = soup.findAll("table", {"class": "simple-table lotofacil"})
for div in divs:
	row = ''
	roww = ''
	rows = div.findAll('tr')
	for row in rows:
		row = div.findAll('td')
		for roww in row:
			resultado.append(int(roww.text))
		break

#random.shuffle(resultado)

group.append(resultado[0:10])
group.append(resultado[1:11])
group.append(resultado[2:12])
group.append(resultado[3:13])
group.append(resultado[4:14])
group.append(resultado[5:15])

group.append(resultado[0:3]+resultado[6:9]+resultado[12:15])
group.append(resultado[0:2]+resultado[4:6]+resultado[8:10]+resultado[11:13]+resultado[14:15])
group.append(resultado[0:1]+resultado[2:3]+resultado[3:4]+resultado[5:6]+resultado[7:8]+resultado[9:10]+resultado[10:11]+resultado[11:12]+resultado[12:13])
group.append(resultado[2:7]+resultado[9:13])
group.append(resultado[0:4]+resultado[10:15])

group.append(resultado[0:2]+resultado[4:6]+resultado[8:10]+resultado[12:14])
group.append(resultado[3:5]+resultado[7:9]+resultado[11:13]+resultado[13:15])
group.append(resultado[0:4]+resultado[11:15])
group.append(resultado[5:13])


listaDois = listaUm.copy()
for x in resultado:
	listaDois.remove(x)
	
random.shuffle(listaDois)

opcao.append(listaDois[0:5])
opcao.append(listaDois[0:5])
opcao.append(listaDois[0:5])
opcao.append(listaDois[0:5])
opcao.append(listaDois[0:5])
opcao.append(listaDois[0:5])

opcao.append(listaDois[4:10])
opcao.append(listaDois[4:10])
opcao.append(listaDois[4:10])
opcao.append(listaDois[4:10])
opcao.append(listaDois[4:10])

opcao.append(listaDois[2:9])
opcao.append(listaDois[2:9])
opcao.append(listaDois[2:9])
opcao.append(listaDois[2:9])

# print(*group, sep = "\n") 
# print("Aleatorios \n")
# print(*opcao, sep = "\n") 

#input()

for w in range(15):
	for item in range(1):
		contador = contador+1
		documento = "lotofacil.txt"
		arq = open(documento, "a")
		final = []
		abc = group[w].copy()
		for z in opcao[w]:
			abc.append(z)
		lotofacil = sorted(abc)
		for e in lotofacil:
			final.append('%0.2d' % e)
		print("\nCriando Jogo "+str(contador)+"\n")
		res = "\n".join(["".join(str(final[i:i+15])) for i in range(0,len(str(final)),15)])
		arq.write(res[0:90]+"\n")
		arq.close()
print("\n#################### Processo Finalizado ##############################\n")

