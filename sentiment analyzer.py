from textblob import TextBlob
import tkinter.font as font
import nltk
from newspaper import Article
import tkinter

m = tkinter.Tk()
m.geometry('1000x1200')
m.configure(bg='#F3EEEC')

def initial():


    def mains():
        global photo
        global w
        hello=text.get()
        obj = TextBlob(hello)
        sentiment = obj.sentiment.polarity
        if (sentiment == 0):
            photo = tkinter.PhotoImage(file=r"project\neutrol.png")
            w = tkinter.Label(m, text='the person is in neutrol')
            p = tkinter.Label(m,image=photo)


        elif (sentiment < -0.5):
            photo = tkinter.PhotoImage(file=r"project\sad.png")
            w = tkinter.Label(m, text='the person is sad',width=20)
            p = tkinter.Label(m, image=photo )
        elif (sentiment < 0):
            photo = tkinter.PhotoImage(file=r"project\negative.png")
            w = tkinter.Label(m, text='the person is negative mood')
            p = tkinter.Label(m, image=photo)
        elif (sentiment > 0.5):
            photo = tkinter.PhotoImage(file=r"project\happy.png")
            w = tkinter.Label(m, text='the person is happy')
            p = tkinter.Label(m, image=photo)
        else:
            photo = tkinter.PhotoImage(file=r"project\positive.png")
            w = tkinter.Label(m, text='the person is in positive mood')
            p = tkinter.Label(m, image=photo)
        w.config(font=("Times", 25, "bold"))
        p.config(font=("Times", 25, "bold"))
        w.grid(row=3, column=6)
        p.grid(row=4, column=6)
    def ent():
        w.grid_forget()
        text.delete(first=0,last=22)

   # myFont = tkinter.Font(family="Times New Roman", size=12)


    a=tkinter.Label(m, text='Statement :')
    a.config(font=("Times", 25, "bold"))
    a.grid(row=1,columnspan=4)

    text = tkinter.Entry(m,width=35,highlightcolor='yellow')
    text.config(font=("Times", 15, "bold"))
    text.grid(row=1, column=6)


    button = tkinter.Button(m, text='submit', width=15,activebackground='red',bg='green', command=mains)
    buttons = tkinter.Button(m, text='try again', width=15, activebackground='red', bg='green', command=ent)
    button.config(font=("Times", 20, "bold"))
    button.config(font=("Times", 20, "bold"))
    button.grid(row=2, column=6)
    buttons.grid(row=2, column=7)
    m.mainloop()

initial()