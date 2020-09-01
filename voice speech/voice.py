from tkinter import *
import speech_recognition as sr
parent_window = Tk()

parent_window.title('Voice')
parent_window.geometry('500x500')

def voice():
    r = sr.Recognizer()
    label0 = Label(parent_window,text ='listening')
    label0.pack()
    with sr.Microphone() as source:
        
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            label1 = Label(parent_window,text = text)
            label1.pack()      
        except:
            label2 = Label(parent_window, text = 'not audible')
button = Button(parent_window, text = 'tap to speak', command = voice)
button.pack()
parent_window.mainloop()
