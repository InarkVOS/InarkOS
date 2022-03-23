import npyscreen
import os
w, h = os.get_terminal_size()

class TextEditor(npyscreen.NPSApp):
    def __init__(self, usr):
        self.usr = usr
    def main(self):
        F        = npyscreen.Form(name = "InarkOS Text Editor",)
        maintext = F.add(npyscreen.MultiLineEdit, value = '', max_height=h-7, rely=1)
        fname    = F.add(npyscreen.TitleText, name = "Filename:", rely=h-3)
        a        = 0
        F.edit()
        if fname.value.replace('/', '').replace('\\', '').replace(':', '').replace('*', '').replace('"', '').replace('>', '').replace('<', '').replace('|', '') != '':
            open(f'MainDrive/Users/{self.usr}/Desktop/{fname.value}', 'w').write(maintext.value)

def run(usr):
    try:
        App = TextEditor(usr)
        App.run()
        App = ''
    except AttributeError:
        print('There is a bug that you can only run the text editor once i dont know how to fix it. :P')
