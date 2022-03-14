from commandhandler import check

def mainwindow(usr):
    print("Please know that this is a beta build.")
    while True:
        option = input(f"{usr}> ")
        check(option, usr)
