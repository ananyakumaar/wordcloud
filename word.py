import sys
import numpy as np
from PIL import Image
import wikipedia
from wordcloud import WordCloud,STOPWORDS

a=str(input("Enter the word of which you want to make a word cloud:" ))
title=wikipedia.search(a)[0]
page=wikipedia.page(title)
text=page.content
print(text)

bg=np.array(Image.open("black2.jpeg"))
unwanted_word=set(STOPWORDS)
wordclo=WordCloud(background_color="black",max_words=400,mask=bg,stopwords=unwanted_word)
wordclo.generate(text)
wordclo.to_file("sample.png")

