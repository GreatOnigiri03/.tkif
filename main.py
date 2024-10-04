import tkinter

import tkinter.filedialog
import tkinter.messagebox

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
    image = tkinter.filedialog.askopenfilename()

    canvas.delete('all')

    try:
        reader.Reader().read_image(image, canvas)

        print(f'Successfully read "{image}".')
        root.title(f'.TKIF Built-In Reader - "{image}"')

    except Exception as exception:
        print(f'Exception has raised while reading "{image}".')
        print(exception)

        root.title(f'.TKIF Built-In Reader')

        tkinter.messagebox.showerror(
            title=f'Error',
            message=f'"{image}".\n{exception}'
        )


def exit_reader():
    exit()


main_menu = tkinter.Menu()
file_menu = tkinter.Menu()

file_menu.add_command(label='Open', command=open_image)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=exit_reader)

main_menu.add_cascade(label='File', menu=file_menu)

root.config(menu=main_menu)
root.mainloop()
