from commandhandler import check

def mainwindow():
    print("Please know that this is a beta build. \n PKGM is currently not working!")
    while True:
        option = input("-> ")
        check(option)