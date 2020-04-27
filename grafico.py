# -*- coding: utf-8 -*-

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from tkinter import *
  
class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "12")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 20
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 30
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 30
        self.terceiroContainer.pack()
    
        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 10
        self.quartoContainer.pack(side=RIGHT)
  
        self.titulo = Label(self.primeiroContainer, text="Caminho do texto")
        self.titulo["font"] = ("Arial", "12", "bold")
        self.titulo.pack()
  
        self.nomeLabel = Label(self.segundoContainer,text="Caminho", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
  
        self.caminho = Entry(self.segundoContainer)
        self.caminho["width"] = 40
        self.caminho["font"] = self.fontePadrao
        self.caminho.pack(side=LEFT)
  
        self.executar = Button(self.terceiroContainer)
        self.executar["text"] = "Nuvem de Palavras"
        self.executar["font"] = ("Calibri", "10")
        self.executar["width"] = 30
        self.executar["command"] = self.nuvem
        self.executar.pack()

        self.mensagem = Label(self.terceiroContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
    
        self.sair = Button(self.quartoContainer)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 10
        self.sair["command"] = self.quartoContainer.quit
        self.sair.pack(side=RIGHT)
		
    def nuvem(self):
        if self.caminho.get() != "":
            stop_words = set(stopwords.words("portuguese"))
            stop_words.update(('-', '"','.',',','!', ':', '','de','acima','tudo','à','é','ú','Com','O','Que','Um','Uma','aqui','às','2005', '28', 'A','As','E','Os'))
            stop_words.update(set(STOPWORDS))
            texto = open(self.caminho.get(),'r').read()
            wordcloud = WordCloud(stopwords = stop_words, max_font_size=200 ,width = 1024, height = 728).generate(texto)
            plt.figure(figsize=(16,9))
            plt.imshow(wordcloud)
            plt.axis("off")
            plt.title('Frequencia das palavras')
            plt.show()
        else:
            self.mensagem["text"] = "Informe o caminho!!!"
  
root = Tk()
Application(root)
root.mainloop()