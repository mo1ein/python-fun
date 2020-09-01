import speech_recognition as sr
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
            print(int(a[0])+int(a[2]))
        elif a[1] == 'plus':
            print(int(a[0])+int(a[2]))
        elif a[1] == '-':
            print(int(a[0])-int(a[2]))
        elif a[1] == 'minus':
            print(int(a[0])-int(a[2]))
        elif a[1] == 'divided':
            print(int(a[0])/int(a[-1]))
        elif a[1] == '*':
            print(int(a[0])*int(a[2]))
        elif a[1] == 'into':
            print(int(a[0])*int(a[2]))
        elif a[1] == 'multiply':
            print(int(a[0])*int(a[2]))
        elif a[1] == 'in':
            print(int(a[0])*int(a[2]))
        else:
            print('cant understand')
    except:
        print('Speak again!!')
