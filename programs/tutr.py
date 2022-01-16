# Tutr Documentation Program for DarkOS
def tutr(pkg):
    if pkg.lower() == 'tutr pkg':
        print('''Package manager Documentation:
        -1 How to install packages
            First download the programlist using "pkgm pullpkgs"
            Next is to install a package using pkgm install [package]
            Next is to add the command to commandhandler.py
            ''')