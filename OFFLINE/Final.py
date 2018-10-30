from tkinter import *
import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from PIL import Image, ImageTk








window = Tk()
window.title("Recog: Face Recognition Based Attendance")
window.geometry("800x600")
window.state('zoomed')
#window.attributes('-fullscreen', True) full screen, no title bar

class Example(Frame):#note example word used instead of Window, no problem
    
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)

        Example.txt1=0
        Example.txt2=""
        self.image = Image.open("./layout/bgone.png")#set the background
        self.img_copy = self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        #two labels, for notification and attendance defined globally
        self.label1 = Label(self, text="", font=(
            "Helvetica", 18), width=0, height=0, fg="#444444")
        self.label1.place(x=485, y=315)
        self.label1.config(bg="White")
        self.label2 = Label(self, text="", font=(
            "Helvetica", 18), width=0, height=0, fg="#444444")
        self.label2.place(x=485, y=507)
        self.label2.config(bg="White")

        
        self.showHeader()
        self.takeImageBtn()
        self.trainImageBtn()
        self.trackImageBtn()
        self.quitBtn()
        self.clearID()
        self.clearName()
        self.showLabels()
        self.showText()
        

    #clear Button
    def clearID(self):
        image = PhotoImage(file="./layout/clearid.png")
        qbtn = Button(self, text="Clear ID", width=124, height=44,command=self.clearvalid)
        qbtn.config(image=image)
        qbtn.image = image  # real button definition
        qbtn.place(x=830, y=200)
        self.master.title("GUI")  # name of the window, should be outside
        self.pack(fill=BOTH, expand=1)
    
    #function that will clear the value
    def clearvalid(self):    
        res = ""
        self.label1.configure(text= res)
        Example.txt1.delete(0, END)


    #clear name button
    def clearName(self):
        image = PhotoImage(file="./layout/clearname.png")
        qbtn = Button(self, text="Clear Name", width=124, height=44,command=self.clearvalname)
        qbtn.config(image=image)
        qbtn.image = image  # real button definition
        qbtn.place(x=830, y=255)
        self.master.title("GUI")  # name of the window, should be outside
        self.pack(fill=BOTH, expand=1)
    
    #function that will clear the name value
    def clearvalname(self):   
        res = ""
        self.label1.configure(text= res)
        Example.txt2.delete(0, END)

    #function to display textboxes
    
    def showText(self):
        Example.txt1 = Entry(width=18, font=("Helvetica", 24))
        Example.txt1.pack()
        Example.txt1.place(x=488, y=200)
        Example.txt2 = Entry(width=18, font=("Helvetica", 24))
        Example.txt2.pack()
        Example.txt2.place(x=488, y=250)

    #function to display all labels
    def showLabels(self):
        load=Image.open("./layout/label_one.png")
        render=ImageTk.PhotoImage(load)
        img=Label(self,text="Enter ID",image=render,width=90,height=40)
        img.image=render
        img.place(x=383,y=200)

        load = Image.open("./layout/label_two.png")
        render = ImageTk.PhotoImage(load)
        img2 = Label(self, text="Enter Name",image=render, width=138, height=38)
        img2.image = render
        img2.place(x=338, y=250)

        load = Image.open("./layout/notification.png")
        render = ImageTk.PhotoImage(load)
        img3 = Label(self, text="Notification",image=render, width=138, height=35)
        img3.image = render
        img3.place(x=338, y=310)

        load = Image.open("./layout/attendance.png")
        render = ImageTk.PhotoImage(load)
        img2 = Label(self, text="Attendance",image=render, width=138, height=35)
        img2.image = render
        img2.place(x=338, y=500)


    #take image button
    def takeImageBtn(self):
        image=PhotoImage(file="./layout/capture.png")
        qbtn = Button(self, text="Take Image",width=150,height=50,command=self.takebtnaction)
        qbtn.config(image=image)
        qbtn.image=image  # real button definition
        qbtn.place(x=245.75, y=400)
        self.master.title("GUI")  # name of the window, should be outside
        self.pack(fill=BOTH, expand=1)
    
    def takebtnaction(self):
        
        Id=self.txt1.get()      
        name=self.txt2.get()
        if(Id.isdigit() and name.isalpha()):
            cam = cv2.VideoCapture(0)
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector=cv2.CascadeClassifier(harcascadePath)
            sampleNum=0
            while(True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                    #incrementing sample number 
                    sampleNum=sampleNum+1
                    #saving the captured face in the dataset folder TrainingImage
                    cv2.imwrite("TrainingImage\ "+ str(name) +"."+ str(Id) +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                    #display the frame
                    cv2.imshow('frame',img)
                #wait for 100 miliseconds 
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                # break if the sample number is morethan 100
                elif sampleNum>60:
                    break
            cam.release()
            cv2.destroyAllWindows() 
            entry=[]
            entry.append(Id)
            entry.append(name)
         #   for i in range(1,3):
         #       worksheet.update_cell(end_row, i, entry[i-1])
            res = "Images Saved for ID : " + str(Id) +" Name : "+ name
            row = [Id , name]
            with open('StudentDetails\StudentDetails.csv','a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
            self.label1.configure(text= res)
        else:
            if(Id.isdigit()):
                res = "Enter Alphabetical Name"
                self.label1.configure(text= res)
            if(name.isalpha()):
                res = "Enter Numeric Id"
                self.label1.configure(text= res)

    #Example of changing text by clicking a button, can be set on anything else as well
    def trainImageBtn(self):
        image=PhotoImage(file="./layout/train.png")
        qbtn = Button(self, text="Train Image",width=150,height=50,command=self.trainBtnAction)
        qbtn.config(image=image)
        qbtn.image=image  # real button definition
        qbtn.place(x=487, y=400)
        self.master.title("GUI")  # name of the window, should be outside
        self.pack(fill=BOTH, expand=1)

    #now on clicking sets the new text in the labels, can be changed
    def trainBtnAction(self):
        def getImagesAndLabels(path):
            #get the path of all the files in the folder
            imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
            #print(imagePaths)
    
            #create empth face list
            faces=[]
            #create empty ID list
            Ids=[]
            #now looping through all the image paths and loading the Ids and the images
            for imagePath in imagePaths:
                #loading the image and converting it to gray scale
                pilImage=Image.open(imagePath).convert('L')
                #Now we are converting the PIL image into numpy array
                imageNp=np.array(pilImage,'uint8')
                #getting the Id from the image
                try:
                    Id=int(os.path.split(imagePath)[-1].split(".")[1])
                except ValueError:
                    pass
                # extract the face from the training image sample
                faces.append(imageNp)
                Ids.append(Id)        
            return faces,Ids
        #print(self.label1['text'])#set text by using = and the text to display
        #print(self.label2['text'])
        #self.label1['text']="Changed first label"
        #self.label2['text']="Changed second label"
        recognizer = cv2.face_LBPHFaceRecognizer.create()#recognizer = cv2.face.LBPHFaceRecognizer_create()#recognizer=cv2.createLBPHFaceRecognizer()
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector =cv2.CascadeClassifier(harcascadePath)
        faces,Id = getImagesAndLabels("TrainingImage")
        recognizer.train(faces, np.array(Id))
        recognizer.save("TrainingImageLabel\Trainner.yml")
        res = "Image Trained"#+",".join(str(f) for f in Id)
        self.label1.configure(text= res)

    


    #track image button
    def trackImageBtn(self):
        image=PhotoImage(file="./layout/track.png")
        qbtn = Button(self, text="Track Image",width=150,height=50,command=self.trackbtnaction)
        qbtn.config(image=image)
        qbtn.image=image  # real button definition
        qbtn.place(x=728.5, y=400)
        self.master.title("GUI")  # name of the window, should be outside
        self.pack()
    
    
    def trackbtnaction(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
        recognizer.read("TrainingImageLabel\Trainner.yml")
        harcascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath);    
        df=pd.read_csv("StudentDetails\StudentDetails.csv")
        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX        
        col_names =  ['Id','Name','Date','Time']
        attendance = pd.DataFrame(columns = col_names)
        b=[]
        x1,x2,x3,x4="","","",""   
        while True:
            ret, im =cam.read()
            gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            faces=faceCascade.detectMultiScale(gray, 1.2,5)    
            for(x,y,w,h) in faces:
                cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
                Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
                if(conf < 50):
                    ts = time.time()      
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    aa=df.loc[df['Id'] == Id]['Name'].values
                    tt=str(Id)+"-"+aa
                    x1=str(Id)
                    x2=str(aa[0])
                    x3=str(date)
                    x4=str(timeStamp)
                    attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                
                else:
                    Id='Unknown'                
                    tt=str(Id)  
                if(conf > 75):
                    noOfFile=len(os.listdir("ImagesUnknown"))+1
                    cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
                cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
            attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
            cv2.imshow('im',im) 
            if (cv2.waitKey(1)==ord('q')):
                break
        ts = time.time()      
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Hour,Minute,Second=timeStamp.split(":")
        fileName="Attendance\Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
        attendance.to_csv(fileName,index=False)
        cam.release()
        cv2.destroyAllWindows()
        b.append(x1[0:])
        b.append(x2[0:])
        b.append(x3[0:])
        b.append(x4[0:])

        lst=[]
        lst.extend(b)
    
       # values_list = worksheet1.get_all_values()
       # last_row=len(values_list)+1#getting last row


      #  for i in range(1,5):#from cell 1 to 4
      #      worksheet1.update_cell(last_row,i,lst[i-1])#saving values from 0 to 3
    

       # values_list = worksheet1.get_all_values()
        #print(values_list)
        self.label2.configure(text= attendance)#Attendance with col name
        #self.label2.configure(text= b)#attendance without col name
      #  list_of_lists = worksheet.get_all_values()
        #print(list_of_lists)#prints student details on console


    #quit button
    def quitBtn(self):
        image = PhotoImage(file="./layout/quit.png")
        qbtn = Button(self, text="Quit", width=150, height=50,command=exit)
        qbtn.config(image=image)
        qbtn.image = image  # real button definition
        qbtn.place(x=970, y=400)
        self.master.title("GUI")  # name of the window, should be outside
        self.pack(fill=BOTH, expand=1)

    #function to show title of the project: Fusion
    def showHeader(self):#for the fusion title
        #load = Image.open("./layout/header.png")
        load = Image.open("./layout/headertwo.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=383, y=0)

    def _resize_image(self, event):#to have bg resized as you adjust the window

        new_width = event.width
        new_height = event.height
        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


e = Example(window)
#e.pack(fill=BOTH, expand=YES)
window.mainloop()
