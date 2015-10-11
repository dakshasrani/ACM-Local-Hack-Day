from clarifai.client import ClarifaiApi
from wordcloud import WordCloud
import matplotlib
matplotlib.use("TkAgg")
import json
import matplotlib.pyplot as plt
import pylab

clarifai_api = ClarifaiApi("2N6hHrw6ECUTstHErD8UDBp7jhdJZDcNUpbQs9K6","ckT1Mk5oR-GX9i-65J8TC7nn_Lv9B_aaahtHqTLm")

#Counting number of files
import os
directory = '/Users/RichaShah/Documents/LocalHackDay/Images/'
# directory = '/Users/RichaShah/Documents/Personal/Photos/December 2014 Trip Sorted Photos/Richa\'s iPad/12-28 Big Sur'
number_of_files = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))])

tags = ""
for item in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, item)):
        file_path = '/Users/RichaShah/Documents/LocalHackDay/Images/'
        file_path += str(item)
        # print file_path

        filter_words = ['women','woman', 'man', 'men', 'adult', 'wear', 'clothing', 'one', 'two', 'three', 'four', 'boy', 'girl']
        result = clarifai_api.tag_images(open(file_path,'rb'))

        for word in result["results"][0]['result']['tag']['classes']:
            if word not in filter_words:
                tags += json.dumps(word).replace('"',"")
                tags += " "

print tags

wordcloud = WordCloud().generate(tags)
img=plt.imshow(wordcloud)
plt.axis("off")
plt.savefig('/Users/RichaShah/Documents/LocalHackDay/wordcloud.png')

# execfile('/Users/RichaShah/Documents/LocalHackDay/GetOutput.py')