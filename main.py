import tkinter
from tkinter.filedialog import askopenfilename
import reader

root = tkinter.Tk()

print('Hello, World!\n- - - - - - -')

root.title('.TKIF Built-In Reader')
root.geometry('640x480')

root.option_add("*tearOff", 'false')

canvas = tkinter.Canvas(
    width=640,
    height=480,
    bg='white'
)

canvas.place(x=0, y=0, anchor='nw')


def open_image():
    file = askopenfilename()

    canvas.delete('all')

    try:
        reader.Reader().read_image(file, canvas)
        print(f'Loaded "{file}".')
        root.title(f'.TKIF Built-In Reader - {file}')
    except Exception as exception:
        print(f'Exception has been raised while loading "{file}".')
        print(exception)


main_menu = tkinter.Menu()
file_menu = tkinter.Menu()

file_menu.add_command(label='Open', command=open_image)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=exit)

main_menu.add_cascade(label='File', menu=file_menu)

root.config(menu=main_menu)
root.mainloop()
