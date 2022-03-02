from commandhandler import check


def mainwindow():
    print("Please know that this is a beta build.")
    while True:
        option = input("-> ")
        check(option)
