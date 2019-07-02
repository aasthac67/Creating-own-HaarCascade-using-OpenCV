import urllib.request
import cv2
import numpy as np
import os

def store_raw_images():
    #http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00017222
    #http://image-net.org/api/text/imagenet.synset.geturls?wnid=n03028079
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00017222'   
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 1035
    
    if not os.path.exists('neg'):
        os.makedirs('neg')
        
    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
            img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))

def pos_img():
    img=cv2.imread("mummy.jpeg",cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(img, (50, 50))
    cv2.imwrite("mummy_pos_face.jpg",resized_image)

def create_pos_n_neg():
    for file_type in ['neg']:
        
        for img in os.listdir(file_type):

            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)

pos_img()
#create_pos_n_neg()
#store_raw_images()