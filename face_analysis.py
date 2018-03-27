#Ver 1.00
#Author Ananda Kalutantiri -University of Newcastle, Australia
# Access AWS Rekognition service using boto3 and display results in GUI
#wirtten in python 3.6
#@2018 Ananda Kalutantiri
#can be used by public for any legal purpose without permission and I am not liable for any damage or
#illegal use of this code by anyone.

import tkinter as tk
from tkinter import filedialog

import pprint
import boto3
import json
from PIL import Image
#from PIL.Image import core as _imaging
from PIL import ImageTk


def process_image():
    global file_path
    global emo_text
    file_path = filedialog.askopenfilename()
    SIMILARITY_THRESHOLD = 75.0
    a_key='access key'
    s_key='security code'
    r_name='ap-southeast-2'
    client = boto3.client('rekognition', aws_access_key_id=a_key, aws_secret_access_key=s_key, region_name=r_name )
    if __name__ == '__main__':
     #    client = boto3.client('rekognition')
    # create the center widgets
 #       try:
 #           center
 #       except NameError:
 #           pass
 #       else:
 #           center.destroy()
 #       center = tk.Frame(root, bg='gray', width=1000, height=500, padx=3,pady=3)
        
        
        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)
        center.grid_columnconfigure(0, weight=3)
        ctr_left = tk.Frame(center, bg='light blue', width=650, height=500)
        try:
            ctr_right    
        except NameError:
            pass
        else:
            ctr_right.destroy()
            
        ctr_right = tk.Frame(center, bg='light yellow', width=350, height=500, padx=3, pady=3)
        ctr_left.grid(row=0, column=0, sticky="nesw")
        ctr_right.grid(row=0, column=1, sticky="nw")

        # Our source image: http://i.imgur.com/OK8aDRq.jpg
        img=Image.open(file_path)
        width,height=img.size
        thumb_h=500
        if height > thumb_h:
            thumb_w=int(thumb_h*width/height)
            img=img.resize((thumb_w, thumb_h), Image.ANTIALIAS)
        photo=ImageTk.PhotoImage(img)
        c_photo_label = tk.Label(ctr_left, image=photo)
        c_photo_label.image = photo
        c_photo_label.pack()
            
                           
        with open(file_path, 'rb') as source_image:
            source_bytes = source_image.read()

        # Our target image: http://i.imgur.com/Xchqm1r.jpg
        #with open('target.jpg', 'rb') as target_image:
        #    target_bytes = target_image.read()

     #   response =    client.compare_faces(
     #                  SourceImage={ 'Bytes': source_bytes },
     #                  TargetImage={ 'Bytes': target_bytes },
     #                  SimilarityThreshold=SIMILARITY_THRESHOLD
     #   )
#        print('Detect Face')
        
        response= client.detect_faces(Image={ 'Bytes': source_bytes }, Attributes=['ALL'])
    #    pprint.pprint(response)
    #    for feature in response['FaceDetail']:
    #       print (feature['FaceDetail'] + ' : '+ feature['Value'] + ' : ' + str(feature['Confidence']))
     #   for faceDetail in response['FaceDetails']:
#            print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
#                  + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old '  + faceDetail['Gender']['Value'] )
#            
#            print('Here are the other attributes:')
#            print('Smile : '+ str(faceDetail['Smile']['Value'] )+ ' with confidence level ' + str(format(faceDetail['Smile']['Confidence'],'.2f'))+'%')
#            print ('Emotions : ' + str(faceDetail['Emotions'][0]['Type'])+' with confidence level ' +str(format(faceDetail['Emotions'][0]['Confidence'],'.2f') )+'%')
        emo_text='\nFace Emotions and Details\n'    
        for faceDetail in response['FaceDetails']:
            emo_text='The detected face is between ' + str(faceDetail['AgeRange']['Low'])  + ' and '
            emo_text= emo_text  + str(faceDetail['AgeRange']['High']) + ' years old '  + str(faceDetail['Gender']['Value']) + '\n\n' 
            emo_text= emo_text  + 'Here are the other attributes:\n'  + 'Smile : '+ str(faceDetail['Smile']['Value'] )
            emo_text= emo_text  + ' with confidence level ' + str(format(faceDetail['Smile']['Confidence'],'.2f'))+'% \n' 
            emo_text= emo_text  + 'Emotions : ' + str(faceDetail['Emotions'][0]['Type'])+' with confidence level '
            emo_text= emo_text  + str(format(faceDetail['Emotions'][0]['Confidence'],'.2f') )
        
        response = client.detect_labels(Image={'Bytes': source_bytes})
    #    pprint.pprint(response)
        emo_text=emo_text + '% \n\n' + 'Other Details \n'                                              
        for label in response['Labels']:
            emo_text= emo_text + label['Name'] + ' : ' + str(format(label['Confidence'],'.2f')) +'%\n'

        
        emo_text= emo_text  + '\n\n Done...'
        
        try:
            c_label
        except NameError:
            pass

        else:
            c_label.pack_forget()
            c_label.destroy()
        c_label = tk.Label(ctr_right, text=emo_text)
        c_label.pack()
        

 
root = tk.Tk()
root.title( 'AI- Face Analysis')
root.geometry('{}x{}'.format(1000, 650))

# create all of the main containers
top_frame = tk.Frame(root, bg='light yellow', width=1000, height=100, pady=3)
center = tk.Frame(root, bg='gray', width=1000, height=500, padx=3,pady=3)
btm_frame = tk.Frame(root, bg='lavender', width=1000, height=45, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0,  sticky="ew")
center.grid(row=1, sticky="nsew")
btm_frame.grid(row=2, sticky="ew")

# create the widgets for the top frame
model_label = tk.Label(top_frame, padx = 15, pady=10, fg='green', bg='light yellow' ,font = "Helvetica 14 bold italic", text='Ok, I am ready, please load the photo!')
button_u = tk.Button(top_frame, padx = 5, pady=5, bg='blue', fg='white', font = "Helvetica 14 bold", text='Upload', width=10, command=process_image)
button_q = tk.Button(top_frame, padx = 5, pady=5, bg='blue', fg='white', font = "Helvetica 14 bold ",text='Quit', width=10, command=root.destroy)
#entry_W = Entry(top_frame, background="pink")
#entry_L = Entry(top_frame, background="orange")

# layout the widgets in the top frame
model_label.grid(row=0, columnspan=3)
button_u.grid(row=2, column=4 )
button_q.grid(row=2, column=6)


# create the center widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)
center.grid_columnconfigure(0, weight=3)

ctr_left = tk.Frame(center, bg='light blue', width=650, height=190)
ctr_right = tk.Frame(center, bg='light yellow', width=350, height=190, padx=3, pady=3)


ctr_left.grid(row=0, column=0, sticky="ns")
ctr_right.grid(row=0, column=1, sticky="ns")

root.mainloop()
#browsebutton = tk.Button(root, text="Browse", command=process_image).pack()


