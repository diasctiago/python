# -*- coding: utf-8 -*-

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords

#print('\n')
#input('Pressione ENTER para iniciar...')

stop_words = set(stopwords.words("portuguese"))
stop_words.update(('-', '"','.',',','!', ':', ';','de','acima','tudo','à','é','ú','Com','O','Que','Um','Uma','aqui','às','2005', '28', 'A','As','E','Os'))
stop_words.update(set(STOPWORDS))
texto = open('C:\Python\onu.txt','r').read()
wordcloud = WordCloud(stopwords = stop_words, max_font_size=200 ,width = 1024, height = 728).generate(texto)
plt.figure(figsize=(16,9))
plt.imshow(wordcloud)
plt.axis("off")
plt.title('Frequencia das palavras')
plt.show()

#print('\n')
#input('Pressione ENTER para finalizar...')