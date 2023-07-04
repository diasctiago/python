# -*- coding: utf-8 -*-

# importando bibliotecas
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import nltk
#from nltk.tokenize import sent_tokenize
#from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
#nltk.download('punkt')
#nltk.download('stopwords')

# declarando algumas variaveis
txt = []

print ('\n')
input ('Pressione ENTER para iniciar...')
#caminho = input('Informe o caminho onde o arquivo está salvo no formato .txt: ')
#arquivo = input('Informe o nome do arquivo para leitura sem exteção: ')
#discursos = caminho + '\\' + arquivo + '.txt'
discursos = 'C:\Python\congresso.txt'

# lista das stopwords a serem removidas
stop_words = set(stopwords.words("portuguese"))
# Adicionando stopwords a serem removidas informadas
stop_words.update(('-', '"','.',',','!', ':', '','de','acima','tudo','à','é','ú','Com','O','Que','Um','Uma','aqui','às','2005', '28', 'A','As','E','Os'))
# lista das stopwords em ingles a serem removidas do próprio método wordcloud
stop_words.update(set(STOPWORDS))
# Leitura do texto informado
texto = open(discursos,'r').read()

#palavras = nltk.word_tokenize(texto)
# loop para retirar as palavras a serem removidas dos discursos
#for x in stop_words:
#	while x in palavras:
#		palavras.remove(x)
# juntando as palavras dos discursos
#txt.extend(palavras)
# convertendo a lista de palavras em string	
#resultado = ', '.join(txt)

# plotando a nuvem de palavras
wordcloud = WordCloud(stopwords = stop_words, max_font_size=200 ,width = 1024, height = 728).generate(texto)
plt.figure(figsize=(16,9))
plt.imshow(wordcloud)
plt.axis("off")
plt.title('Frequencia das palavras')
plt.show()

input ('Pressione ENTER para continuar...')
