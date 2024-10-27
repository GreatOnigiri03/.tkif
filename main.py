import tkinter

import tkinter.filedialog
import tkinter.messagebox

import lib.tkif

root = tkinter.Tk()

print('\nHello, World!\n')

root.title('.TKIF Built-In Reader')
root.geometry('800x600')
root.resizable(False, False)

root.option_add("*tearOff", 'false')

canvas = tkinter.Canvas(
    width=800,
    height=600,
    bg='white'
)

canvas.place(x=-1, y=-2, anchor='nw')


def command_file_new():

    total = canvas.find_all()
    canvas.delete('all')

    print(f'Canvas cleared. Total deleted {len(total)} objects.')


def command_file_open():
    image = tkinter.filedialog.askopenfilename()

    command_file_new()

    try:
        lib.tkif.Reader().read_image(image, canvas)

        print(f'Successfully read "{image}".')
        root.title(f'.TKIF Built-In Reader - "{image}"')

    except Exception as exception:
        print(f'Exception has raised while reading "{image}".')
        print(exception)

        root.title(f'.TKIF Built-In Reader')

        tkinter.messagebox.showerror(
            title=f'Error!',
            message=f'"{image}".\n{exception}'
        )


mouse_position = tkinter.StringVar(value=str())

main_menu = tkinter.Menu()
file_menu = tkinter.Menu()
view_menu = tkinter.Menu()

file_menu.add_command(label='New', command=command_file_new)
file_menu.add_command(label='Open', command=command_file_open)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=lambda: exit())

main_menu.add_cascade(label='File', menu=file_menu)

frame = tkinter.Frame(borderwidth=1, relief='ridge', background='white')
tkinter.Label(frame, textvariable=mouse_position, background='white').pack(anchor='w', expand=1)
frame.pack(anchor='sw', expand=1, fill='x')

root.bind('<Motion>', lambda mouse: mouse_position.set(f'{mouse.x}, {mouse.y}'))

root.config(menu=main_menu)
root.mainloop()
