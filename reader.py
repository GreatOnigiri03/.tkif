import tkinter
import configparser


class Reader:
    def __init__(self):
        self.image = configparser.ConfigParser()

    def read_image(self, file, canvas: tkinter.Canvas):

        if file.endswith('.tkif'):
            try:
                self.image.read(file)

                for section in self.image.sections():
                    if section.startswith('point'):
                        if section.endswith('pass'):
                            pass
                        else:
                            if (
                                self.image.has_option(section, 'x') and
                                self.image[section]['x'].isnumeric() and
                                self.image.has_option(section, 'y') and
                                self.image[section]['y'].isnumeric()
                            ):
                                canvas.create_line(
                                    int(self.image[section]['x']),
                                    int(self.image[section]['y']),
                                    int(self.image[section]['x'])+1,
                                    int(self.image[section]['y'])+1
                                )
                            else:
                                raise Exception('Parameters are Invalid or not Found.')

                    if section.startswith('line'):
                        if section.endswith('pass'):
                            pass
                        else:
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
                                            int(self.image[b]['y'])
                                        )
                                    else:
                                        raise Exception('Required Parameters Invalid or not Found.')
                                else:
                                    raise Exception('Required Sections not Found')
                            else:
                                raise Exception('Reqiured Parameters Invalid or not Found.')
            except Exception as exc:
                raise Exception(exc)
        else:
            raise Exception('Invalid File Format or File Path.')
