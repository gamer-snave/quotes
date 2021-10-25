import tkinter as tk
from tkinter import ttk
from tkinter.constants import EXTENDED
import requests
from threading import Thread
api="http://api.quotable.io/random"
quotes=[]
jokes=[]
quote_number=0
windows=tk.Tk()
windows.geometry("988x260")
windows.title("RANDOM QUOTES")
windows.grid_columnconfigure(0, weight=1)
windows.resizable(0,0)
windows.configure(bg="grey")

#c
def preload_quotes():
    global quotes
    try:
        print("***Loading More Quotes***")
        for x in range(10):
            random_quote=requests.get(api).json()
            content=random_quote["content"]
            author=random_quote["author"]
            quote=content + "\n\n" + "By   " + author
            print(content)

            quotes.append(quote)
        print("Finished Loading Quotes")
    
        preload_quotes()       
    except:raise ConnectionRefusedError




def get_quote():
    global quote_label
    global quotes
    global quote_number

    quote_label.configure(text=quotes[quote_number])
    quote_number=quote_number+1
    print(quote_number)

    if  quotes[quote_number]==quotes[-3]:
        thread=Thread(target=preload_quotes)
        thread.start()



# def get_joke():





#ui
quote_label=tk.Label(windows, text="click on the button to generate a random Quote",
                    height=6,
                    pady=10,
                    padx=10,
                    wraplength=800,
                    font=('Helvatica', 14)
)
quote_label.grid(row=0, column=0, sticky="WE", padx=20, pady=10)
frame=ttk.LabelFrame(windows).grid(row=1,column=1)
button=tk.Button(frame,text="Quote", command=get_quote, bg='#8052cc', fg='#ffffff', activebackground='grey', font=('Helvatica', 14))
button.grid(row=1, column=0, sticky="WE", padx=10, pady=10)

button2=tk.Button(frame,text="Joke", command='', bg='#8052cc', fg='#ffffff', activebackground='grey', font=('Helvatica', 14))
button2.grid(row=1, column=1, sticky="WE", padx=10, pady=10)




#Run program
if __name__=="__main__": 
    windows.mainloop()

  