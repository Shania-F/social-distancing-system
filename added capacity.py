from keras.models import load_model
import cv2
import numpy as np
import tkinter
from tkinter import messagebox
import smtplib

root = tkinter.Tk()
root.withdraw()

model = load_model('face_mask_detection_alert_system.h5') # trained deep learning model
face_det_classifier=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

vid_source=cv2.VideoCapture(0)

text_dict={0:'Mask Present',1:'No Mask'}
rect_color_dict={0:(0,255,0),1:(0,0,255)} # green for mask, and red for no mask
SUBJECT = "No Face Mask"   
TEXT = "Visitor has been detected without a face mask. Entrance is denied."

# Capacity Control Parameters
cap = 1000
allowedcap=0.5 * cap; #Currently: 50%
ctr = 0
 
# continuously detect camera feed
while(True):
    ret, img = vid_source.read()
    grayscale_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_det_classifier.detectMultiScale(grayscale_img,1.3,5)  

    for (x,y,w,h) in faces:
        face_img = grayscale_img[y:y+w,x:x+w]
        resized_img = cv2.resize(face_img,(112,112))
        normalized_img = resized_img/255.0
        reshaped_img = np.reshape(normalized_img,(1,112,112,1))
        result=model.predict(reshaped_img)

        label=np.argmax(result,axis=1)[0]
      
        cv2.rectangle(img,(x,y),(x+w,y+h),rect_color_dict[label],2)
        cv2.rectangle(img,(x,y-40),(x+w,y),rect_color_dict[label],-1)
        cv2.putText(img, text_dict[label], (x, y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,0),2) 
        
        # label is 1, i.e no mask
        if (label == 1):
            # display message to tell user to wear a mask 
            # access is denied till they wear mask
            messagebox.showwarning("Warning","Access Denied. Please wear a Face Mask")
            
            # email is sent if visitor is not wearing face mask 
            message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls() # tunneled transport layer security
            mail.login('test@gmail.com','test')
            mail.sendmail('test@gmail.com','test@gmail.com',message)
            mail.close
        else:
            pass
            break

    cv2.imshow('Video Feed',img)
    key=cv2.waitKey(1)
    
    # key 27 is Esc; video feed ends on pressing Esc
    if(key==27):
        break
        
# Capacity Check & Display
if (label == 0):
    ctr+=1
    if (ctr > allowedcap):
        print("CAPACITY FULL; ENTRY DENIED")
        ctr-=1
        print("Current Capacity:",ctr)        
    else:
        print("ENTRY PERMITTED")
        print("Current Capacity:",ctr)        
        
cv2.destroyAllWindows()
vid_source.release()
