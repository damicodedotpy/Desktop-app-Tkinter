from tkinter import Tk, StringVar, font
from tkinter.ttk import Entry, Button, Label, Frame


def createPhrase(*args, **kwargs):
    for child in responseFrame.winfo_children():
        child.destroy()
    if name.get() and age.get():
        phrase = f'''Genial! Hola {age.get()}, tu edad es {name.get()}
        
                        n_n
                        '''
        Label(responseFrame, text=phrase).grid(row=3, column=0)
    elif not name.get() and not age.get():
        phrase = 'Pon tus datos prroo! >:('
        Label(responseFrame, text=phrase).grid(row=3, column=0)
        
    elif name.get() or age.get():
        phrase = 'Todos! animal...'
        Label(responseFrame, text=phrase).grid(row=3, column=0)
    
    for child in responseFrame.winfo_children():
        child.grid_configure(padx=30, pady=(0,30))

window = Tk()
window.title('app chingona :3')
font.nametofont('TkDefaultFont').configure(size=15)

window.columnconfigure(0, weight=1, pad=50)

windowFrame = Frame(window, padding=(50, 30))
windowFrame.grid(row=0, column=0)

responseFrame = Frame(window)
responseFrame.grid(row=1, column=0)

name = StringVar(value='')
age = StringVar(value='')

nameLabel = Label(windowFrame, text='¿Cuál es tu nombre?:')
nameLabel.grid(row=0, column=0, sticky='W')
nameEntry = Entry(windowFrame, textvariable=name, font=('Segoe UI', 15), justify='center')
nameEntry.focus()
nameEntry.grid(row=0, column=1)

ageLabel = Label(windowFrame, text='¿Cuántos años tienes?:')
ageLabel.grid(row=1, column=0, sticky='W')
ageEntry = Entry(windowFrame, textvariable=age, font=('Segoe UI', 15), justify='center')
ageEntry.grid(row=1, column=1)

sendButton = Button(windowFrame, text='Enviar respuestas', command=createPhrase)
sendButton.grid(row=2, column=0, columnspan=2, sticky='WE')

for child in windowFrame.winfo_children():
    if not isinstance(child, Button):
        child.grid_configure(padx=15, pady=15)
        
window.bind('<Return>', createPhrase)
window.bind('<KP_Enter>', createPhrase)


window.mainloop()