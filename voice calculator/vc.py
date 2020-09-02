import speech_recognition as sr
from tkinter import *
parent_calculator =Tk()
parent_calculator.title('Voice Calculator')
parent_calculator.geometry('500x500')

def voicec():
    st = sr.Recognizer()
    with sr.Microphone() as source:
        audio = st.listen(source)
        try:
            text = st.recognize_google(audio)
            a = text.split()
            for n,i in enumerate(a):
                if i == 'thousand':
                    a[n] = 1000
            for n,i in enumerate(a):
                if i == 'hundred':
                    a[n] = 100
            if a[1] == '+':
                label1 = Label(parent_calculator, text =  int(a[0])+int(a[2]))
                label1.pack()
            elif a[1] == 'plus':
                label1 = Label(parent_calculator, text =  int(a[0])+int(a[2]))
                label1.pack()
            elif a[1] == '-':
                label1 = Label(parent_calculator, text = int(a[0])-int(a[2]))
                label1.pack()
            elif a[1] == 'minus':
                label1 = Label(parent_calculator,text = int(a[0])-int(a[2]))
                label1.pack()
            elif a[1] == 'divided':
                label1 = Label(parent_calculator,text = int(a[0])/int(a[-1]))
                label1.pack()
            elif a[1] == '*':
                label1 = Label(parent_calculator,text = int(a[0])*int(a[2]))
                label1.pack()
            elif a[1] == 'into':
                label1 = Label(parent_calculator,text = int(a[0])*int(a[2]))
                label1.pack()
            elif a[1] == 'multiply':
                label1 = Label(parent_calculator,text = int(a[0])*int(a[2]))
                label1.pack()
            elif a[1] == 'in':
                label1 = Label(parent_calculator,text = int(a[0])*int(a[2]))
                label1.pack()
            else:
                print('cant understand')
        except:
            print('Speak again!!')
button = Button(parent_calculator, text = 'tap to speak', command = voicec)
button.pack()
parent_calculator.mainloop()
