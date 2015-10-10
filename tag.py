import matplotlib.pyplot as plt
from wordcloud import WordCloud
 
text = "man woman recreation adult action travel leisure travel friends friends sky bridge beach beach recreation travel travel coffee man woman woman man"
 
wordcloud = WordCloud().generate(text)
img=plt.imshow(wordcloud)
plt.axis("off")
plt.show() 