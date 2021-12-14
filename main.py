from tkinter import *
import gtts



app = Tk()
app.title("Delta TTA")
app.geometry("200x200")

Label_lbl = Label(app,text="Please Set Your Text In The TextBox:").pack()

Text_txt = Entry(app)
Text_txt.pack()

Label2_lbl = Label(app,text="Please Set Audio Name In The TextBox:").pack()

Text2_txt = Entry(app)
Text2_txt.pack()

def tta():
    TTS = gtts.gTTS(Text_txt.get(),lang='en')
    TTS.save(f"./{Text2_txt.get()}.mp3")

Create_btn = Button(app,text="Create",command=tta).pack()

app.mainloop()