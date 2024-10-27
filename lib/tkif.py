import tkinter
import configparser

parameters_exception = Exception('Required Parameters Invalid or not Found.')


def create_point(canvas: tkinter.Canvas, x, y, **kwargs):
    fill = kwargs.get('fill', 'black')
    activefill = kwargs.get('activefill', 'red')

    point = canvas.create_line(
        x,
        y,
        x+1,
        y+1,
        fill=fill,
        activefill=activefill
    )
    return point


class Reader:
    def __init__(self):
        self.image = configparser.ConfigParser()

    def read_image(self, file, canvas: tkinter.Canvas):

        if file.endswith('.tkif'):
            try:
                self.image.read(file)

                for section in self.image.sections():
                    if section.endswith('pass'):
                        pass
                    else:
                        color = 'black'
                        active_color = 'red'

                        if self.image.has_option(section, 'color'):
                            color = self.image[section]['color']
                        if self.image.has_option(section, 'active_color'):
                            active_color = self.image[section]['active_color']

                        if section.startswith('point'):
                            if (
                                self.image.has_option(section, 'x') and
                                self.image[section]['x'].isnumeric() and
                                self.image.has_option(section, 'y') and
                                self.image[section]['y'].isnumeric()
                            ):
                                create_point(
                                    canvas,
                                    int(self.image[section]['x']),
                                    int(self.image[section]['y']),
                                    color=color, activefill=active_color
                                )
                            else:
                                raise parameters_exception

                        if section.startswith('line'):
                            if (
                                self.image.has_option(section, 'a') and
                                self.image.has_option(section, 'b')
                            ):

                                a = self.image[section]['a']
                                b = self.image[section]['b']

                                if (
                                    self.image.has_section(a) and
                                    self.image.has_section(b)
                                ):
                                    if (
                                        self.image.has_option(a, 'x') and
                                        self.image[a]['x'].isnumeric() and
                                        self.image.has_option(a, 'y') and
                                        self.image[a]['y'].isnumeric() and
                                        self.image.has_option(b, 'x') and
                                        self.image[b]['x'].isnumeric() and
                                        self.image.has_option(b, 'y') and
                                        self.image[b]['y'].isnumeric()
                                    ):
                                        canvas.create_line(
                                            int(self.image[a]['x']),
                                            int(self.image[a]['y']),
                                            int(self.image[b]['x']),
                                            int(self.image[b]['y']),
                                            fill=color, activefill=active_color
                                        )
                                    else:
                                        raise parameters_exception
                                else:
                                    raise Exception('Required Sections not Found')
                            else:
                                raise parameters_exception

            except Exception as exc:
                raise Exception(exc)
        else:
            raise Exception('Invalid File Format or File Path.')
