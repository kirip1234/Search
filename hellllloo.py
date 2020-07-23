import pandas as pd
from tkinter import *
import webbrowser


root= Tk()

root.title('Cable Management')
root.geometry('400x100')

title_label = Label(root, text="Cable Management", font=("Helvetica" , 16))



def callback(url):
    webbrowser.open_new(r'C:\Users\kirip\OneDrive\Desktop\Python\cables.xlsx')


e = Entry(root, width=50)
e.pack()

def find():
    top = Toplevel()
    top.title('Cable Results')
    top.geometry('800x499')
    df = pd.read_excel(r'C:\Users\kirip\OneDrive\Desktop\Python\cables.xlsx') 
    dt = df.loc[df['Node_Name'] =='ML.AFDrSW005']
    print(dt)
    
    
    
    



link1 = Label(root, text="View full list of cables", fg="blue", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback(r'C:\Users\kirip\OneDrive\Desktop\Python\cables.xlsx'))


f5 = Frame(root, width=800, height=20, bg='#1959c1')
f5.pack(side=BOTTOM)

 
        



myButton = Button(root, text="Search" , command=find)
myButton.pack()

credits_label = Label(f5, text=' '*8 + 'Developed by 8888', bg='#1959c1', fg='#eff0f2', width=48)
credits_label.pack(side=RIGHT)

root.mainloop()
