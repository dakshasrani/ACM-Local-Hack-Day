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

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def create_word_cloud():
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads/')
    number_of_files = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))])

    tags = ""
    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, item)):
            file_path = directory
            file_path += str(item)

            if allowed_file(file_path):
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
    image_path = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'), 'wordcloud.png')
    plt.savefig(image_path)
    remove_uploaded_images()

def remove_uploaded_images():
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads/')
    number_of_files = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))])

    tags = ""
    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, item)):
            file_path = directory
            file_path += str(item)
            os.remove(file_path)