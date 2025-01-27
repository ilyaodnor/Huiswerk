import tkinter as tk

window = tk.Tk()
window.title("Light Switch")

light = False

def on_off():
    global light
    light = not light  
    if light:
        print('Light is ON')
        button.config(text='Light is ON', bg= 'yellow',fg="black", font= 'bold')
        window.config(bg='yellow')
    else:
        print('Light is OFF')
        button.config(text='Light is OFF', bg = 'white', fg="black")
        window.config(bg='white')

button = tk.Button(window, text="Light is OFF", bg="white", fg="black", command=on_off)
button.pack(pady=20, padx=20)

window.mainloop()
