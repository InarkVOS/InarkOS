import npyscreen
import os
w, h = os.get_terminal_size()

class TestApp(npyscreen.NPSApp):
    def __init__(self, usr):
        self.usr = usr
    def main(self):
        F  = npyscreen.Form(name = "InarkOS Text Editor",)
        maintext = F.add(npyscreen.MultiLineEdit, value = '', max_height=h-7, rely=1)
        fname    = F.add(npyscreen.TitleText, name = "Filename:", rely=h-3)
        F.edit()
        a = 0
        if fname.value.replace('/', '').replace('\\', '').replace(':', '').replace('*', '').replace('"', '').replace('>', '').replace('<', '').replace('|', '') != '':
            open(f'MainDrive/Users/{self.usr}/Desktop/{fname.value}', 'w').write(maintext.value)

def run(usr):
    App = TestApp(usr)
    App.run()